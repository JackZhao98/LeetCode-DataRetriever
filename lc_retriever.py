
from datetime import datetime
import os
import requests
import time
import json
from lc_api import *

class LCDataRetriever:
    def __init__(self, cookie):
        self.cookie = {}
        try:
            self.cookie = dict(map(lambda x: (x.split('=')[0], x.split('=')[1]), cookie.split(';')))
        
        except:
            print("Please enter a valid cookie.")

        self.submissions = []
        self.headers = lc_headers

    # The Three Retrievers
    def retrieve_all(self):
        source = requests.get(lc_all, headers=self.headers, cookies=self.cookie)
        return json.loads(source.text)

    def retrieve_question(self, title_slug):
        api = lc_graphql
        json_data = {
            'operationName':'questionData',
            'query':query_string,
            'variables': {
                'titleSlug':title_slug
            }
        }
        query_header = {**self.headers, 'Referer':'https://leetcode.com/problems/%s/' % title_slug}
        
        query = requests.post(url=api, json=json_data, headers=query_header, cookies=self.cookie)
        
        ret = json.loads(query.text)

        if not ret['data']['question']:
            print(ret['errors'][0]['message'])
            return None
        else:
            return ret['data']['question']

    def retrieve_submissions(self, pages=-1, verbose=False, delay=2):
        limit = 20
        api = lc_submissions
        lastkey = ""
        has_next = True
        offset_val = 0
        while has_next and (pages > 0 or pages == -1):
            response = requests.get(api % {
                "lastkey":lastkey,
                "limit":str(limit),
                "offset":str(offset_val),
                }, headers=self.headers, cookies=self.cookie)

            try:
                tmp = json.loads(response.text)
                self.submissions += tmp['submissions_dump']
            except:
                print("Stuck...attempting retry at offset={}".format(offset_val))
                continue

            # Update parameters
            has_next = bool(tmp['has_next'])
            last_key = tmp['last_key']
            offset_val += limit
            if pages > 0:
                pages -= 1

            # Delay before next request
            time.sleep(delay)

            # Print message
            if verbose:
                print("Proceeding to page {}".format(offset_val//limit + 1))

        if verbose:
            print("All submissions have been loaded successfully!")

        return self.submissions


    # Helper function

    def naive_title_slug(self, title):
        tmp = title.lower()
        title_code = ""
        for c in tmp:
            if c in "abcdefghijklmnopqrstuvwxyz0123456789- ":
                title_code += c
        return title_code.replace(' ', '-').replace('---', '-')

    def question_id_lookup(self, query_resp):
        if not query_resp:
            return -1
        return query_resp['questionFrontendId']





class LCDownloader(LCDataRetriever):
    def __init__(self, cookie, path = "./", target_folder = "LeetCode Data"):
        super().__init__(cookie)
        if path:
            self.path = path
        else:
            print("Invalid path, set download target to default \'./\'")

        
        self.folder = target_folder if target_folder else "LeetCode Data"
        self.download_path = os.path.join(path, self.folder)

        if not os.path.exists(self.download_path):
            os.makedirs(self.download_path)
            print("Created folder: {}".format(self.download_path))
        else:
            print("Folder exists: {}".format(self.download_path))

    def download_submissions(self, pages = -1, submissions = [], mode = "md"):

        if mode.lower() == "md":
            is_md = True
        elif mode.lower() == "raw":
            is_md = False
        else:
            print("Wrong mode. Accepted modes:\n\t'md' -- MarkDown files\n\t'raw' -- Source code")
            return

        if not submissions:
            submissions = self.retrieve_submissions(pages = pages, verbose = False)

        for s in submissions:
            if s['status_display'] != "Accepted":
                continue
            if is_md:
                self.write_to_md(s)
            else:
                self.write_to_raw(s)

        print("Download complete!")


    def write_to_md(self, entry):
        md_template = '''# [%(id)s] %(title)s (%(difficulty)s)

%(small_tags)s

:+1: %(likes)s &nbsp; &nbsp; :thumbsdown: %(dislikes)s

## My Submission

- Runtime: %(runtime)s
- Completed time: %(time)s

```%(lang)s
%(code)s
```

## Content
%(contents)s

## Related Problems
%(related_problems)s

## What a(n) %(difficulty)s problem!
Among **%(submission)s** total submissions, **%(accepted)s** are accepted, with an acceptance rate of %(acc_rate)s. <br>

- Likes: %(likes)s
- Dislikes: %(dislikes)s

'''
        related_template = "[%(related_title)s](%(link)s) (%(related_difficulty)s) <br>"
        tag_template = "[![%(tag)s_badge](https://img.shields.io/badge/topic-%(tag)s-%(color)s.svg)](%(URL)s) "
        related = []

        base_url = "https://leetcode.com/problems/%s/"
        title = entry['title']
        question_info = self.retrieve_question(self.naive_title_slug(title))
        question_id = question_info['questionFrontendId']
        filename = os.path.join(self.download_path, f"[{question_id}] {title}.md")

        tags = []
        for tag in question_info['topicTags']:
            tags.append(tag_template % {
                "tag" : tag['name'].strip(),
                "URL" : base_url % question_info['titleSlug'],
                "color" : "green"
            })


        rel = json.loads(question_info['similarQuestions'])
        stats = json.loads(question_info['stats'])
        for r in rel:
            related.append(related_template % {
                "related_title" : r["title"], 
                "link" : base_url % r["titleSlug"],
                "related_difficulty" : r["difficulty"]
            })

        with open(filename, "w") as f:
            f.write(md_template % {
                "id" : question_id,
                "title" : title,
                "difficulty" : question_info['difficulty'],
                "small_tags" : ' '.join(tags),
                "URL" : base_url % question_info['titleSlug'],
                'lang' : entry['lang'],
                'runtime': entry['runtime'],
                'time': datetime.fromtimestamp(entry['timestamp']),
                'code' : entry['code'],
                'contents' : question_info['content'],
                'related_problems' : '\n'.join(related),
                'submission' : stats['totalSubmissionRaw'],
                'accepted' : stats['totalAcceptedRaw'],
                'acc_rate' : stats['acRate'],
                'likes' : question_info['likes'],
                'dislikes' : question_info['dislikes']
                })

    def write_to_raw(self, entry):
        title = entry['title']


    def extension(self, type_slug):
        lookup_table = {
            'cpp':'cpp',
            'java':'java',
            'python':'py',
            'python3':'py',
            'c':'c',
            'csharp':'cs',
            'javascript':'js',
            'ruby':'rb',
            'swift':'swift',
            'golang':'go',
            'scala':'scala',
            'kotlin':'kt',
            'rust':'rs',
            'php':'php',
            'typescript':'ts'
        }
        return lookup_table[type_slug]













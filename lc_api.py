lc_headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
            "authority": "leetcode.com",
        }

lc_all = "https://leetcode.com/api/problems/all/"
lc_submissions = "https://leetcode.com/api/submissions/?offset=%(offset)s&limit=%(limit)s&lastkey=%(lastkey)s"
lc_graphql = "https://leetcode.com/graphql"

query_string = 'query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      paidOnly\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    enableDebugger\n    envInfo\n    libraryUrl\n    adminUrl\n    __typename\n  }\n}\n'

md_template = '''# [%(id)s] %(title)s (%(difficulty)s)

%(small_tags)s

:+1: %(likes)s &nbsp; &nbsp; :thumbsdown: %(dislikes)s

---

## My Submission

- Language: %(lang)s
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
Among **%(submission)s** total submissions, **%(accepted)s** are accepted, with an acceptance rate of **%(acc_rate)s**. <br>

- Likes: %(likes)s
- Dislikes: %(dislikes)s

'''

related_template = "[%(related_title)s](%(link)s) (%(related_difficulty)s) <br>"

tag_template = "[![%(tag)s_badge](https://img.shields.io/badge/topic-%(tag)s-%(color)s.svg)](%(URL)s) "

raw_md_template = '''## [%(id)s] %(title)s (%(difficulty)s)

%(small_tags)s

👍  %(likes)s &nbsp; &nbsp; 👎  %(dislikes)s

---

## My Submission

- Language: %(lang)s
- Runtime: %(runtime)s
- Completed time: %(time)s

```%(lang)s
%(code)s
```

## Related Problems
%(related_problems)s

## What a(n) %(difficulty)s problem!
Among **%(submission)s** total submissions, **%(accepted)s** are accepted, with an acceptance rate of **%(acc_rate)s**.

- Likes: %(likes)s
- Dislikes: %(dislikes)s

'''


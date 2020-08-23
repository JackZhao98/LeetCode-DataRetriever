# LeetCode Data Retriever

<br>

<p>Doing LeetCode problems every day?</p>
<p>Trying to take notes in the mid-way but already far behind?</p>
<p>This project will help you.</p>

## Requirements
- **Python3.***
- **LeetCode Auth Cookie🍪** (None of your personal data will be collected)

## Submission Download
<p>Using your Cookie🍪, this script is able to collect all of your submission history with these information:</p>

- 'id' --> submission id
- 'lang' --> language used
- 'time' --> relative time of submission
- 'timestamp' --> time of submission
- 'status_display' --> submission status ('Accepted', 'Rejected', etc.)
- 'runtime' --> submission runtime
- 'is_pending' --> is pending?
- 'title' --> problem title
- 'memory' --> submission memory usage
- 'code' --> your code
- 'compare_result' --> a binary string where 1 represents "Correct" and 0 represents "Wrong"

# Usage
## LCDataRetriever
First, **initialize** the `LCDataRetriever(cookie = COOKIE)` object with your cookie. (This is a **required** parameter)

```python3
ld = LCDataRetriever(cookie = COOKIE)
```

### Submission Retriever
`retrieve_submissions(self, pages=-1, verbose=False, delay=2)` can be used as a submission info retreival tool.

- pages: number of pages you want to retrieve, -1 for all pages.
- verbose: print some bullshit to watch while waiting
- delay: time delay between two requests to avoid access denial.

Values are returned as a list of dict. 

```python3
ld.retrieve_submissions(pages=1)
```

### Question detail Retriever

`retrieve_question(self, title_slug)` can be used for querying a single question details.

- title_slug (**required**) a title format that you can found at the end of a question url. It looks like this:

    - "two-sum"
    - "n-queens-ii"
 
Values are returned as a dict

```python3
question_detail = ld.retrieve_question("3sum")
```

### "Everything" Retriever

`retrieve_all(self)`. As titled, this method gives you everything about your usage data, plus all 1500+ problem infomation, in a dict.

```python3
ld.retrieve_all()
```

## LCDownloader
**_A native built LeetCode data downloader_**

### __init__
Still, initialize with you LeetCode auth cookie.
`__init__(self, cookie, path = "./", target_folder = "LeetCode Data")`

- cookie (**required**)
- path: download directory
- target_folder: download folder name

```python3
d = LCDownloader(COOKIE)
```

### Download Submissions!
Call `download_submissions(self, pages = -1, submissions = [], mode = "md")` to download your submissions to the designated folder.

- pages: how many pages of submissions will be downloaded (-1 for all)
- submissions: fill in submissions if you have already retrieved submissions information
- mode: "md" or "raw"
    - md: a well-formatted Markdown file with rich information
    - raw: source code
    
```python3
d.download_submissions()
```

## Have Fun




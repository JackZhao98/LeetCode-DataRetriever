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

### Usage
**Step 1. Get submission details, stores in a `list` object**

```python3
submissions = get_submissions(Cookie, headers)
```

**Step 2. Use submission details to download**

This function will create a folder named "LeetCode Submissions" under designated directory. 
<br>
All codes will be written as files under this folder.

```python3
download_code(all_submissions, headers, Cookie, path = "./")
```

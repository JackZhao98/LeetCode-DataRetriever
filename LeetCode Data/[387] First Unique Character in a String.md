# [387] First Unique Character in a String (Easy)

[![Hash%20Table_badge](https://img.shields.io/badge/topic-Hash%20Table-green.svg)](https://leetcode.com/problems/first-unique-character-in-a-string/)  [![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/first-unique-character-in-a-string/) 

:+1: 2080 &nbsp; &nbsp; :thumbsdown: 117

---

## My Submission

- Language: python3
- Runtime: 172 ms
- Completed time: 2020-07-23 17:47:48

```python3
class Solution:
    def firstUniqChar(self, s: str) -> int:

        record = {}
        for c in s:
            if c not in record.keys():
                record[c] = 1
            else:
                record[c] += 1
        
        for i, c in enumerate(s):
            if record[c] == 1:
                return i
        return -1
```

## Content
<p>Given a string, find the first non-repeating character in it and return its index. If it doesn&#39;t exist, return -1.</p>

<p><b>Examples:</b></p>

<pre>
s = &quot;leetcode&quot;
return 0.

s = &quot;loveleetcode&quot;
return 2.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b> You may assume the string contains only lowercase English letters.</p>


## Related Problems
[Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/) (Medium) <br>

## What a(n) Easy problem!
Among **1065731** total submissions, **569150** are accepted, with an acceptance rate of **53.4%**. <br>

- Likes: 2080
- Dislikes: 117


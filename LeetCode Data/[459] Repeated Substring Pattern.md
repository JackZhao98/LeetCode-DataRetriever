# [459] Repeated Substring Pattern (Easy)

[![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/repeated-substring-pattern/) 

:+1: 1818 &nbsp; &nbsp; :thumbsdown: 170

---

## My Submission

- Language: python3
- Runtime: 24 ms
- Completed time: 2020-09-03 13:48:36

```python3
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        fold = s[1:] + s[:-1]
        return s in fold
```

## Content
<p>Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.</p>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> &quot;abab&quot;
<b>Output:</b> True
<b>Explanation:</b> It&#39;s the substring &quot;ab&quot; twice.
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> &quot;aba&quot;
<b>Output:</b> False
</pre>

<p><b>Example 3:</b></p>

<pre>
<b>Input:</b> &quot;abcabcabcabc&quot;
<b>Output:</b> True
<b>Explanation:</b> It&#39;s the substring &quot;abc&quot; four times. (And the substring &quot;abcabc&quot; twice.)
</pre>


## Related Problems
[Implement strStr()](https://leetcode.com/problems/implement-strstr/) (Easy) <br>
[Repeated String Match](https://leetcode.com/problems/repeated-string-match/) (Medium) <br>

## What a(n) Easy problem!
Among **351555** total submissions, **150342** are accepted, with an acceptance rate of **42.8%**. <br>

- Likes: 1818
- Dislikes: 170


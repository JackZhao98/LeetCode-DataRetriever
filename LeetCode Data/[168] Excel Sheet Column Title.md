# [168] Excel Sheet Column Title (Easy)

[![Math_badge](https://img.shields.io/badge/topic-Math-green.svg)](https://leetcode.com/problems/excel-sheet-column-title/) 

:+1: 1299 &nbsp; &nbsp; :thumbsdown: 257

---

## My Submission

- Language: python3
- Runtime: 36 ms
- Completed time: 2020-07-19 16:22:42

```python3
class Solution:
    def convertToTitle(self, n: int) -> str:
        key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ret = ""
  
        while n > 0:
            ret = key[n % 26 - 1] + ret
            n -= 1
            n //= 26
            
        return ret
```

## Content
<p>Given a positive integer, return its corresponding column title as appear in an Excel sheet.</p>

<p>For example:</p>

<pre>
    1 -&gt; A
    2 -&gt; B
    3 -&gt; C
    ...
    26 -&gt; Z
    27 -&gt; AA
    28 -&gt; AB 
    ...
</pre>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 1
<strong>Output:</strong> &quot;A&quot;
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 28
<strong>Output:</strong> &quot;AB&quot;
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> 701
<strong>Output:</strong> &quot;ZY&quot;
</pre>

## Related Problems
[Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/) (Easy) <br>

## What a(n) Easy problem!
Among **721686** total submissions, **224687** are accepted, with an acceptance rate of **31.1%**. <br>

- Likes: 1299
- Dislikes: 257


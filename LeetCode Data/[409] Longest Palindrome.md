# [409] Longest Palindrome (Easy)

[![Hash Table_badge](https://img.shields.io/badge/topic-Hash Table-green.svg)](https://leetcode.com/problems/longest-palindrome/) 

:+1: 1202 &nbsp; &nbsp; :thumbsdown: 89

## My Submission

- Runtime: 28 ms
- Completed time: 2020-08-14 14:11:32

```python3
class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        ret = 0
        for c in s:
            if c in seen:
                ret += 2
                seen.remove(c)
            else:
                seen.add(c)
        if seen:
            ret += 1
        return ret
                
```

## Content
<p>Given a string <code>s</code> which consists of lowercase or uppercase letters, return <em>the length of the <strong>longest palindrome</strong></em>&nbsp;that can be built with those letters.</p>

<p>Letters are <strong>case sensitive</strong>, for example,&nbsp;<code>&quot;Aa&quot;</code> is not considered a palindrome here.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abccccdd&quot;
<strong>Output:</strong> 7
<strong>Explanation:</strong>
One longest palindrome that can be built is &quot;dccaccd&quot;, whose length is 7.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a&quot;
<strong>Output:</strong> 1
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bb&quot;
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2000</code></li>
	<li><code>s</code> consits of lower-case <strong>and/or</strong> upper-case English&nbsp;letters only.</li>
</ul>


## Related Problems
[Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/) (Easy) <br>

## What a(n) Easy problem!
Among **335274** total submissions, **173433** are accepted, with an acceptance rate of 51.7%. <br>

- Likes: 1202
- Dislikes: 89


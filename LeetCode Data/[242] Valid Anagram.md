# [242] Valid Anagram (Easy)

[![Hash Table_badge](https://img.shields.io/badge/topic-Hash Table-green.svg)](https://leetcode.com/problems/valid-anagram/)  [![Sort_badge](https://img.shields.io/badge/topic-Sort-green.svg)](https://leetcode.com/problems/valid-anagram/) 

[Magic Portal](https://leetcode.com/problems/valid-anagram/)

## My Submission

- Runtime: 48 ms
- Completed time: 2020-07-23 15:58:09

```python3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        for i, j in zip(sorted(s), sorted(t)):
            if i != j:
                return False
            
        return True
```

## Content
<p>Given two strings <em>s</em> and <em>t&nbsp;</em>, write a function to determine if <em>t</em> is an anagram of <em>s</em>.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> <em>s</em> = &quot;anagram&quot;, <em>t</em> = &quot;nagaram&quot;
<b>Output:</b> true
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> <em>s</em> = &quot;rat&quot;, <em>t</em> = &quot;car&quot;
<b>Output: </b>false
</pre>

<p><strong>Note:</strong><br />
You may assume the string contains only lowercase alphabets.</p>

<p><strong>Follow up:</strong><br />
What if the inputs contain unicode characters? How would you adapt your solution to such case?</p>


## Related Problems
[Group Anagrams](https://leetcode.com/problems/group-anagrams/) (Medium) <br>
[Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/) (Easy) <br>
[Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) (Medium) <br>

## What a(n) Easy problem!
Among **1060315** total submissions, **603949** are accepted, with an acceptance rate of 57.0%. <br>

- Likes: 1690
- Dislikes: 145


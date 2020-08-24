# [125] Valid Palindrome (Easy)

[![Two%20Pointers_badge](https://img.shields.io/badge/topic-Two%20Pointers-green.svg)](https://leetcode.com/problems/valid-palindrome/)  [![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/valid-palindrome/) 

:+1: 1357 &nbsp; &nbsp; :thumbsdown: 3090

---

## My Submission

- Language: python3
- Runtime: 48 ms
- Completed time: 2020-08-03 13:45:03

```python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        j = len(s) - 1
        i = 0
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
```

## Content
<p>Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.</p>

<p><strong>Note:</strong>&nbsp;For the purpose of this problem, we define empty string as valid palindrome.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> &quot;A man, a plan, a canal: Panama&quot;
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> &quot;race a car&quot;
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>s</code> consists only of printable ASCII characters.</li>
</ul>


## Related Problems
[Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) (Easy) <br>
[Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) (Easy) <br>

## What a(n) Easy problem!
Among **1799401** total submissions, **662250** are accepted, with an acceptance rate of **36.8%**. <br>

- Likes: 1357
- Dislikes: 3090


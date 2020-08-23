# [520] Detect Capital (Easy)

[![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/detect-capital/) 

[Magic Portal](https://leetcode.com/problems/detect-capital/)

## My Submission

- Runtime: 32 ms
- Completed time: 2020-08-03 13:38:01

```python3
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        allCap = False
        firstCap = None
        for c, v in enumerate(word):
            if c == 0:
                firstCap = (v >= 'A' and v <= 'Z')
            else:
                if not firstCap:
                    if v >= 'A' and v <= 'Z':
                        return False
                else:
                    if c == 1:
                        allCap = (v >= 'A' and v <= 'Z')
                    else:
                        if allCap:
                            if v >= 'a' and v <= 'z':
                                return False
                        else:
                            if v >= 'A' and v <= 'Z':
                                return False
        return True
```

## Content
<p>Given a word, you need to judge whether the usage of capitals in it is right or not.</p>

<p>We define the usage of capitals in a word to be right when one of the following cases holds:</p>

<ol>
	<li>All letters in this word are capitals, like &quot;USA&quot;.</li>
	<li>All letters in this word are not capitals, like &quot;leetcode&quot;.</li>
	<li>Only the first letter in this word is capital, like &quot;Google&quot;.</li>
</ol>
Otherwise, we define that this word doesn&#39;t use capitals in a right way.

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> &quot;USA&quot;
<b>Output:</b> True
</pre>

<p>&nbsp;</p>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> &quot;FlaG&quot;
<b>Output:</b> False
</pre>

<p>&nbsp;</p>

<p><b>Note:</b> The input will be a non-empty word consisting of uppercase and lowercase latin letters.</p>


## Related Problems


## What a(n) Easy problem!
Among **313324** total submissions, **168992** are accepted, with an acceptance rate of 53.9%. <br>

- Likes: 639
- Dislikes: 278


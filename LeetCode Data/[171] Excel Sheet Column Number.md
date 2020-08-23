# [171] Excel Sheet Column Number (Easy)

[![Math_badge](https://img.shields.io/badge/topic-Math-green.svg)](https://leetcode.com/problems/excel-sheet-column-number/) 

[Magic Portal](https://leetcode.com/problems/excel-sheet-column-number/)

## My Submission

- Runtime: 44 ms
- Completed time: 2020-07-19 15:08:43

```python3
class Solution:
    def titleToNumber(self, s: str) -> int:
        l = len(s) - 1
        i = 0
        ret = 0
        while l >= 0:
            ret += (ord(s[i]) - ord('A') + 1) * (26 ** l)
            l -= 1
            i += 1
        return ret
        
            
```

## Content
<p>Given a column title as appear in an Excel sheet, return its corresponding column number.</p>

<p>For example:</p>

<pre>
    A -&gt; 1
    B -&gt; 2
    C -&gt; 3
    ...
    Z -&gt; 26
    AA -&gt; 27
    AB -&gt; 28 
    ...
</pre>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> &quot;A&quot;
<strong>Output:</strong> 1
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>&quot;AB&quot;
<strong>Output:</strong> 28
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>&quot;ZY&quot;
<strong>Output:</strong> 701
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 7</code></li>
	<li><code>s</code> consists only of uppercase English letters.</li>
	<li><code>s</code> is between &quot;A&quot; and &quot;FXSHRXW&quot;.</li>
</ul>


## Related Problems
[Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/) (Easy) <br>

## What a(n) Easy problem!
Among **586194** total submissions, **328728** are accepted, with an acceptance rate of 56.1%. <br>

- Likes: 1246
- Dislikes: 166


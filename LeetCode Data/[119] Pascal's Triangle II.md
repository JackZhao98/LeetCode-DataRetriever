# [119] Pascal's Triangle II (Easy)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/pascals-triangle-ii/) 

[Magic Portal](https://leetcode.com/problems/pascals-triangle-ii/)

## My Submission

- Runtime: 20 ms
- Completed time: 2020-08-12 12:27:52

```python3
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ret = [1]
        for i in range(rowIndex):
            ret = [x + y for (x, y) in zip(ret + [0], [0] + ret)]
        return ret
```

## Content
<p>Given an integer <code>rowIndex</code>, return the <code>rowIndex<sup>th</sup></code>&nbsp;row of the Pascal&#39;s triangle.</p>

<p>Notice&nbsp;that the row index starts from&nbsp;<strong>0</strong>.</p>

<p><img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif" /><br />
<small>In Pascal&#39;s triangle, each number is the sum of the two numbers directly above it.</small></p>

<p><strong>Follow up:</strong></p>

<p>Could you optimize your algorithm to use only <em>O</em>(<em>k</em>) extra space?</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> rowIndex = 3
<strong>Output:</strong> [1,3,3,1]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> rowIndex = 0
<strong>Output:</strong> [1]
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> rowIndex = 1
<strong>Output:</strong> [1,1]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;=&nbsp;rowIndex &lt;= 40</code></li>
</ul>


## Related Problems
[Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) (Easy) <br>

## What a(n) Easy problem!
Among **632059** total submissions, **320325** are accepted, with an acceptance rate of 50.7%. <br>

- Likes: 1017
- Dislikes: 201


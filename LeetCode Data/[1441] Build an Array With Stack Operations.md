# [1441] Build an Array With Stack Operations (Easy)

[![Stack_badge](https://img.shields.io/badge/topic-Stack-green.svg)](https://leetcode.com/problems/build-an-array-with-stack-operations/) 

[Magic Portal](https://leetcode.com/problems/build-an-array-with-stack-operations/)

## My Submission

- Runtime: 40 ms
- Completed time: 2020-05-09 19:47:30

```python3
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target_len = len(target)
        Max = target[-1]
        result = []
        i = 1
        index = 0
        while i <= Max:
            if target[index] == i:
                result.append("Push")
                index += 1
            else:
                result.append("Push")
                result.append("Pop")
            i += 1
        print(result)
        
        return result
```

## Content
<p>Given an array <code>target</code> and&nbsp;an integer <code>n</code>. In each iteration, you will read a number from &nbsp;<code>list = {1,2,3..., n}</code>.</p>

<p>Build the <code>target</code>&nbsp;array&nbsp;using the following operations:</p>

<ul>
	<li><strong>Push</strong>: Read a new element from the beginning&nbsp;<code>list</code>, and push it in the array.</li>
	<li><strong>Pop</strong>: delete the last element of&nbsp;the array.</li>
	<li>If the target array is already&nbsp;built, stop reading more elements.</li>
</ul>

<p>You are guaranteed that the target array is strictly&nbsp;increasing, only containing&nbsp;numbers between 1 to <code>n</code>&nbsp;inclusive.</p>

<p>Return the operations to build the target array.</p>

<p>You are guaranteed that the answer is unique.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> target = [1,3], n = 3
<strong>Output:</strong> [&quot;Push&quot;,&quot;Push&quot;,&quot;Pop&quot;,&quot;Push&quot;]
<strong>Explanation: 
</strong>Read number 1 and automatically push in the array -&gt; [1]
Read number 2 and automatically push in the array then Pop it -&gt; [1]
Read number 3 and automatically push in the array -&gt; [1,3]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> target = [1,2,3], n = 3
<strong>Output:</strong> [&quot;Push&quot;,&quot;Push&quot;,&quot;Push&quot;]
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> target = [1,2], n = 4
<strong>Output:</strong> [&quot;Push&quot;,&quot;Push&quot;]
<strong>Explanation: </strong>You only need to read the first 2 numbers and stop.
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> target = [2,3,4], n = 4
<strong>Output:</strong> [&quot;Push&quot;,&quot;Pop&quot;,&quot;Push&quot;,&quot;Push&quot;,&quot;Push&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= target.length &lt;= 100</code></li>
	<li><code>1 &lt;= target[i]&nbsp;&lt;= 100</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>target</code> is strictly&nbsp;increasing.</li>
</ul>


## Related Problems


## What a(n) Easy problem!
Among **31255** total submissions, **21511** are accepted, with an acceptance rate of 68.8%. <br>

- Likes: 156
- Dislikes: 187


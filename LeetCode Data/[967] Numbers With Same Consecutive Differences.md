# [967] Numbers With Same Consecutive Differences (Medium)

[![DynamicProgramming_badge](https://img.shields.io/badge/topic-DynamicProgramming-green.svg)](https://leetcode.com/problems/numbers-with-same-consecutive-differences/) 

:+1: 480 &nbsp; &nbsp; :thumbsdown: 106

## My Submission

- Runtime: 60 ms
- Completed time: 2020-08-18 17:57:21

```python3
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        table = {}
        for i in range(10):
            tmp = []
            if i + K <= 9:
                tmp.append(i + K)
            if i - K >= 0:
                tmp.append(i - K)
            table[i] = tmp
        ret = []

        def DFS(current, layer, ret, L):
            if layer == N:
                L.append(ret)
            elif layer < N:
                queue = table[current]
                for x in queue:
                    DFS(x, layer + 1, ret * 10 + x, L)
            return L
        
        for i in range(1, 10):
            ret += DFS(i, 1, i, [])
        
        
        if N == 1:
            ret += [0]
        return list(set(ret))
                    
                
```

## Content
<p>Return all <strong>non-negative</strong> integers of length <code>N</code> such that the absolute difference between every two consecutive digits is <code>K</code>.</p>

<p>Note that <strong>every</strong> number in the answer <strong>must not</strong> have leading zeros <strong>except</strong> for the number <code>0</code> itself. For example, <code>01</code> has one leading zero and is invalid, but <code>0</code> is valid.</p>

<p>You may return the answer in any order.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-1-1">3</span>, K = <span id="example-input-1-2">7</span>
<strong>Output: </strong><span id="example-output-1">[181,292,707,818,929]</span>
<strong>Explanation: </strong>Note that 070 is not a valid number, because it has leading zeroes.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-2-1">2</span>, K = <span id="example-input-2-2">1</span>
<strong>Output: </strong><span id="example-output-2">[10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]</span></pre>

<p>&nbsp;</p>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= N &lt;= 9</code></li>
	<li><code>0 &lt;= K &lt;= 9</code></li>
</ol>


## Related Problems


## What a(n) Medium problem!
Among **84770** total submissions, **37034** are accepted, with an acceptance rate of 43.7%. <br>

- Likes: 480
- Dislikes: 106


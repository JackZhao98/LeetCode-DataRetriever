# [905] Sort Array By Parity (Easy)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/sort-array-by-parity/) 

[Magic Portal](https://leetcode.com/problems/sort-array-by-parity/)

## My Submission

- Runtime: 160 ms
- Completed time: 2020-08-21 11:45:53

```python3
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i = 0
        j = len(A) - 1
        while i < j:
            if A[i] % 2 == 0:
                i += 1
            elif A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
            else:
                j -= 1

        return A
```

## Content
<p>Given an array <code>A</code> of non-negative integers, return an array consisting of all the even elements of <code>A</code>, followed by all the odd elements of <code>A</code>.</p>

<p>You may return any answer array that satisfies this condition.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[3,1,2,4]</span>
<strong>Output: </strong><span id="example-output-1">[2,4,3,1]</span>
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 5000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 5000</code></li>
</ol>
</div>


## Related Problems


## What a(n) Easy problem!
Among **323584** total submissions, **242434** are accepted, with an acceptance rate of 74.9%. <br>

- Likes: 1206
- Dislikes: 77


# [189] Rotate Array (Easy)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/rotate-array/) 

[Magic Portal](https://leetcode.com/problems/rotate-array/)

## My Submission

- Runtime: 180 ms
- Completed time: 2020-07-29 17:52:38

```python3
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            nums.insert(0, nums.pop(-1))
            k -= 1
```

## Content
<p>Given an array, rotate the array to the right by <em>k</em> steps, where&nbsp;<em>k</em>&nbsp;is non-negative.</p>

<p><strong>Follow up:</strong></p>

<ul>
	<li>Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.</li>
	<li>Could you do it in-place with O(1) extra space?</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5,6,7], k = 3
<strong>Output:</strong> [5,6,7,1,2,3,4]
<strong>Explanation:</strong>
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,-100,3,99], k = 2
<strong>Output:</strong> [3,99,-1,-100]
<strong>Explanation:</strong> 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10^4</code></li>
	<li>It&#39;s guaranteed that <code>nums[i]</code> fits in a 32 bit-signed integer.</li>
	<li><code>k &gt;= 0</code></li>
</ul>


## Related Problems
[Rotate List](https://leetcode.com/problems/rotate-list/) (Medium) <br>
[Reverse Words in a String II](https://leetcode.com/problems/reverse-words-in-a-string-ii/) (Medium) <br>

## What a(n) Easy problem!
Among **1497964** total submissions, **521910** are accepted, with an acceptance rate of 34.8%. <br>

- Likes: 3072
- Dislikes: 838


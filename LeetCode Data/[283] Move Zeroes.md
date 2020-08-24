# [283] Move Zeroes (Easy)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/move-zeroes/)  [![Two%20Pointers_badge](https://img.shields.io/badge/topic-Two%20Pointers-green.svg)](https://leetcode.com/problems/move-zeroes/) 

:+1: 4072 &nbsp; &nbsp; :thumbsdown: 129

---

## My Submission

- Language: python3
- Runtime: 116 ms
- Completed time: 2020-04-04 18:45:03

```python3
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for x in nums:
            if x == 0:
                count += 1
        
        for i in range(count):
            nums.remove(0)
            nums.append(0)
        
```

## Content
<p>Given an array <code>nums</code>, write a function to move all <code>0</code>&#39;s to the end of it while maintaining the relative order of the non-zero elements.</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> <code>[0,1,0,3,12]</code>
<b>Output:</b> <code>[1,3,12,0,0]</code></pre>

<p><b>Note</b>:</p>

<ol>
	<li>You must do this <b>in-place</b> without making a copy of the array.</li>
	<li>Minimize the total number of operations.</li>
</ol>

## Related Problems
[Remove Element](https://leetcode.com/problems/remove-element/) (Easy) <br>

## What a(n) Easy problem!
Among **1532207** total submissions, **887136** are accepted, with an acceptance rate of **57.9%**. <br>

- Likes: 4072
- Dislikes: 129


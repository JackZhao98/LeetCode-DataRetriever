# [268] Missing Number (Easy)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/missing-number/)  [![Math_badge](https://img.shields.io/badge/topic-Math-green.svg)](https://leetcode.com/problems/missing-number/)  [![BitManipulation_badge](https://img.shields.io/badge/topic-BitManipulation-green.svg)](https://leetcode.com/problems/missing-number/) 

:+1: 1928 &nbsp; &nbsp; :thumbsdown: 2214

## My Submission

- Runtime: 148 ms
- Completed time: 2020-07-23 22:26:50

```python3
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) ==1:
            if nums[0] == 1:
                return 0
            return nums[0]+1
        counter = 0
        nums.sort()
        for i in nums:
            if counter != i:
                return counter
            counter += 1
        return nums[-1] + 1
```

## Content
<p>Given an array containing <i>n</i> distinct numbers taken from <code>0, 1, 2, ..., n</code>, find the one that is missing from the array.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> [3,0,1]
<b>Output:</b> 2
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> [9,6,4,2,3,5,7,0,1]
<b>Output:</b> 8
</pre>

<p><b>Note</b>:<br />
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?</p>

## Related Problems
[First Missing Positive](https://leetcode.com/problems/first-missing-positive/) (Hard) <br>
[Single Number](https://leetcode.com/problems/single-number/) (Easy) <br>
[Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) (Medium) <br>
[Couples Holding Hands](https://leetcode.com/problems/couples-holding-hands/) (Hard) <br>

## What a(n) Easy problem!
Among **933088** total submissions, **483475** are accepted, with an acceptance rate of 51.8%. <br>

- Likes: 1928
- Dislikes: 2214


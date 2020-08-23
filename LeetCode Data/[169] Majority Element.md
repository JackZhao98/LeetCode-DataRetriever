# [169] Majority Element (Easy)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/majority-element/)  [![Divide and Conquer_badge](https://img.shields.io/badge/topic-Divide and Conquer-green.svg)](https://leetcode.com/problems/majority-element/)  [![Bit Manipulation_badge](https://img.shields.io/badge/topic-Bit Manipulation-green.svg)](https://leetcode.com/problems/majority-element/) 

:+1: 3453 &nbsp; &nbsp; :thumbsdown: 226

## My Submission

- Runtime: 240 ms
- Completed time: 2020-07-20 21:27:58

```python3
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        same = 0
        prev = nums[0]
        threashold = len(nums)/2
        for n in nums:
            if n == prev:
                same += 1
            else:
                prev = n
                same = 1
            if same > threashold:
                return prev
```

## Content
<p>Given an array of size <i>n</i>, find the majority element. The majority element is the element that appears <b>more than</b> <code>&lfloor; n/2 &rfloor;</code> times.</p>

<p>You may assume that the array is non-empty and the majority element always exist in the array.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [3,2,3]
<strong>Output:</strong> 3</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [2,2,1,1,1,2,2]
<strong>Output:</strong> 2
</pre>


## Related Problems
[Majority Element II](https://leetcode.com/problems/majority-element-ii/) (Medium) <br>
[Check If a Number Is Majority Element in a Sorted Array](https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/) (Easy) <br>

## What a(n) Easy problem!
Among **1159393** total submissions, **681729** are accepted, with an acceptance rate of 58.8%. <br>

- Likes: 3453
- Dislikes: 226


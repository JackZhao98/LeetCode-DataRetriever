# [217] Contains Duplicate (Easy)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/contains-duplicate/)  [![Hash Table_badge](https://img.shields.io/badge/topic-Hash Table-green.svg)](https://leetcode.com/problems/contains-duplicate/) 

:+1: 970 &nbsp; &nbsp; :thumbsdown: 758

## My Submission

- Runtime: 128 ms
- Completed time: 2020-07-23 16:58:35

```python3
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
```

## Content
<p>Given an array of integers, find if the array contains any duplicates.</p>

<p>Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [1,2,3,1]
<strong>Output:</strong> true</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>[1,2,3,4]
<strong>Output:</strong> false</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>[1,1,1,3,3,4,3,2,4,2]
<strong>Output:</strong> true</pre>


## Related Problems
[Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) (Easy) <br>
[Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/) (Medium) <br>

## What a(n) Easy problem!
Among **1076140** total submissions, **603249** are accepted, with an acceptance rate of 56.1%. <br>

- Likes: 970
- Dislikes: 758


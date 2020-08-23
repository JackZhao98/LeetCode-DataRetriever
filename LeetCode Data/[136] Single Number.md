# [136] Single Number (Easy)

[![HashTable_badge](https://img.shields.io/badge/topic-HashTable-green.svg)](https://leetcode.com/problems/single-number/)  [![BitManipulation_badge](https://img.shields.io/badge/topic-BitManipulation-green.svg)](https://leetcode.com/problems/single-number/) 

:+1: 4751 &nbsp; &nbsp; :thumbsdown: 167

## My Submission

- Runtime: 1712 ms
- Completed time: 2020-04-03 12:27:30

```python3
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = []
        for n in nums:
            if n not in ans:
                ans.append(n)
            else:
                ans.remove(n)
        return ans[0]
```

## Content
<p>Given a <strong>non-empty</strong>&nbsp;array of integers, every element appears <em>twice</em> except for one. Find that single one.</p>

<p><strong>Note:</strong></p>

<p>Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [2,2,1]
<strong>Output:</strong> 1
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [4,1,2,1,2]
<strong>Output:</strong> 4
</pre>


## Related Problems
[Single Number II](https://leetcode.com/problems/single-number-ii/) (Medium) <br>
[Single Number III](https://leetcode.com/problems/single-number-iii/) (Medium) <br>
[Missing Number](https://leetcode.com/problems/missing-number/) (Easy) <br>
[Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) (Medium) <br>
[Find the Difference](https://leetcode.com/problems/find-the-difference/) (Easy) <br>

## What a(n) Easy problem!
Among **1414874** total submissions, **927773** are accepted, with an acceptance rate of 65.6%. <br>

- Likes: 4751
- Dislikes: 167


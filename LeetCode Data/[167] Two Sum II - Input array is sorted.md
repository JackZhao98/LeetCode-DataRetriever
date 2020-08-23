# [167] Two Sum II - Input array is sorted (Easy)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)  [![Two Pointers_badge](https://img.shields.io/badge/topic-Two Pointers-green.svg)](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)  [![Binary Search_badge](https://img.shields.io/badge/topic-Binary Search-green.svg)](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) 

:+1: 1781 &nbsp; &nbsp; :thumbsdown: 628

## My Submission

- Runtime: 5212 ms
- Completed time: 2020-07-19 14:11:06

```python3
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = {}
        for c, n in enumerate(numbers, 1):
            for x in l.items():
                if x[1] == n:
                    return [x[0], c]
            l[c] = target - n
            
```

## Content
<p>Given an array of integers that is already <strong><em>sorted in ascending order</em></strong>, find two numbers such that they add up to a specific target number.</p>

<p>The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>Your returned answers (both index1 and index2) are not zero-based.</li>
	<li>You may assume that each input would have <em>exactly</em> one solution and you may not use the <em>same</em> element twice.</li>
</ul>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> numbers = [2,7,11,15], target = 9
<strong>Output:</strong> [1,2]
<strong>Explanation:</strong> The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.</pre>


## Related Problems
[Two Sum](https://leetcode.com/problems/two-sum/) (Easy) <br>
[Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/) (Easy) <br>
[Two Sum Less Than K](https://leetcode.com/problems/two-sum-less-than-k/) (Easy) <br>

## What a(n) Easy problem!
Among **801941** total submissions, **434574** are accepted, with an acceptance rate of 54.2%. <br>

- Likes: 1781
- Dislikes: 628


# [53] Maximum Subarray (Easy)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/maximum-subarray/)  [![Divide and Conquer_badge](https://img.shields.io/badge/topic-Divide and Conquer-green.svg)](https://leetcode.com/problems/maximum-subarray/)  [![Dynamic Programming_badge](https://img.shields.io/badge/topic-Dynamic Programming-green.svg)](https://leetcode.com/problems/maximum-subarray/) 

:+1: 8568 &nbsp; &nbsp; :thumbsdown: 404

## My Submission

- Runtime: 80 ms
- Completed time: 2020-04-03 14:21:53

```python3

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = 0
        current_sum = 0
        allNeg = True
        for x in nums:
            if x >= 0:
                allNeg = False
            current_sum = max(0, current_sum + x)
            print("Current Sum = " + str(current_sum))
            best_sum = max(best_sum, current_sum)
            print("Best Sum = " + str(best_sum))
        if allNeg:
            print("All neg")
            best_sum = nums[0]
            for x in nums:
                print(best_sum)
                print(x)
                best_sum = max(best_sum, x)
        return best_sum
```

## Content
<p>Given an integer array <code>nums</code>, find the contiguous subarray&nbsp;(containing at least one number) which has the largest sum and return its sum.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [-2,1,-3,4,-1,2,1,-5,4],
<strong>Output:</strong> 6
<strong>Explanation:</strong>&nbsp;[4,-1,2,1] has the largest sum = 6.
</pre>

<p><strong>Follow up:</strong></p>

<p>If you have figured out the O(<em>n</em>) solution, try coding another solution using the divide and conquer approach, which is more subtle.</p>


## Related Problems
[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) (Easy) <br>
[Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) (Medium) <br>
[Degree of an Array](https://leetcode.com/problems/degree-of-an-array/) (Easy) <br>
[Longest Turbulent Subarray](https://leetcode.com/problems/longest-turbulent-subarray/) (Medium) <br>

## What a(n) Easy problem!
Among **2338939** total submissions, **1090248** are accepted, with an acceptance rate of 46.6%. <br>

- Likes: 8568
- Dislikes: 404


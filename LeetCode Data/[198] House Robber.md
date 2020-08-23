# [198] House Robber (Easy)

[Magic Portal](https://leetcode.com/problems/house-robber/)

## My Submission

- Runtime: N/A
- Completed time: 2020-07-30 15:42:19

```python3
class Solution:
    def rob(self, nums: List[int]) -> int:
        sumodd = 0
        sumeven = 0
        for i in range(0, len(nums)):
            if i % 2:
                sumodd += nums[i]
            else:
                sumeven += nums[i]
        return max(sumeven, sumodd)
```
## Content

<p>You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and <b>it will automatically contact the police if two adjacent houses were broken into on the same night</b>.</p>

<p>Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight <b>without alerting the police</b>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Rob house 1 (money = 1) and then rob house 3 (money = 3).
&nbsp;            Total amount you can rob = 1 + 3 = 4.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,9,3,1]
<strong>Output:</strong> 12
<strong>Explanation:</strong> Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
&nbsp;            Total amount you can rob = 2 + 9 + 1 = 12.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 400</code></li>
</ul>


## Related Problems

[Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
[House Robber II](https://leetcode.com/problems/house-robber-ii/)
[Paint House](https://leetcode.com/problems/paint-house/)
[Paint Fence](https://leetcode.com/problems/paint-fence/)
[House Robber III](https://leetcode.com/problems/house-robber-iii/)
[Non-negative Integers without Consecutive Ones](https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/)
[Coin Path](https://leetcode.com/problems/coin-path/)
[Delete and Earn](https://leetcode.com/problems/delete-and-earn/)

## What a(n) Easy problem!


Among **1308974** total submissions, **550467** are accepted, with an acceptance rate of 42.1%. <br>

- Likes: 5170
- Dislikes: 159


# [121] Best Time to Buy and Sell Stock (Easy)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)  [![Dynamic Programming_badge](https://img.shields.io/badge/topic-Dynamic Programming-green.svg)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) 

:+1: 5692 &nbsp; &nbsp; :thumbsdown: 247

## My Submission

- Runtime: 60 ms
- Completed time: 2020-06-24 13:04:14

```python3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        local_min = 9999999999
        diff = 0
        for x in prices:
            if x < local_min:
                local_min = x
            
            tmp = (x - local_min)
            if diff < tmp:
                diff = tmp
        return diff
                
```

## Content
<p>Say you have an array for which the <em>i</em><sup>th</sup> element is the price of a given stock on day <em>i</em>.</p>

<p>If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.</p>

<p>Note that you cannot sell a stock before you buy one.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [7,1,5,3,6,4]
<strong>Output:</strong> 5
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
&nbsp;            Not 7-1 = 6, as selling price needs to be larger than buying price.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transaction is done, i.e. max profit = 0.
</pre>


## Related Problems
[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) (Easy) <br>
[Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) (Easy) <br>
[Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) (Hard) <br>
[Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) (Hard) <br>
[Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) (Medium) <br>

## What a(n) Easy problem!
Among **1849826** total submissions, **935022** are accepted, with an acceptance rate of 50.5%. <br>

- Likes: 5692
- Dislikes: 247


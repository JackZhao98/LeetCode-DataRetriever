# [122] Best Time to Buy and Sell Stock II (Easy)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)  [![Greedy_badge](https://img.shields.io/badge/topic-Greedy-green.svg)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) 

:+1: 2752 &nbsp; &nbsp; :thumbsdown: 1790

---

## My Submission

- Language: python3
- Runtime: 68 ms
- Completed time: 2020-06-24 13:34:47

```python3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        for i in range(0, len(prices) - 1):
            ret += max(prices[i+1] - prices[i],0)
        return ret
                
```

## Content
<p>Say you have an array <code>prices</code> for which the <em>i</em><sup>th</sup> element is the price of a given stock on day <em>i</em>.</p>

<p>Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).</p>

<p><strong>Note:</strong> You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [7,1,5,3,6,4]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
&nbsp;            Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [1,2,3,4,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
&nbsp;            Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
&nbsp;            engaging multiple transactions at the same time. You must sell before buying again.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transaction is done, i.e. max profit = 0.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 3 * 10 ^ 4</code></li>
	<li><code>0 &lt;= prices[i]&nbsp;&lt;= 10 ^ 4</code></li>
</ul>


## Related Problems
[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) (Easy) <br>
[Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) (Hard) <br>
[Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) (Hard) <br>
[Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) (Medium) <br>
[Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) (Medium) <br>

## What a(n) Easy problem!
Among **1135919** total submissions, **648729** are accepted, with an acceptance rate of **57.1%**. <br>

- Likes: 2752
- Dislikes: 1790


# [1553] Minimum Number of Days to Eat N Oranges (Hard)

[Magic Portal](https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/)

## My Submission

- Runtime: N/A
- Completed time: 2020-08-15 20:18:40

```python3
class Solution: 
    def minDays(self, n: int) -> int:
        def eat(remain: int) -> int:
            if remain == 1 or remain == 2:
                return 1
            if remain == 3:
                return 2
            if remain % 2 == 0 and remain % 3 == 0:
                return min(1 + eat(remain - 1), 1 + eat(remain - remain // 2), 1 + eat(remain - 2 * (remain // 3)))
            elif remain % 2 == 0:
                return min(1 + eat(remain - 1), 1 + eat(remain - remain // 2))
            elif remain % 3 == 0:
                return min(1 + eat(remain - 1), 1 + eat(remain - 2 * (remain // 3)))
            else:
                return 1 + eat(remain - 1)
        return eat(n)
```
## Content

<p>There are <code>n</code> oranges in the kitchen and you decided to eat some of these oranges every day as follows:</p>

<ul>
	<li>Eat one orange.</li>
	<li>If the number of remaining oranges (<code>n</code>) is divisible by 2 then you can eat&nbsp; n/2 oranges.</li>
	<li>If the number of remaining oranges (<code>n</code>) is divisible by 3&nbsp;then you can eat&nbsp; 2*(n/3)&nbsp;oranges.</li>
</ul>

<p>You can only choose one of the actions per day.</p>

<p>Return the minimum number of days to eat <code>n</code> oranges.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 4
<strong>Explanation:</strong> You have 10 oranges.
Day 1: Eat 1 orange,  10 - 1 = 9.  
Day 2: Eat 6 oranges, 9 - 2*(9/3) = 9 - 6 = 3. (Since 9 is divisible by 3)
Day 3: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1. 
Day 4: Eat the last orange  1 - 1  = 0.
You need at least 4 days to eat the 10 oranges.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 6
<strong>Output:</strong> 3
<strong>Explanation:</strong> You have 6 oranges.
Day 1: Eat 3 oranges, 6 - 6/2 = 6 - 3 = 3. (Since 6 is divisible by 2).
Day 2: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1. (Since 3 is divisible by 3)
Day 3: Eat the last orange  1 - 1  = 0.
You need at least 3 days to eat the 6 oranges.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 1
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> n = 56
<strong>Output:</strong> 6
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2*10^9</code></li>
</ul>

## Related Problems



## What a(n) Hard problem!


Among **29821** total submissions, **7972** are accepted, with an acceptance rate of 26.7%. <br>

- Likes: 231
- Dislikes: 24


# [1550] Three Consecutive Odds (Easy)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/three-consecutive-odds/) 

[Magic Portal](https://leetcode.com/problems/three-consecutive-odds/)

## My Submission

- Runtime: 44 ms
- Completed time: 2020-08-15 19:32:14

```python3
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        counter = 0
        for x in arr:
            if x % 2:
                counter += 1
                if counter == 3:
                    return True
            else:
                counter = 0
        return False
```

## Content
Given an integer array <code>arr</code>, return <code>true</code>&nbsp;if there are three consecutive odd numbers in the array. Otherwise, return&nbsp;<code>false</code>.
<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [2,6,4,1]
<strong>Output:</strong> false
<b>Explanation:</b> There are no three consecutive odds.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2,34,3,4,5,7,23,12]
<strong>Output:</strong> true
<b>Explanation:</b> [5,7,23] are three consecutive odds.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 1000</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 1000</code></li>
</ul>


## Related Problems


## What a(n) Easy problem!
Among **21007** total submissions, **14223** are accepted, with an acceptance rate of 67.7%. <br>

- Likes: 69
- Dislikes: 12


# [1103] Distribute Candies to People (Easy)

[![Math_badge](https://img.shields.io/badge/topic-Math-green.svg)](https://leetcode.com/problems/distribute-candies-to-people/) 

:+1: 407 &nbsp; &nbsp; :thumbsdown: 115

---

## My Submission

- Language: python3
- Runtime: 40 ms
- Completed time: 2020-08-17 16:05:46

```python3
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        r = 0
        ret = [0]*num_people
        while candies > 0:
            for c in range(num_people):
                tmp = min(r * num_people + c + 1, candies)
                ret[c] += tmp
                candies -= tmp
            r += 1
        return ret
        
```

## Content
<p>We distribute some&nbsp;number of <code>candies</code>, to a row of <strong><code>n =&nbsp;num_people</code></strong>&nbsp;people in the following way:</p>

<p>We then give 1 candy to the first person, 2 candies to the second person, and so on until we give <code>n</code>&nbsp;candies to the last person.</p>

<p>Then, we go back to the start of the row, giving <code>n&nbsp;+ 1</code> candies to the first person, <code>n&nbsp;+ 2</code> candies to the second person, and so on until we give <code>2 * n</code>&nbsp;candies to the last person.</p>

<p>This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run out of candies.&nbsp; The last person will receive all of our remaining candies (not necessarily one more than the previous gift).</p>

<p>Return an array (of length <code>num_people</code>&nbsp;and sum <code>candies</code>) that represents the final distribution of candies.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> candies = 7, num_people = 4
<strong>Output:</strong> [1,2,3,1]
<strong>Explanation:</strong>
On the first turn, ans[0] += 1, and the array is [1,0,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0,0].
On the third turn, ans[2] += 3, and the array is [1,2,3,0].
On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> candies = 10, num_people = 3
<strong>Output:</strong> [5,2,3]
<strong>Explanation: </strong>
On the first turn, ans[0] += 1, and the array is [1,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0].
On the third turn, ans[2] += 3, and the array is [1,2,3].
On the fourth turn, ans[0] += 4, and the final array is [5,2,3].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>1 &lt;= candies &lt;= 10^9</li>
	<li>1 &lt;= num_people &lt;= 1000</li>
</ul>


## Related Problems


## What a(n) Easy problem!
Among **77857** total submissions, **49570** are accepted, with an acceptance rate of **63.7%**. <br>

- Likes: 407
- Dislikes: 115


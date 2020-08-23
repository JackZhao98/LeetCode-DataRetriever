# [202] Happy Number (Easy)

[![Hash Table_badge](https://img.shields.io/badge/topic-Hash Table-green.svg)](https://leetcode.com/problems/happy-number/)  [![Math_badge](https://img.shields.io/badge/topic-Math-green.svg)](https://leetcode.com/problems/happy-number/) 

[Magic Portal](https://leetcode.com/problems/happy-number/)

## My Submission

- Runtime: 24 ms
- Completed time: 2020-04-03 12:59:03

```python3
class Solution:
    def isHappy(self, n: int) -> bool:
        while n >= 10:
            result = 0
            num = str(n)
            for c in num:
                result += int(c)*int(c)
            n = result
        return n == 1 or n == 7
```

## Content
<p>Write an algorithm to determine if a number <code>n</code> is &quot;happy&quot;.</p>

<p>A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it <strong>loops endlessly in a cycle</strong> which does not include 1. Those numbers for which this process <strong>ends in 1</strong> are happy numbers.</p>

<p>Return True if <code>n</code> is a happy number, and False if not.</p>

<p><strong>Example:&nbsp;</strong></p>

<pre>
<strong>Input:</strong> 19
<strong>Output:</strong> true
<strong>Explanation: 
</strong>1<sup>2</sup> + 9<sup>2</sup> = 82
8<sup>2</sup> + 2<sup>2</sup> = 68
6<sup>2</sup> + 8<sup>2</sup> = 100
1<sup>2</sup> + 0<sup>2</sup> + 0<sup>2</sup> = 1
</pre>


## Related Problems
[Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) (Easy) <br>
[Add Digits](https://leetcode.com/problems/add-digits/) (Easy) <br>
[Ugly Number](https://leetcode.com/problems/ugly-number/) (Easy) <br>

## What a(n) Easy problem!
Among **1054027** total submissions, **532219** are accepted, with an acceptance rate of 50.5%. <br>

- Likes: 2307
- Dislikes: 442


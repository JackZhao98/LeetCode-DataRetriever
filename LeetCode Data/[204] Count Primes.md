# [204] Count Primes (Easy)

[Magic Portal](https://leetcode.com/problems/count-primes/)

## My Submission

- Runtime: N/A
- Completed time: 2020-07-30 18:30:25

```python3
class Solution:
    def isPrime(self, num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    
    def countPrimes(self, n: int) -> int:
        counter = 0
        for i in range(2, n+1):
            if self.isPrime(i):
                counter += 1
        return counter
```
## Content

<p>Count the number of prime numbers less than a non-negative number, <b><i>n</i></b>.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 10
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
</pre>


## Related Problems

[Ugly Number](https://leetcode.com/problems/ugly-number/)
[Ugly Number II](https://leetcode.com/problems/ugly-number-ii/)
[Perfect Squares](https://leetcode.com/problems/perfect-squares/)

## What a(n) Easy problem!


Among **1192335** total submissions, **375835** are accepted, with an acceptance rate of 31.5%. <br>

- Likes: 2164
- Dislikes: 632


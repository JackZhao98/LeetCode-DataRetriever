# [7] Reverse Integer (Easy)

[![Math_badge](https://img.shields.io/badge/topic-Math-green.svg)](https://leetcode.com/problems/reverse-integer/) 

:+1: 3590 &nbsp; &nbsp; :thumbsdown: 5639

## My Submission

- Runtime: 0 ms
- Completed time: 2019-06-27 21:33:36

```cpp
class Solution {

    
public:
    int reverse(int x) {
        int result = 0;
        bool pos = (x >= 0);
        if (!pos) {
            if (x == INT_MIN)
                return 0;
            x *= -1;
        }
        while (x > 0) {
            if (0.1*INT_MAX < result)
                return 0;
            result *= 10;
            result += x%10;
            x /= 10;
        }
        if (!pos)
            result *= -1;
        return result;
    }
};
```

## Content
<p>Given a 32-bit signed integer, reverse digits of an integer.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 123
<strong>Output:</strong> 321
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> -123
<strong>Output:</strong> -321
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> 120
<strong>Output:</strong> 21
</pre>

<p><strong>Note:</strong><br />
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [&minus;2<sup>31</sup>,&nbsp; 2<sup>31&nbsp;</sup>&minus; 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.</p>


## Related Problems
[String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/) (Medium) <br>
[Reverse Bits](https://leetcode.com/problems/reverse-bits/) (Easy) <br>

## What a(n) Easy problem!
Among **4573625** total submissions, **1180499** are accepted, with an acceptance rate of 25.8%. <br>

- Likes: 3590
- Dislikes: 5639


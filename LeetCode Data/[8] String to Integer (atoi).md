# [8] String to Integer (atoi) (Medium)

[![Math_badge](https://img.shields.io/badge/topic-Math-green.svg)](https://leetcode.com/problems/string-to-integer-atoi/)  [![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/string-to-integer-atoi/) 

:+1: 1688 &nbsp; &nbsp; :thumbsdown: 9724

---

## My Submission

- Language: cpp
- Runtime: 8 ms
- Completed time: 2019-06-27 20:59:17

```cpp
class Solution {
public:
    int myAtoi(string str) {
        int result = 0;
        int negative = 1;
        for (int i = 0; i < str.length(); ++ i) {
            if (str[i] == ' ') {
                continue;
            }
            if (str[i] == '+' || str[i] == '-' || isdigit(str[i])) {
                if (str[i] == '+') {
                    if (i+1 != str.length()) {
                    if (!isdigit(str[i+1]))
                        break;
                }
                    continue;
                }
                if (str[i] == '-') {
                    negative = -1;
                    if (i+1 != str.length()) {
                    if (!isdigit(str[i+1]))
                        break;
                }
                    continue;
                }
                if (result < double(0.1*INT_MAX))
                    result *= 10;
                else {
                    if (negative > 0)
                        return INT_MAX;
                    else 
                        return INT_MIN;
                }
                if ((INT_MAX - (str[i] - '0')) >= result) 
                    result += (str[i] - '0');
                else {
                    if (negative > 0)
                        return INT_MAX;
                    else 
                        return INT_MIN;
                }
                if (i+1 != str.length()) {
                    if (!isdigit(str[i+1]))
                        break;
                }
            }
            else 
                break;
        }
        
        return negative*result;
    }
};
```

## Content
<p>Implement <code><span>atoi</span></code> which&nbsp;converts a string to an integer.</p>

<p>The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.</p>

<p>The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.</p>

<p>If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.</p>

<p>If no valid conversion could be performed, a zero value is returned.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>Only the space character <code>&#39; &#39;</code> is considered as whitespace character.</li>
	<li>Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [&minus;2<sup>31</sup>,&nbsp; 2<sup>31&nbsp;</sup>&minus; 1]. If the numerical value is out of the range of representable values, INT_MAX (2<sup>31&nbsp;</sup>&minus; 1) or INT_MIN (&minus;2<sup>31</sup>) is returned.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> &quot;42&quot;
<strong>Output:</strong> 42
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> &quot;   -42&quot;
<strong>Output:</strong> -42
<strong>Explanation:</strong> The first non-whitespace character is &#39;-&#39;, which is the minus sign.
&nbsp;            Then take as many numerical digits as possible, which gets 42.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> &quot;4193 with words&quot;
<strong>Output:</strong> 4193
<strong>Explanation:</strong> Conversion stops at digit &#39;3&#39; as the next character is not a numerical digit.
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> &quot;words and 987&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> The first non-whitespace character is &#39;w&#39;, which is not a numerical 
&nbsp;            digit or a +/- sign. Therefore no valid conversion could be performed.</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong> &quot;-91283472332&quot;
<strong>Output:</strong> -2147483648
<strong>Explanation:</strong> The number &quot;-91283472332&quot; is out of the range of a 32-bit signed integer.
&nbsp;            Thefore INT_MIN (&minus;2<sup>31</sup>) is returned.</pre>


## Related Problems
[Reverse Integer](https://leetcode.com/problems/reverse-integer/) (Easy) <br>
[Valid Number](https://leetcode.com/problems/valid-number/) (Hard) <br>

## What a(n) Medium problem!
Among **3862541** total submissions, **594431** are accepted, with an acceptance rate of **15.4%**. <br>

- Likes: 1688
- Dislikes: 9724


# [793] Preimage Size of Factorial Zeroes Function (Hard)

[![Binary Search_badge](https://img.shields.io/badge/topic-Binary Search-green.svg)](https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/) 

:+1: 175 &nbsp; &nbsp; :thumbsdown: 55

## My Submission

- Runtime: 4 ms
- Completed time: 2019-08-31 07:03:11

```cpp
class Solution {
public:
    int preimageSizeFZF(int K) {
        if (K < 5) return 5;
        int base = 1;
        while (base * 5 + 1 <= K) {
            base = base * 5 + 1;
        }
        if (K / base == 5) return 0;
        return preimageSizeFZF(K % base);
    }
};
```

## Content
<p>Let <code>f(x)</code> be the number of zeroes at the end of <code>x!</code>. (Recall that <code>x! = 1 * 2 * 3 * ... * x</code>, and by convention, <code>0! = 1</code>.)</p>

<p>For example, <code>f(3) = 0</code> because 3! = 6 has no zeroes at the end, while <code>f(11) = 2</code> because 11! = 39916800 has 2 zeroes at the end. Given <code>K</code>, find how many non-negative integers <code>x</code> have the property that <code>f(x) = K</code>.</p>

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> K = 0
<strong>Output:</strong> 5
<strong>Explanation:</strong> 0!, 1!, 2!, 3!, and 4! end with K = 0 zeroes.

<strong>Example 2:</strong>
<strong>Input:</strong> K = 5
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is no x such that x! ends in K = 5 zeroes.
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li><code>K</code> will be an integer in the range <code>[0, 10^9]</code>.</li>
</ul>


## Related Problems
[Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/) (Easy) <br>

## What a(n) Hard problem!
Among **20324** total submissions, **8181** are accepted, with an acceptance rate of 40.3%. <br>

- Likes: 175
- Dislikes: 55


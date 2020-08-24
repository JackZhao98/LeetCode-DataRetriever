# [342] Power of Four (Easy)

[![Bit%20Manipulation_badge](https://img.shields.io/badge/topic-Bit%20Manipulation-green.svg)](https://leetcode.com/problems/power-of-four/) 

:+1: 680 &nbsp; &nbsp; :thumbsdown: 235

---

## My Submission

- Language: cpp
- Runtime: 4 ms
- Completed time: 2020-08-04 13:42:32

```cpp
class Solution {
public:
    bool isPowerOfFour(int num) {
        int mask = 1;
        while (mask < num && (mask != 0x40000000)) {
            cout << "mask" << mask << endl;
            mask = mask << 2;
        }

        cout << mask;
        return !(mask ^ num);
    }
};
```

## Content
<p>Given an integer (signed 32 bits), write a function to check whether it is a power of 4.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">16</span>
<strong>Output: </strong><span id="example-output-1">true</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">5</span>
<strong>Output: </strong><span id="example-output-2">false</span></pre>
</div>

<p><b>Follow up</b>: Could you solve it without loops/recursion?</p>

## Related Problems
[Power of Two](https://leetcode.com/problems/power-of-two/) (Easy) <br>
[Power of Three](https://leetcode.com/problems/power-of-three/) (Easy) <br>

## What a(n) Easy problem!
Among **488059** total submissions, **202290** are accepted, with an acceptance rate of **41.4%**. <br>

- Likes: 680
- Dislikes: 235


# [771] Jewels and Stones (Easy)

[![Hash Table_badge](https://img.shields.io/badge/topic-Hash Table-green.svg)](https://leetcode.com/problems/jewels-and-stones/) 

[Magic Portal](https://leetcode.com/problems/jewels-and-stones/)

## My Submission

- Runtime: 4 ms
- Completed time: 2019-07-26 00:25:16

```cpp
class Solution {
public:
    int numJewelsInStones(string J, string S) {
        int lenJ = J.size();
        int lenS = S.size();
        int count = 0;
        int indexS = 0, indexJ = 0;
        while (indexS < lenS) {
            while (indexJ < lenJ) {
                if (!(S[indexS] - J[indexJ ++]))
                    ++ count;
            }
            indexJ = 0;
            ++ indexS;
        }
        return count;
    }
    
};
```

## Content
<p>You&#39;re given strings <code>J</code> representing the types of stones that are jewels, and <code>S</code> representing the stones you have.&nbsp; Each character in <code>S</code> is a type of stone you have.&nbsp; You want to know how many of the stones you have are also jewels.</p>

<p>The letters in <code>J</code> are guaranteed distinct, and all characters in <code>J</code> and <code>S</code> are letters. Letters are case sensitive, so <code>&quot;a&quot;</code> is considered a different type of stone from <code>&quot;A&quot;</code>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> J = &quot;aA&quot;, S = &quot;aAAbbbb&quot;
<strong>Output:</strong> 3
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> J = &quot;z&quot;, S = &quot;ZZ&quot;
<strong>Output:</strong> 0
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li><code>S</code> and <code>J</code> will consist of letters and have length at most 50.</li>
	<li>The characters in <code>J</code> are distinct.</li>
</ul>


## Related Problems


## What a(n) Easy problem!
Among **616856** total submissions, **532979** are accepted, with an acceptance rate of 86.4%. <br>

- Likes: 2185
- Dislikes: 372


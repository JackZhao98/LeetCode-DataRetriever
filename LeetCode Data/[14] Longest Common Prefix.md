# [14] Longest Common Prefix (Easy)

[![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/longest-common-prefix/) 

:+1: 2825 &nbsp; &nbsp; :thumbsdown: 1931

---

## My Submission

- Language: cpp
- Runtime: 8 ms
- Completed time: 2019-09-03 00:59:03

```cpp
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 0)
            return "";
        
        int min = INT_MAX;
        
        for (int i = 0; i < strs.size(); ++ i) {
            if (min > strs[i].length())
                min = strs[i].length();
        }
        
        string res = "";
        for (int j = 0; j < min; ++ j) {
            char c = strs[0][j];
            
            for (int n = 0; n < strs.size(); ++ n) {
                if (strs[n][j] != c)
                    return res;
            }
            
            res += c;
            
        }
        return res;
        
    }
};
```

## Content
<p>Write a function to find the longest common prefix string amongst an array of strings.</p>

<p>If there is no common prefix, return an empty string <code>&quot;&quot;</code>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[&quot;flower&quot;,&quot;flow&quot;,&quot;flight&quot;]
<strong>Output:</strong> &quot;fl&quot;
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>[&quot;dog&quot;,&quot;racecar&quot;,&quot;car&quot;]
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> There is no common prefix among the input strings.
</pre>

<p><strong>Note:</strong></p>

<p>All given inputs are in lowercase letters <code>a-z</code>.</p>


## Related Problems


## What a(n) Easy problem!
Among **2244271** total submissions, **796305** are accepted, with an acceptance rate of **35.5%**. <br>

- Likes: 2825
- Dislikes: 1931


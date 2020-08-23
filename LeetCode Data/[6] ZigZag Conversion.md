# [6] ZigZag Conversion (Medium)

[![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/zigzag-conversion/) 

:+1: 1783 &nbsp; &nbsp; :thumbsdown: 4800

## My Submission

- Runtime: 8 ms
- Completed time: 2019-09-05 00:19:04

```cpp
class Solution {
public:
    string convert(string s, int numRows) {
        if (s == "" || numRows == 1)
            return s;
        
        string res;
        vector<string> str(numRows);
        int rowCount = 0;
        bool descend = false;
        
        for (int i = 0; i < s.size(); ++ i) {
            str[rowCount] += s[i];
            
            if (rowCount <= 0 || rowCount >= (numRows - 1))
                descend = !descend;
            
            (descend)? rowCount ++ : rowCount --;
        }
        
        for (int i = 0 ; i < numRows; ++ i) {
            res += str[i];
        }
        
        return res;
    }
        
    
};
```

## Content
<p>The string <code>&quot;PAYPALISHIRING&quot;</code> is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)</p>

<pre>
P   A   H   N
A P L S I I G
Y   I   R
</pre>

<p>And then read line by line: <code>&quot;PAHNAPLSIIGYIR&quot;</code></p>

<p>Write the code that will take a string and make this conversion given a number of rows:</p>

<pre>
string convert(string s, int numRows);</pre>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;PAYPALISHIRING&quot;, numRows = 3
<strong>Output:</strong> &quot;PAHNAPLSIIGYIR&quot;
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;PAYPALISHIRING&quot;, numRows =&nbsp;4
<strong>Output:</strong>&nbsp;&quot;PINALSIGYAHRPI&quot;
<strong>Explanation:</strong>

P     I    N
A   L S  I G
Y A   H R
P     I</pre>


## Related Problems


## What a(n) Medium problem!
Among **1312337** total submissions, **478109** are accepted, with an acceptance rate of 36.4%. <br>

- Likes: 1783
- Dislikes: 4800


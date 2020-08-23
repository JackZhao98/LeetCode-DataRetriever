# [709] To Lower Case (Easy)

[![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/to-lower-case/) 

:+1: 510 &nbsp; &nbsp; :thumbsdown: 1607

## My Submission

- Runtime: 4 ms
- Completed time: 2019-07-24 17:21:08

```cpp
class Solution {
public:
    string toLowerCase(string str) {
        string result = "";
        int len = str.size();
        for (int i = 0; i < len; ++ i) {
            if ('a' <= str[i] && str[i] <= 'z') {
                result += str[i];
                continue;
            }
            if ('A' <= str[i] && str[i] <= 'Z') {
                char c = str[i] - 'A' + 'a';
                result += c;
                continue;
            }
            result += str[i];
        }
        return result;
    }
};
```

## Content
<p>Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">&quot;Hello&quot;</span>
<strong>Output: </strong><span id="example-output-1">&quot;hello&quot;</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">&quot;here&quot;</span>
<strong>Output: </strong><span id="example-output-2">&quot;here&quot;</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">&quot;LOVELY&quot;</span>
<strong>Output: </strong><span id="example-output-3">&quot;lovely&quot;</span>
</pre>
</div>
</div>
</div>

## Related Problems


## What a(n) Easy problem!
Among **275756** total submissions, **218867** are accepted, with an acceptance rate of 79.4%. <br>

- Likes: 510
- Dislikes: 1607


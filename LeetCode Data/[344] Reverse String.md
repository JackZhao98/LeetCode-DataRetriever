# [344] Reverse String (Easy)

[![Two Pointers_badge](https://img.shields.io/badge/topic-Two Pointers-green.svg)](https://leetcode.com/problems/reverse-string/)  [![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/reverse-string/) 

[Magic Portal](https://leetcode.com/problems/reverse-string/)

## My Submission

- Runtime: 40 ms
- Completed time: 2019-07-26 00:10:19

```cpp
class Solution {
public:
    void reverseString(vector<char>& s) {
        int len = s.size()/2;
        int j = s.size()-1;
        for (int i = 0; i < len; ++i) {
            swap(s[i], s[j--]);
        }
    }
    
    void swap(char& a, char& b) {
        char temp = b;
        b = a;
        a = temp;
    }
};
```

## Content
<p>Write a function that reverses a string. The input string is given as an array of characters <code>char[]</code>.</p>

<p>Do not allocate extra space for another array, you must do this by <strong>modifying the input array&nbsp;<a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a></strong> with O(1) extra memory.</p>

<p>You may assume all the characters consist of <a href="https://en.wikipedia.org/wiki/ASCII#Printable_characters" target="_blank">printable ascii characters</a>.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[&quot;h&quot;,&quot;e&quot;,&quot;l&quot;,&quot;l&quot;,&quot;o&quot;]</span>
<strong>Output: </strong><span id="example-output-1">[&quot;o&quot;,&quot;l&quot;,&quot;l&quot;,&quot;e&quot;,&quot;h&quot;]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[&quot;H&quot;,&quot;a&quot;,&quot;n&quot;,&quot;n&quot;,&quot;a&quot;,&quot;h&quot;]</span>
<strong>Output: </strong><span id="example-output-2">[&quot;h&quot;,&quot;a&quot;,&quot;n&quot;,&quot;n&quot;,&quot;a&quot;,&quot;H&quot;]</span>
</pre>
</div>
</div>


## Related Problems
[Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/) (Easy) <br>
[Reverse String II](https://leetcode.com/problems/reverse-string-ii/) (Easy) <br>

## What a(n) Easy problem!
Among **1166152** total submissions, **800799** are accepted, with an acceptance rate of 68.7%. <br>

- Likes: 1560
- Dislikes: 708


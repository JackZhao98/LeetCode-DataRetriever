# [832] Flipping an Image (Easy)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/flipping-an-image/) 

:+1: 933 &nbsp; &nbsp; :thumbsdown: 150

## My Submission

- Runtime: 12 ms
- Completed time: 2019-07-24 18:44:01

```cpp

auto speed=[]()
{
    std::ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return nullptr;
}();

class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        vector<vector<int>> B = A;
        for (int i = 0; i < B.size(); ++ i) {
            flipAndInvert(B[i]);
        }
        return B;
    }
    
    void swap(int& a, int& b) {
        int temp = b;
        b = a;
        a = temp;
    }
    
    void reverse(vector<int>& reverseThis) {
        int i = 0, j = reverseThis.size() -1;
        while (i < j) {
            swap(reverseThis[i++], reverseThis[j--]);
        }
    }
    
    void flipAndInvert(vector<int>& flipThis) {
        reverse(flipThis);
        for (int i = 0; i < flipThis.size(); ++ i) {
            if (flipThis.at(i)) {
                flipThis[i] = 0;
            } else {
                flipThis[i] = 1;
            }
        }
    }
};
```

## Content
<p>Given a binary matrix <code>A</code>, we want to flip the image horizontally, then invert it, and return the resulting image.</p>

<p>To flip an image horizontally means that each row of the image is reversed.&nbsp; For example, flipping&nbsp;<code>[1, 1, 0]</code>&nbsp;horizontally results in&nbsp;<code>[0, 1, 1]</code>.</p>

<p>To invert an image means&nbsp;that each <code>0</code> is replaced by <code>1</code>, and each <code>1</code> is replaced by <code>0</code>.&nbsp;For example, inverting&nbsp;<code>[0, 1, 1]</code>&nbsp;results in&nbsp;<code>[1, 0, 0]</code>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[[1,1,0],[1,0,1],[0,0,0]]
<strong>Output: </strong>[[1,0,0],[0,1,0],[1,1,1]]
<strong>Explanation:</strong> First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
<strong>Output: </strong>[[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
<strong>Explanation:</strong> First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
</pre>

<p><strong>Notes:</strong></p>

<ul>
	<li><code>1 &lt;= A.length = A[0].length &lt;= 20</code></li>
	<li><code>0 &lt;= A[i][j]<font face="sans-serif, Arial, Verdana, Trebuchet MS">&nbsp;&lt;=&nbsp;</font>1</code></li>
</ul>


## Related Problems


## What a(n) Easy problem!
Among **234166** total submissions, **178719** are accepted, with an acceptance rate of 76.3%. <br>

- Likes: 933
- Dislikes: 150


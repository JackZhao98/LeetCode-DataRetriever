# [665] Non-decreasing Array (Easy)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/non-decreasing-array/) 

:+1: 1982 &nbsp; &nbsp; :thumbsdown: 477

## My Submission

- Runtime: 28 ms
- Completed time: 2019-07-23 19:28:57

```cpp
class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        bool changed = false;
        for (int i = 1; i < nums.size(); ++ i) {
            // 出现Non-decreasing
            if (nums[i] < nums[i-1]) {
                if (changed)
                    return false;
                
                if (i == 1 || nums[i] >= nums[i - 2]) 
                    nums[i - 1] = nums[i];
                else
                    nums[i] = nums[i - 1];
                
                changed = true;
            }
            
        }
        return true;
    }
};
```

## Content
<p>Given an array <code>nums</code> with <code>n</code> integers, your task is to check if it could become non-decreasing by modifying <b>at most</b> <code>1</code> element.</p>

<p>We define an array is non-decreasing if <code>nums[i] &lt;= nums</code><code>[i + 1]</code> holds for every <code>i</code>&nbsp;(0-based) such that <code>(0&nbsp;&lt;= i &lt;= n - 2)</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,2,3]
<strong>Output:</strong> true
<strong>Explanation:</strong> You could modify the first <code>4</code> to <code>1</code> to get a non-decreasing array.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,2,1]
<strong>Output:</strong> false
<strong>Explanation:</strong> You can&#39;t get a non-decreasing array by modify at most one element.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10 ^ 4</code></li>
	<li><code>- 10 ^ 5&nbsp;&lt;= nums[i] &lt;= 10 ^ 5</code></li>
</ul>


## Related Problems


## What a(n) Easy problem!
Among **510152** total submissions, **99697** are accepted, with an acceptance rate of 19.5%. <br>

- Likes: 1982
- Dislikes: 477


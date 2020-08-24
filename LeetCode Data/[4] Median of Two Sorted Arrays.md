# [4] Median of Two Sorted Arrays (Hard)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/median-of-two-sorted-arrays/)  [![Binary%20Search_badge](https://img.shields.io/badge/topic-Binary%20Search-green.svg)](https://leetcode.com/problems/median-of-two-sorted-arrays/)  [![Divide%20and%20Conquer_badge](https://img.shields.io/badge/topic-Divide%20and%20Conquer-green.svg)](https://leetcode.com/problems/median-of-two-sorted-arrays/) 

:+1: 7617 &nbsp; &nbsp; :thumbsdown: 1200

---

## My Submission

- Language: cpp
- Runtime: 24 ms
- Completed time: 2019-06-27 20:35:16

```cpp
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> sorted;
        while (!nums1.empty() || !nums2.empty()) {
            if (nums1.size() > 0 && nums2.size() > 0) {
                sorted.push_back((nums1.back() > nums2.back())? nums1.back():nums2.back());
                (nums1.back() > nums2.back())? nums1.pop_back():nums2.pop_back();
                
                         
            }
            else if (nums1.size() > 0) {
                sorted.push_back(nums1.back());
                nums1.pop_back();
            }
            else if (nums2.size() > 0) {
                sorted.push_back(nums2.back());
                nums2.pop_back();
            }
        }
        double median = 0;
        if (sorted.size() % 2 == 1) {
            median = sorted[sorted.size()/2];
        } else {
            median = 0.5 * (sorted[sorted.size()/2 - 1] + sorted[sorted.size()/2]);
        }
        return median;
    }
};
```

## Content
<p>Given two sorted arrays <code>nums1</code> and <code>nums2</code> of size <code>m</code> and <code>n</code> respectively.</p>

<p>Return <strong>the median</strong> of the two sorted arrays.</p>

<p><strong>Follow up:</strong> The overall run time complexity should be <code>O(log (m+n))</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,3], nums2 = [2]
<strong>Output:</strong> 2.00000
<strong>Explanation:</strong> merged array = [1,2,3] and median is 2.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2], nums2 = [3,4]
<strong>Output:</strong> 2.50000
<strong>Explanation:</strong> merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [0,0], nums2 = [0,0]
<strong>Output:</strong> 0.00000
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [], nums2 = [1]
<strong>Output:</strong> 1.00000
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [2], nums2 = []
<strong>Output:</strong> 2.00000
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>nums1,length == m</code></li>
	<li><code>nums2,length == n</code></li>
	<li><code>0 &lt;= m &lt;= 1000</code></li>
	<li><code>0 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= m + n &lt;= 2000</code></li>
</ul>


## Related Problems


## What a(n) Hard problem!
Among **2434211** total submissions, **722810** are accepted, with an acceptance rate of **29.7%**. <br>

- Likes: 7617
- Dislikes: 1200


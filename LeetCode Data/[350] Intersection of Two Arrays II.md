# [350] Intersection of Two Arrays II (Easy)

[![HashTable_badge](https://img.shields.io/badge/topic-HashTable-green.svg)](https://leetcode.com/problems/intersection-of-two-arrays-ii/)  [![TwoPointers_badge](https://img.shields.io/badge/topic-TwoPointers-green.svg)](https://leetcode.com/problems/intersection-of-two-arrays-ii/)  [![BinarySearch_badge](https://img.shields.io/badge/topic-BinarySearch-green.svg)](https://leetcode.com/problems/intersection-of-two-arrays-ii/)  [![Sort_badge](https://img.shields.io/badge/topic-Sort-green.svg)](https://leetcode.com/problems/intersection-of-two-arrays-ii/) 

:+1: 1501 &nbsp; &nbsp; :thumbsdown: 428

## My Submission

- Runtime: 80 ms
- Completed time: 2020-07-24 21:18:17

```python3
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = []
        for x in nums1:
            if x in nums2:
                ret.append(x)
                nums2.remove(x)
        return ret
```

## Content
<p>Given two arrays, write a function to compute their intersection.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>nums1 = <span id="example-input-1-1">[1,2,2,1]</span>, nums2 = <span id="example-input-1-2">[2,2]</span>
<strong>Output: </strong><span id="example-output-1">[2,2]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>nums1 = <span id="example-input-2-1">[4,9,5]</span>, nums2 = <span id="example-input-2-2">[9,4,9,8,4]</span>
<strong>Output: </strong><span id="example-output-2">[4,9]</span></pre>
</div>

<p><b>Note:</b></p>

<ul>
	<li>Each element in the result should appear as many times as it shows in both arrays.</li>
	<li>The result can be in any order.</li>
</ul>

<p><b>Follow up:</b></p>

<ul>
	<li>What if the given array is already sorted? How would you optimize your algorithm?</li>
	<li>What if <i>nums1</i>&#39;s size is small compared to <i>nums2</i>&#39;s size? Which algorithm is better?</li>
	<li>What if elements of <i>nums2</i> are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?</li>
</ul>


## Related Problems
[Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/) (Easy) <br>
[Find Common Characters](https://leetcode.com/problems/find-common-characters/) (Easy) <br>

## What a(n) Easy problem!
Among **733395** total submissions, **377148** are accepted, with an acceptance rate of 51.4%. <br>

- Likes: 1501
- Dislikes: 428


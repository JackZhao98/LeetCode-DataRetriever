# [435] Non-overlapping Intervals (Medium)

[![Greedy_badge](https://img.shields.io/badge/topic-Greedy-green.svg)](https://leetcode.com/problems/non-overlapping-intervals/) 

:+1: 1424 &nbsp; &nbsp; :thumbsdown: 43

## My Submission

- Runtime: 76 ms
- Completed time: 2020-08-15 16:38:25

```python3
class Solution:
    
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key = lambda a: a[1])
        end = intervals[0][1]
        ret = 1
        for x in intervals:
            if end <= x[0]:
                ret += 1
                end = x[1]
            
        return len(intervals) - ret
```

## Content
<p>Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.</p>

<ol>
</ol>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> [[1,2],[2,3],[3,4],[1,3]]
<b>Output:</b> 1
<b>Explanation:</b> [1,3] can be removed and the rest of intervals are non-overlapping.
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> [[1,2],[1,2],[1,2]]
<b>Output:</b> 2
<b>Explanation:</b> You need to remove two [1,2] to make the rest of intervals non-overlapping.
</pre>

<p><b>Example 3:</b></p>

<pre>
<b>Input:</b> [[1,2],[2,3]]
<b>Output:</b> 0
<b>Explanation:</b> You don&#39;t need to remove any of the intervals since they&#39;re already non-overlapping.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>You may assume the interval&#39;s end point is always bigger than its start point.</li>
	<li>Intervals like [1,2] and [2,3] have borders &quot;touching&quot; but they don&#39;t overlap each other.</li>
</ol>


## Related Problems
[Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) (Medium) <br>

## What a(n) Medium problem!
Among **236220** total submissions, **102682** are accepted, with an acceptance rate of 43.5%. <br>

- Likes: 1424
- Dislikes: 43


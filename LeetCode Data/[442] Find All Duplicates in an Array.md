# [442] Find All Duplicates in an Array (Medium)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/find-all-duplicates-in-an-array/) 

[Magic Portal](https://leetcode.com/problems/find-all-duplicates-in-an-array/)

## My Submission

- Runtime: 484 ms
- Completed time: 2020-08-06 14:27:06

```python3
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = {}
        ret = []
        for i in nums:
            if i in seen.keys():
                ret.append(i)
            else:
                seen[i] = i
                
            
        return ret
```

## Content
<p>Given an array of integers, 1 &le; a[i] &le; <i>n</i> (<i>n</i> = size of array), some elements appear <b>twice</b> and others appear <b>once</b>.</p>

<p>Find all the elements that appear <b>twice</b> in this array.</p>

<p>Could you do it without extra space and in O(<i>n</i>) runtime?</p>
</p>
<p><b>Example:</b><br/>
<pre>
<b>Input:</b>
[4,3,2,7,8,2,3,1]

<b>Output:</b>
[2,3]
</pre>

## Related Problems
[Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) (Easy) <br>

## What a(n) Medium problem!
Among **321821** total submissions, **218225** are accepted, with an acceptance rate of 67.8%. <br>

- Likes: 2644
- Dislikes: 159


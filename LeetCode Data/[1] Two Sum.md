# [1] Two Sum (Easy)

[![Array_badge](https://img.shields.io/badge/topic-Array-green.svg)](https://leetcode.com/problems/two-sum/)  [![Hash Table_badge](https://img.shields.io/badge/topic-Hash Table-green.svg)](https://leetcode.com/problems/two-sum/) 

:+1: 16378 &nbsp; &nbsp; :thumbsdown: 590

## My Submission

- Runtime: 324 ms
- Completed time: 2019-06-27 19:48:28

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        for (int i = 0; i < nums.size(); ++ i) {
            for (int j = 0; j < nums.size(); ++ j) {
                if (i == j)
                    continue;
                if (nums[i] + nums[j] == target) {
                    result.push_back(i);
                    result.push_back(j);
                    return result;
                }
            }
        }
        return result;
    }
};
```

## Content
<p>Given an array of integers, return <strong>indices</strong> of the two numbers such that they add up to a specific target.</p>

<p>You may assume that each input would have <strong><em>exactly</em></strong> one solution, and you may not use the <em>same</em> element twice.</p>

<p><strong>Example:</strong></p>

<pre>
Given nums = [2, 7, 11, 15], target = 9,

Because nums[<strong>0</strong>] + nums[<strong>1</strong>] = 2 + 7 = 9,
return [<strong>0</strong>, <strong>1</strong>].
</pre>


## Related Problems
[3Sum](https://leetcode.com/problems/3sum/) (Medium) <br>
[4Sum](https://leetcode.com/problems/4sum/) (Medium) <br>
[Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) (Easy) <br>
[Two Sum III - Data structure design](https://leetcode.com/problems/two-sum-iii-data-structure-design/) (Easy) <br>
[Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) (Medium) <br>
[Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/) (Easy) <br>
[Two Sum Less Than K](https://leetcode.com/problems/two-sum-less-than-k/) (Easy) <br>

## What a(n) Easy problem!
Among **7034883** total submissions, **3211483** are accepted, with an acceptance rate of 45.7%. <br>

- Likes: 16378
- Dislikes: 590


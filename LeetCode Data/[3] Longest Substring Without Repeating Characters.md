# [3] Longest Substring Without Repeating Characters (Medium)

[Magic Portal](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## My Submission

- Runtime: N/A
- Completed time: 2020-08-02 15:45:03

```python3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        i = 0
        while i + l <= len(s) and i <= i + l:
            if len(set(s[i:i+l])) == l:
                return l;
            if i + l == len(s):
                l -= 1
                i = 0
            else:
                i += 1
        return l
                
```
## Content

<p>Given a string, find the length of the <b>longest substring</b> without repeating characters.</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">&quot;abcabcbb&quot;</span>
<strong>Output: </strong><span id="example-output-1">3 
<strong>Explanation:</strong></span> The answer is <code>&quot;abc&quot;</code>, with the length of 3. 
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">&quot;bbbbb&quot;</span>
<strong>Output: </strong><span id="example-output-2">1
</span><span id="example-output-1"><strong>Explanation: </strong>T</span>he answer is <code>&quot;b&quot;</code>, with the length of 1.
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">&quot;pwwkew&quot;</span>
<strong>Output: </strong><span id="example-output-3">3
</span><span id="example-output-1"><strong>Explanation: </strong></span>The answer is <code>&quot;wke&quot;</code>, with the length of 3. 
             Note that the answer must be a <b>substring</b>, <code>&quot;pwke&quot;</code> is a <i>subsequence</i> and not a substring.
</pre>
</div>
</div>
</div>


## Related Problems

[Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)
[Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)
[Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/)

## What a(n) Medium problem!


Among **5449137** total submissions, **1659450** are accepted, with an acceptance rate of 30.5%. <br>

- Likes: 10194
- Dislikes: 600


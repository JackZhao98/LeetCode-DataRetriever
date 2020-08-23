# [274] H-Index (Medium)

[![Hash Table_badge](https://img.shields.io/badge/topic-Hash Table-green.svg)](https://leetcode.com/problems/h-index/)  [![Sort_badge](https://img.shields.io/badge/topic-Sort-green.svg)](https://leetcode.com/problems/h-index/) 

[Magic Portal](https://leetcode.com/problems/h-index/)

## My Submission

- Runtime: 36 ms
- Completed time: 2020-08-11 18:19:46

```python3
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        h = 0
        
        for c in citations:
            if c <= h:
                break
            h += 1

        return h
```

## Content
<p>Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher&#39;s h-index.</p>

<p>According to the <a href="https://en.wikipedia.org/wiki/H-index" target="_blank">definition of h-index on Wikipedia</a>: &quot;A scientist has index <i>h</i> if <i>h</i> of his/her <i>N</i> papers have <b>at least</b> <i>h</i> citations each, and the other <i>N &minus; h</i> papers have <b>no more than</b> <i>h</i> citations each.&quot;</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> <code>citations = [3,0,6,1,5]</code>
<b>Output:</b> 3 
<strong>Explanation: </strong><code>[3,0,6,1,5] </code>means the researcher has <code>5</code> papers in total and each of them had 
             received <code>3, 0, 6, 1, 5</code> citations respectively. 
&nbsp;            Since the researcher has <code>3</code> papers with <b>at least</b> <code>3</code> citations each and the remaining 
&nbsp;            two with <b>no more than</b> <code>3</code> citations each, her h-index is <code>3</code>.</pre>

<p><strong>Note:&nbsp;</strong>If there are several possible values for <em>h</em>, the maximum one is taken as the h-index.</p>


## Related Problems
[H-Index II](https://leetcode.com/problems/h-index-ii/) (Medium) <br>

## What a(n) Medium problem!
Among **510410** total submissions, **185019** are accepted, with an acceptance rate of 36.2%. <br>

- Likes: 764
- Dislikes: 1303


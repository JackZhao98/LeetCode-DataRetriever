# [49] Group Anagrams (Medium)

[![Hash%20Table_badge](https://img.shields.io/badge/topic-Hash%20Table-green.svg)](https://leetcode.com/problems/group-anagrams/)  [![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/group-anagrams/) 

:+1: 3857 &nbsp; &nbsp; :thumbsdown: 194

---

## My Submission

- Language: python3
- Runtime: 152 ms
- Completed time: 2020-07-31 23:18:54

```python3
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = {}
        for s in strs:
            k = str(sorted(s))
            if k in ret.keys():
                ret[k].append(s)
            else:
                ret[k] = [s]
        return ret.values()
```

## Content
<p>Given an array of strings, group anagrams together.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> <code>[&quot;eat&quot;, &quot;tea&quot;, &quot;tan&quot;, &quot;ate&quot;, &quot;nat&quot;, &quot;bat&quot;]</code>,
<strong>Output:</strong>
[
  [&quot;ate&quot;,&quot;eat&quot;,&quot;tea&quot;],
  [&quot;nat&quot;,&quot;tan&quot;],
  [&quot;bat&quot;]
]</pre>

<p><strong>Note:</strong></p>

<ul>
	<li>All inputs will be in lowercase.</li>
	<li>The order of your output does not&nbsp;matter.</li>
</ul>


## Related Problems
[Valid Anagram](https://leetcode.com/problems/valid-anagram/) (Easy) <br>
[Group Shifted Strings](https://leetcode.com/problems/group-shifted-strings/) (Medium) <br>

## What a(n) Medium problem!
Among **1268823** total submissions, **724042** are accepted, with an acceptance rate of **57.1%**. <br>

- Likes: 3857
- Dislikes: 194


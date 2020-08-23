# [1286] Iterator for Combination (Medium)

[![Backtracking_badge](https://img.shields.io/badge/topic-Backtracking-green.svg)](https://leetcode.com/problems/iterator-for-combination/)  [![Design_badge](https://img.shields.io/badge/topic-Design-green.svg)](https://leetcode.com/problems/iterator-for-combination/) 

:+1: 454 &nbsp; &nbsp; :thumbsdown: 40

## My Submission

- Runtime: 4032 ms
- Completed time: 2020-08-13 18:21:58

```python3
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.current = 0
        self.combination = []
        self.generate(characters, combinationLength, "")
        self.combination = list(sorted(set(self.combination)))
        print(self.combination)
    def generate(self, chars: str, r: int, tmpString: str):
        if len(tmpString) == r:
            self.combination.append(''.join(sorted(tmpString)))
        else:
            for i in range(len(chars)):
                tmpString += chars[i]
                self.generate(chars[0:i]+ chars[i+1:-1], r, tmpString)
                tmpString = tmpString[:-1]

    def next(self) -> str:
        self.current += 1
        return self.combination[self.current - 1]

    def hasNext(self) -> bool:
        return self.current < len(self.combination)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```

## Content
<p>Design an Iterator class, which has:</p>

<ul>
	<li>A constructor that takes a string&nbsp;<code>characters</code>&nbsp;of <strong>sorted distinct</strong> lowercase English letters and a number&nbsp;<code>combinationLength</code> as arguments.</li>
	<li>A function <em>next()</em>&nbsp;that returns the next combination of length <code>combinationLength</code>&nbsp;in <strong>lexicographical order</strong>.</li>
	<li>A function <em>hasNext()</em> that returns <code>True</code>&nbsp;if and only if&nbsp;there exists a next combination.</li>
</ul>

<p>&nbsp;</p>

<p><b>Example:</b></p>

<pre>
CombinationIterator iterator = new CombinationIterator(&quot;abc&quot;, 2); // creates the iterator.

iterator.next(); // returns &quot;ab&quot;
iterator.hasNext(); // returns true
iterator.next(); // returns &quot;ac&quot;
iterator.hasNext(); // returns true
iterator.next(); // returns &quot;bc&quot;
iterator.hasNext(); // returns false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= combinationLength &lt;=&nbsp;characters.length &lt;= 15</code></li>
	<li>There will be at most <code>10^4</code> function calls per test.</li>
	<li>It&#39;s guaranteed that all&nbsp;calls&nbsp;of the function <code>next</code>&nbsp;are valid.</li>
</ul>


## Related Problems


## What a(n) Medium problem!
Among **46853** total submissions, **33099** are accepted, with an acceptance rate of 70.6%. <br>

- Likes: 454
- Dislikes: 40


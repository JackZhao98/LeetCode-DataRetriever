# [211] Design Add and Search Words Data Structure (Medium)

[Magic Portal](https://leetcode.com/problems/design-add-and-search-words-data-structure/)

## My Submission

- Runtime: N/A
- Completed time: 2020-08-05 18:07:25

```python3
class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.eof = False
    
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        walker = self.root
        for i in range(len(word)):
            j = ord(word[i]) - ord('a')
            if not walker.children[j]:
                walker.children[j] = TrieNode()
            walker = walker.children[j]
        walker.eof = True
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        walker = self.root
        for i in range(len(word)):
            j = ord(word[i]) - ord('a')
            if not walker.children[i]:
                return False
            walker = walker.children[i]
        return walker and walker.eof
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```
## Content

<p>You should design a data structure that supports adding new words and finding if a string matches any previously added string.</p>

<p>Implement the <code>WordDictionary</code> class:</p>

<ul>
	<li><code>WordDictionary()</code>&nbsp;Initializes the object.</li>
	<li><code>void addWord(word)</code> adds <code>word</code> to the data structure, it can be matched later.</li>
	<li><code>bool search(word)</code>&nbsp;returns <code>true</code> if there is any string in the data structure that matches <code>word</code>&nbsp;or <code>false</code> otherwise. <code>word</code> may contain dots <code>&#39;.&#39;</code> where dots can be matched with any letter.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example:</strong></p>

<pre>
<strong>Input</strong>
[&quot;WordDictionary&quot;,&quot;addWord&quot;,&quot;addWord&quot;,&quot;addWord&quot;,&quot;search&quot;,&quot;search&quot;,&quot;search&quot;,&quot;search&quot;]
[[],[&quot;bad&quot;],[&quot;dad&quot;],[&quot;mad&quot;],[&quot;pad&quot;],[&quot;bad&quot;],[&quot;.ad&quot;],[&quot;b..&quot;]]
<strong>Output</strong>
[null,null,null,null,false,true,true,true]

<strong>Explanation</strong>
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord(&quot;bad&quot;);
wordDictionary.addWord(&quot;dad&quot;);
wordDictionary.addWord(&quot;mad&quot;);
wordDictionary.search(&quot;pad&quot;); // return False
wordDictionary.search(&quot;bad&quot;); // return True
wordDictionary.search(&quot;.ad&quot;); // return True
wordDictionary.search(&quot;b..&quot;); // return True
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 500</code></li>
	<li><code>word</code> in <code>addWord</code> consists lower-case English letters.</li>
	<li><code>word</code> in <code>search</code> consist of&nbsp; &#39;.&#39; or lower-case English letters.</li>
	<li>At most <code>50000</code>&nbsp;calls will be made to <code>addWord</code>&nbsp;and <code>search</code> .</li>
</ul>


## Related Problems

[Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)
[Prefix and Suffix Search](https://leetcode.com/problems/prefix-and-suffix-search/)

## What a(n) Medium problem!


Among **588769** total submissions, **224654** are accepted, with an acceptance rate of 38.2%. <br>

- Likes: 2234
- Dislikes: 102


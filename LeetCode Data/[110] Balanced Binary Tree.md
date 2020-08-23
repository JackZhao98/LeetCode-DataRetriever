# [110] Balanced Binary Tree (Easy)

[![Tree_badge](https://img.shields.io/badge/topic-Tree-green.svg)](https://leetcode.com/problems/balanced-binary-tree/)  [![Depth-first Search_badge](https://img.shields.io/badge/topic-Depth-first Search-green.svg)](https://leetcode.com/problems/balanced-binary-tree/) 

:+1: 2444 &nbsp; &nbsp; :thumbsdown: 178

## My Submission

- Runtime: 48 ms
- Completed time: 2020-08-16 18:11:26

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isBalanced(self, root: TreeNode) -> bool:
        def DFS(node, height):
            if not node:
                return height - 1
            L = DFS(node.left, height + 1)
            R = DFS(node.right, height + 1)
            if type(L) != int or type(R) != int:
                return False
            if abs(L - R) > 1:
                return False
            return max(L, R)
        ret = DFS(root, 0)  
        
        return type(ret) == int
```

## Content
<p>Given a binary tree, determine if it is height-balanced.</p>

<p>For this problem, a height-balanced binary tree is defined as:</p>

<blockquote>
<p>a binary tree in which the left and right subtrees of <em>every</em> node differ in height by no more than 1.</p>
</blockquote>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<p>Given the following tree <code>[3,9,20,null,null,15,7]</code>:</p>

<pre>
    3
   / \
  9  20
    /  \
   15   7</pre>

<p>Return true.<br />
<br />
<strong>Example 2:</strong></p>

<p>Given the following tree <code>[1,2,2,3,3,null,null,4,4]</code>:</p>

<pre>
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
</pre>

<p>Return false.</p>


## Related Problems
[Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) (Easy) <br>

## What a(n) Easy problem!
Among **1067411** total submissions, **465428** are accepted, with an acceptance rate of 43.6%. <br>

- Likes: 2444
- Dislikes: 178


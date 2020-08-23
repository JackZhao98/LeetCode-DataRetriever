# [559] Maximum Depth of N-ary Tree (Easy)

[![Tree_badge](https://img.shields.io/badge/topic-Tree-green.svg)](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)  [![Depth-first Search_badge](https://img.shields.io/badge/topic-Depth-first Search-green.svg)](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)  [![Breadth-first Search_badge](https://img.shields.io/badge/topic-Breadth-first Search-green.svg)](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/) 

:+1: 916 &nbsp; &nbsp; :thumbsdown: 50

## My Submission

- Runtime: 144 ms
- Completed time: 2019-08-12 02:42:42

```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
public:
    int maxDepth(Node* root) {
        if(!root) {
            return 0;
        }
        int depth = 0;
        for(int i = 0 ; i < root -> children.size() ; i++){
            depth = max(depth,maxDepth(root->children[i]));
        }
        return depth + 1;
    }
};
```

## Content
<p>Given a n-ary tree, find its maximum depth.</p>

<p>The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.</p>

<p><em>Nary-Tree input serialization&nbsp;is represented in their level order traversal, each group of children is separated by the null value (See examples).</em></p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png" style="width: 100%; max-width: 300px;" /></p>

<pre>
<strong>Input:</strong> root = [1,null,3,2,4,null,5,6]
<strong>Output:</strong> 3
</pre>

<p><strong>Example 2:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png" style="width: 296px; height: 241px;" /></p>

<pre>
<strong>Input:</strong> root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
<strong>Output:</strong> 5
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The depth of the n-ary tree is less than or equal to <code>1000</code>.</li>
	<li>The total number of nodes is between <code>[0,&nbsp;10^4]</code>.</li>
</ul>


## Related Problems
[Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) (Easy) <br>

## What a(n) Easy problem!
Among **174535** total submissions, **119945** are accepted, with an acceptance rate of 68.7%. <br>

- Likes: 916
- Dislikes: 50


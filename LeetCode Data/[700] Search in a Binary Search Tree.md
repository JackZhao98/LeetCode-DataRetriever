# [700] Search in a Binary Search Tree (Easy)

[![Tree_badge](https://img.shields.io/badge/topic-Tree-green.svg)](https://leetcode.com/problems/search-in-a-binary-search-tree/) 

:+1: 927 &nbsp; &nbsp; :thumbsdown: 120

---

## My Submission

- Language: cpp
- Runtime: 52 ms
- Completed time: 2019-07-24 19:08:13

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* searchBST(TreeNode* root, int val) {
        if (!root) {
            return nullptr;
        }
        TreeNode* found = nullptr;
        if (val > root -> val) {
            // GO TO RIGHT
            found = searchBST(root -> right, val);
        }
        else if (val < root -> val) {
            // GO TO LEFT
            found = searchBST(root -> left, val);
        }
        else {
            return root;
        }
        return found;
    }
};
```

## Content
<p>Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node&#39;s value equals the given value. Return the subtree rooted with that node. If such node doesn&#39;t exist, you should return NULL.</p>

<p>For example,&nbsp;</p>

<pre>
Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
</pre>

<p>You should return this subtree:</p>

<pre>
      2     
     / \   
    1   3
</pre>

<p>In the example above, if we want to search the value <code>5</code>, since there is no node with value <code>5</code>, we should return <code>NULL</code>.</p>

<p>Note that an empty tree is represented by <code>NULL</code>, therefore you would see the expected output (serialized tree format) as&nbsp;<code>[]</code>, not <code>null</code>.</p>


## Related Problems
[Closest Binary Search Tree Value](https://leetcode.com/problems/closest-binary-search-tree-value/) (Easy) <br>
[Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/) (Medium) <br>

## What a(n) Easy problem!
Among **276275** total submissions, **202077** are accepted, with an acceptance rate of **73.1%**. <br>

- Likes: 927
- Dislikes: 120


# [98] Validate Binary Search Tree (Medium)

[Magic Portal](https://leetcode.com/problems/validate-binary-search-tree/)

## My Submission

- Runtime: N/A
- Completed time: 2019-06-28 21:58:08

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
    bool isValidBST(TreeNode* root) {
        bool success = false;
        if (!root) {
            return true;
        }
        if (!root -> left || !root -> right) {
            return true;
        }
        
        success = isValidBST(root->left);
        success = isValidBST(root->right);
        
        if (root -> val  <= root->left->val || root -> val  >= root->right->val)
            return false;
        
        return true;
        
        
    }
};
```
## Content

<p>Given a binary tree, determine if it is a valid binary search tree (BST).</p>

<p>Assume a BST is defined as follows:</p>

<ul>
	<li>The left subtree of a node contains only nodes with keys <strong>less than</strong> the node&#39;s key.</li>
	<li>The right subtree of a node contains only nodes with keys <strong>greater than</strong> the node&#39;s key.</li>
	<li>Both the left and right subtrees must also be binary search trees.</li>
</ul>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
    2
   / \
  1   3

<strong>Input:</strong>&nbsp;[2,1,3]
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
    5
   / \
  1   4
&nbsp;    / \
&nbsp;   3   6

<strong>Input:</strong> [5,1,4,null,null,3,6]
<strong>Output:</strong> false
<strong>Explanation:</strong> The root node&#39;s value is 5 but its right child&#39;s value is 4.
</pre>


## Related Problems

[Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
[Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree/)

## What a(n) Medium problem!


Among **2634548** total submissions, **732813** are accepted, with an acceptance rate of 27.8%. <br>

- Likes: 4222
- Dislikes: 558


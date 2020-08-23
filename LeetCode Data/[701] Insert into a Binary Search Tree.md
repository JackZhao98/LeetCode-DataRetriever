# [701] Insert into a Binary Search Tree (Medium)

[![Tree_badge](https://img.shields.io/badge/topic-Tree-green.svg)](https://leetcode.com/problems/insert-into-a-binary-search-tree/) 

:+1: 947 &nbsp; &nbsp; :thumbsdown: 80

## My Submission

- Runtime: 96 ms
- Completed time: 2019-07-24 20:02:30

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
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if (!root) {
            TreeNode* temp = new TreeNode(val);
            return temp;
        }
        
        if (val < root -> val) 
            root -> left = insertIntoBST(root->left, val);
        else
            root -> right = insertIntoBST(root -> right, val);
        
        return root;
    }
};
```

## Content
<p>Given the root node of a binary search tree (BST) and a value to be inserted into the tree,&nbsp;insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.</p>

<p>Note that there may exist&nbsp;multiple valid ways for the&nbsp;insertion, as long as the tree remains a BST after insertion. You can return any of them.</p>

<p>For example,&nbsp;</p>

<pre>
Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
</pre>

<p>You can return this binary search tree:</p>

<pre>
         4
       /   \
      2     7
     / \   /
    1   3 5
</pre>

<p>This tree is also valid:</p>

<pre>
         5
       /   \
      2     7
     / \   
    1   3
         \
          4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the given tree will be between <code>0</code> and <code>10^4</code>.</li>
	<li>Each node will have a unique integer value from <code>0</code>&nbsp;to -<code>10^8</code>, inclusive.</li>
	<li><code>-10^8 &lt;= val &lt;= 10^8</code></li>
	<li>It&#39;s guaranteed that <code>val</code> does not exist in the original BST.</li>
</ul>


## Related Problems
[Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/) (Easy) <br>

## What a(n) Medium problem!
Among **148816** total submissions, **115318** are accepted, with an acceptance rate of 77.5%. <br>

- Likes: 947
- Dislikes: 80


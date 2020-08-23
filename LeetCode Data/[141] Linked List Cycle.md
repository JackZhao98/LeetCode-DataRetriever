# [141] Linked List Cycle (Easy)

[![LinkedList_badge](https://img.shields.io/badge/topic-LinkedList-green.svg)](https://leetcode.com/problems/linked-list-cycle/)  [![TwoPointers_badge](https://img.shields.io/badge/topic-TwoPointers-green.svg)](https://leetcode.com/problems/linked-list-cycle/) 

:+1: 3131 &nbsp; &nbsp; :thumbsdown: 524

## My Submission

- Runtime: 48 ms
- Completed time: 2020-06-24 13:55:02

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head
        while True:
            if fast is None or fast.next is None:
                return False
            
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                return True
            
            
            
```

## Content
<p>Given a linked list, determine if it has a cycle in it.</p>

<p>To represent a cycle in the given linked list, we use an integer <code>pos</code> which represents the position (0-indexed)&nbsp;in the linked list where tail connects to. If <code>pos</code> is <code>-1</code>, then there is no cycle in the linked list.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>head = <span id="example-input-1-1">[3,2,0,-4]</span>, pos = <span id="example-input-1-2">1</span>
<strong>Output: </strong><span id="example-output-1">true
<strong>Explanation:</strong> There is a cycle in the linked list, where tail connects to the second node.</span>
</pre>
</div>

<div>
<p><span><img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png" style="width: 300px; height: 97px; margin-top: 8px; margin-bottom: 8px;" /></span></p>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>head = <span id="example-input-1-1">[1,2]</span>, pos = <span id="example-input-1-2">0</span>
<strong>Output: </strong><span id="example-output-1">true
<strong>Explanation:</strong> There is a cycle in the linked list, where tail connects to the first node.</span>
</pre>
</div>

<div>
<p><span><img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png" style="width: 141px; height: 74px;" /></span></p>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>head = <span id="example-input-1-1">[1]</span>, pos = <span id="example-input-1-2">-1</span>
<strong>Output: </strong><span id="example-output-1">false
<strong>Explanation:</strong> There is no cycle in the linked list.</span>
</pre>
</div>

<p><span><img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png" style="width: 45px; height: 45px;" /></span></p>

<p>&nbsp;</p>

<p><strong>Follow up:</strong></p>

<p>Can you solve it using <em>O(1)</em> (i.e. constant) memory?</p>


## Related Problems
[Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) (Medium) <br>
[Happy Number](https://leetcode.com/problems/happy-number/) (Easy) <br>

## What a(n) Easy problem!
Among **1637676** total submissions, **675050** are accepted, with an acceptance rate of 41.2%. <br>

- Likes: 3131
- Dislikes: 524


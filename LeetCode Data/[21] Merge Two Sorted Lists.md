# [21] Merge Two Sorted Lists (Easy)

[![LinkedList_badge](https://img.shields.io/badge/topic-LinkedList-green.svg)](https://leetcode.com/problems/merge-two-sorted-lists/) 

:+1: 4682 &nbsp; &nbsp; :thumbsdown: 611

## My Submission

- Runtime: 44 ms
- Completed time: 2020-07-29 15:18:33

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        walker = head
        while l1 or l2:
            walker.next = ListNode()
            walker = walker.next
            
            if not l1:
                walker.val = l2.val
                l2 = l2.next
            elif not l2:
                walker.val = l1.val
                l1 = l1.next
            else:
                if l1.val < l2.val:
                    walker.val = l1.val
                    l1 = l1.next
                else:
                    walker.val = l2.val
                    l2 = l2.next
            
            
        return head.next
```

## Content
<p>Merge two sorted linked lists and return it as a new <strong>sorted</strong> list. The new list should be made by splicing together the nodes of the first two lists.</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> 1-&gt;2-&gt;4, 1-&gt;3-&gt;4
<b>Output:</b> 1-&gt;1-&gt;2-&gt;3-&gt;4-&gt;4
</pre>


## Related Problems
[Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) (Hard) <br>
[Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) (Easy) <br>
[Sort List](https://leetcode.com/problems/sort-list/) (Medium) <br>
[Shortest Word Distance II](https://leetcode.com/problems/shortest-word-distance-ii/) (Medium) <br>

## What a(n) Easy problem!
Among **1993973** total submissions, **1071280** are accepted, with an acceptance rate of 53.7%. <br>

- Likes: 4682
- Dislikes: 611


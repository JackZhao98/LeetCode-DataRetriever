# [143] Reorder List (Medium)

[![Linked List_badge](https://img.shields.io/badge/topic-Linked List-green.svg)](https://leetcode.com/problems/reorder-list/) 

:+1: 2335 &nbsp; &nbsp; :thumbsdown: 125

## My Submission

- Runtime: 172 ms
- Completed time: 2020-08-20 17:20:02

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        wugui = head
        tuzi = head
        while tuzi and tuzi.next and tuzi.next.next:
            wugui = wugui.next
            tuzi = tuzi.next.next
        tmp = wugui.next
        wugui.next = None
        wugui = tmp
        
        half = []
        while wugui:
            half.append(wugui)
            wugui = wugui.next
        
        walker = head
        while walker and half:
            wugui = half.pop(-1)
            tmp = walker.next
            walker.next = wugui
            
            tmp_wugui_nxt = wugui.next
            wugui.next = tmp
            wugui = tmp_wugui_nxt
            
            walker = tmp
```

## Content
<p>Given a singly linked list <em>L</em>: <em>L</em><sub>0</sub>&rarr;<em>L</em><sub>1</sub>&rarr;&hellip;&rarr;<em>L</em><sub><em>n</em>-1</sub>&rarr;<em>L</em><sub>n</sub>,<br />
reorder it to: <em>L</em><sub>0</sub>&rarr;<em>L</em><sub><em>n</em></sub>&rarr;<em>L</em><sub>1</sub>&rarr;<em>L</em><sub><em>n</em>-1</sub>&rarr;<em>L</em><sub>2</sub>&rarr;<em>L</em><sub><em>n</em>-2</sub>&rarr;&hellip;</p>

<p>You may <strong>not</strong> modify the values in the list&#39;s nodes, only nodes itself may be changed.</p>

<p><strong>Example 1:</strong></p>

<pre>
Given 1-&gt;2-&gt;3-&gt;4, reorder it to 1-&gt;4-&gt;2-&gt;3.</pre>

<p><strong>Example 2:</strong></p>

<pre>
Given 1-&gt;2-&gt;3-&gt;4-&gt;5, reorder it to 1-&gt;5-&gt;2-&gt;4-&gt;3.
</pre>


## Related Problems


## What a(n) Medium problem!
Among **687716** total submissions, **266538** are accepted, with an acceptance rate of 38.8%. <br>

- Likes: 2335
- Dislikes: 125


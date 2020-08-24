# [234] Palindrome Linked List (Easy)

[![Linked%20List_badge](https://img.shields.io/badge/topic-Linked%20List-green.svg)](https://leetcode.com/problems/palindrome-linked-list/)  [![Two%20Pointers_badge](https://img.shields.io/badge/topic-Two%20Pointers-green.svg)](https://leetcode.com/problems/palindrome-linked-list/) 

:+1: 3482 &nbsp; &nbsp; :thumbsdown: 374

---

## My Submission

- Language: python3
- Runtime: 68 ms
- Completed time: 2020-04-15 12:47:05

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        prev = None
        while (slow and fast): #are not None
            if (fast.next is None):
                fast = slow.next
                slow = prev
                break
            
            elif (fast.next.next is None):
                fast = slow.next
                slow.next = prev
                break
                
            else:
                fast = fast.next.next
                
                # reverse current node
                Next = slow.next
                slow.next = prev
                prev = slow
                
                #move slow one step ahead
                slow = Next
                
                
            # fast can go one or more steps

            
        
        
        while (slow and fast):
            if (slow.val != fast.val):
                return False
            slow = slow.next
            fast = fast.next
        
        return True
                
                
```

## Content
<p>Given a singly linked list, determine if it is a palindrome.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 1-&gt;2
<strong>Output:</strong> false</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 1-&gt;2-&gt;2-&gt;1
<strong>Output:</strong> true</pre>

<p><b>Follow up:</b><br />
Could you do it in O(n) time and O(1) space?</p>


## Related Problems
[Palindrome Number](https://leetcode.com/problems/palindrome-number/) (Easy) <br>
[Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) (Easy) <br>
[Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) (Easy) <br>

## What a(n) Easy problem!
Among **1150227** total submissions, **452893** are accepted, with an acceptance rate of **39.4%**. <br>

- Likes: 3482
- Dislikes: 374


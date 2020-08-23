# [2] Add Two Numbers (Medium)

[![LinkedList_badge](https://img.shields.io/badge/topic-LinkedList-green.svg)](https://leetcode.com/problems/add-two-numbers/)  [![Math_badge](https://img.shields.io/badge/topic-Math-green.svg)](https://leetcode.com/problems/add-two-numbers/) 

:+1: 8899 &nbsp; &nbsp; :thumbsdown: 2246

## My Submission

- Runtime: 28 ms
- Completed time: 2019-06-27 20:15:26

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        bool carry = false;
        ListNode* result = new ListNode(999);
        int l1_num, l2_num;
        ListNode* walker = result;
        
        while (l1 || l2) {
            // if ((l1 && l1 -> next) || (l2&&l2 -> next) || carry) {
            //     walker -> next = new ListNode(1);
            // }
            
            if (l1) {
                if (l1 -> next)
                    walker -> next = new ListNode(1);
            }
            if (l2 && !walker -> next) {
                if (l2 -> next)
                    walker -> next = new ListNode(1);
            }
            
                
            
            l1_num = l2_num = 0;
            if (l1) {
                l1_num = l1 -> val;
                l1 = l1 -> next;
            }
            if (l2) {
                l2_num = l2 -> val;
                l2 = l2 -> next;
            }
            int tempDigit = l1_num + l2_num;
            if (carry) {
                carry = false;
                ++ tempDigit;
            }
            if (tempDigit >= 10) {
                carry = true;
                tempDigit -= 10;
            }
            walker -> val = tempDigit;
            
            if (carry && !(l1&&l2)) {
               walker -> next = new ListNode(1);
            }
            walker = walker -> next;
        }
       
        return result;
    }
};
```

## Content
<p>You are given two <b>non-empty</b> linked lists representing two non-negative integers. The digits are stored in <b>reverse order</b> and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.</p>

<p>You may assume the two numbers do not contain any leading zero, except the number 0 itself.</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> (2 -&gt; 4 -&gt; 3) + (5 -&gt; 6 -&gt; 4)
<b>Output:</b> 7 -&gt; 0 -&gt; 8
<b>Explanation:</b> 342 + 465 = 807.
</pre>


## Related Problems
[Multiply Strings](https://leetcode.com/problems/multiply-strings/) (Medium) <br>
[Add Binary](https://leetcode.com/problems/add-binary/) (Easy) <br>
[Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) (Medium) <br>
[Add Strings](https://leetcode.com/problems/add-strings/) (Easy) <br>
[Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/) (Medium) <br>
[Add to Array-Form of Integer](https://leetcode.com/problems/add-to-array-form-of-integer/) (Easy) <br>

## What a(n) Medium problem!
Among **4412499** total submissions, **1498687** are accepted, with an acceptance rate of 34.0%. <br>

- Likes: 8899
- Dislikes: 2246


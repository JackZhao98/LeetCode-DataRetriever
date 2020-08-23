# [707] Design Linked List (Medium)

[![Linked List_badge](https://img.shields.io/badge/topic-Linked List-green.svg)](https://leetcode.com/problems/design-linked-list/)  [![Design_badge](https://img.shields.io/badge/topic-Design-green.svg)](https://leetcode.com/problems/design-linked-list/) 

:+1: 600 &nbsp; &nbsp; :thumbsdown: 722

## My Submission

- Runtime: 36 ms
- Completed time: 2019-07-24 07:29:36

```cpp
const int fastio = [&]{
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    return 0;
}();

class MyLinkedList {
private:
    struct Node {
        int val;
        Node* next;
        Node(int _val = 0, Node* _next = nullptr):val(_val), next(_next) {}
    };
    
    Node* head;
    int length;
    
public:
    /** Initialize your data structure here. */
    MyLinkedList() {
        head = nullptr;
        length = 0;
    }
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    int get(int index) {
        if (index >= length) 
            return -1;
        if (!head || index < 0)
            return -1;
        if (index == 0) {
            return head -> val;
        }
        Node* walker = head;
        for (int i = 0; i < index; ++ i) {
            walker = walker -> next;
        }
        if (!walker) {
            return -1;
        }
        return walker -> val;
    }
    
    Node* at(int index) {
        if (index >= length) 
            return nullptr;
        if (!head || index < 0)
            return nullptr;
        Node* walker = head;
        while (index-- > 0) {
            walker = walker -> next;
        }
        return walker;
    }
    
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(int val) {
        Node* newHead = new Node(val);
        newHead -> next = head;
        head = newHead;
        length ++;
    }
    
    /** Append a node of value val to the last element of the linked list. */
    void addAtTail(int val) {
        if (!head) {
            head = new Node(val);
            length ++;
            return;
        }
        Node* walker = head;
        while (walker -> next) {
            walker = walker->next;
        }
        walker->next = new Node(val);
        length ++;
    }
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    void addAtIndex(int index, int val) {
        if (index > length)
            return;
        
        if (index <= 0) {
            addAtHead(val);
            return;
        }
        
        if (index == length) {
            addAtTail(val);
            return;
        }
        
        Node* walker = head;
        while (index-- > 1) {
            walker = walker -> next;
        }
        Node* curNext = walker -> next;
        Node* newNode = new Node(val);
        newNode -> next = curNext;
        walker -> next = newNode;
        length ++;
    }
    
    Node* prevNode(Node* target) {
        Node* walker = head;
        if (target == head) {
            return nullptr;
        }
        while (walker -> next != nullptr) {
            if (!walker)
                return nullptr;
            if (walker -> next == target)
                return walker;
            walker = walker -> next;
        }
        return nullptr;
    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index) {
        if (index == 0) {
            Node* temp = head -> next;
            delete head;
            head = temp;
            length--;
            return;
            
        }
        Node* deleteThis = at(index);
        if (!deleteThis) {
            return;
        }
        Node* prev = prevNode(deleteThis);
        
        prev -> next = deleteThis -> next;
        delete deleteThis;
        length --;
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
```

## Content
<p>Design your&nbsp;implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly&nbsp;linked list should have two attributes: <code>val</code>&nbsp;and <code>next</code>. <code>val</code> is the value of the current node, and <code>next</code>&nbsp;is&nbsp;a&nbsp;pointer/reference to the next node. If you want to use the doubly linked list,&nbsp;you will need&nbsp;one more attribute <code>prev</code> to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.</p>

<p>Implement these functions in your linked list class:</p>

<ul>
	<li><code>get(index)</code> : Get the value of&nbsp;the <code>index</code>-th&nbsp;node in the linked list. If the index is invalid, return <code>-1</code>.</li>
	<li><code>addAtHead(val)</code> : Add a node of value <code>val</code>&nbsp;before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.</li>
	<li><code>addAtTail(val)</code> : Append a node of value <code>val</code>&nbsp;to the last element of the linked list.</li>
	<li><code>addAtIndex(index, val)</code> : Add a node of value <code>val</code>&nbsp;before the <code>index</code>-th&nbsp;node in the linked list.&nbsp;If <code>index</code>&nbsp;equals&nbsp;to the length of&nbsp;linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.</li>
	<li><code>deleteAtIndex(index)</code> : Delete&nbsp;the <code>index</code>-th&nbsp;node in the linked list, if the index is valid.</li>
</ul>

<p>&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>
<b>Input: </b>
[&quot;MyLinkedList&quot;,&quot;addAtHead&quot;,&quot;addAtTail&quot;,&quot;addAtIndex&quot;,&quot;get&quot;,&quot;deleteAtIndex&quot;,&quot;get&quot;]
[[],[1],[3],[1,2],[1],[1],[1]]
<b>Output: </b> 
[null,null,null,null,2,null,3]

<b>Explanation:</b>
MyLinkedList linkedList = new MyLinkedList(); // Initialize empty LinkedList
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1-&gt;2-&gt;3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1-&gt;3
linkedList.get(1);&nbsp;&nbsp;&nbsp;         // returns 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= index,val &lt;= 1000</code></li>
	<li>Please do not use the built-in LinkedList library.</li>
	<li>At most <code>2000</code>&nbsp;calls will be made to&nbsp;<code>get</code>,&nbsp;<code>addAtHead</code>,&nbsp;<code>addAtTail</code>,&nbsp; <code>addAtIndex</code> and&nbsp;<code>deleteAtIndex</code>.</li>
</ul>


## Related Problems
[Design Skiplist](https://leetcode.com/problems/design-skiplist/) (Hard) <br>

## What a(n) Medium problem!
Among **287810** total submissions, **71013** are accepted, with an acceptance rate of 24.7%. <br>

- Likes: 600
- Dislikes: 722


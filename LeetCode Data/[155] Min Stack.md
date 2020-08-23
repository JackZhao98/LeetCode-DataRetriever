# [155] Min Stack (Easy)

[![Stack_badge](https://img.shields.io/badge/topic-Stack-green.svg)](https://leetcode.com/problems/min-stack/)  [![Design_badge](https://img.shields.io/badge/topic-Design-green.svg)](https://leetcode.com/problems/min-stack/) 

:+1: 3665 &nbsp; &nbsp; :thumbsdown: 348

## My Submission

- Runtime: 2588 ms
- Completed time: 2020-06-24 14:45:49

```python3
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        return None

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        ret = None
        for x in self.stack:
            if ret is None:
                ret = x
            elif ret > x:
                ret = x
        return ret


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

## Content
<p>Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.</p>

<ul>
	<li>push(x) -- Push element x onto stack.</li>
	<li>pop() -- Removes the element on top of the stack.</li>
	<li>top() -- Get the top element.</li>
	<li>getMin() -- Retrieve the minimum element in the stack.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;MinStack&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;getMin&quot;,&quot;pop&quot;,&quot;top&quot;,&quot;getMin&quot;]
[[],[-2],[0],[-3],[],[],[],[]]

<strong>Output</strong>
[null,null,null,null,-3,null,0,-2]

<strong>Explanation</strong>
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>Methods <code>pop</code>, <code>top</code> and <code>getMin</code> operations will always be called on <strong>non-empty</strong> stacks.</li>
</ul>


## Related Problems
[Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) (Hard) <br>
[Max Stack](https://leetcode.com/problems/max-stack/) (Easy) <br>

## What a(n) Easy problem!
Among **1304936** total submissions, **582031** are accepted, with an acceptance rate of 44.6%. <br>

- Likes: 3665
- Dislikes: 348


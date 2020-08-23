# [17] Letter Combinations of a Phone Number (Medium)

[![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)  [![Backtracking_badge](https://img.shields.io/badge/topic-Backtracking-green.svg)](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) 

:+1: 4203 &nbsp; &nbsp; :thumbsdown: 431

## My Submission

- Runtime: 28 ms
- Completed time: 2020-08-06 17:32:32

```python3
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        Map = {"2": "abc", "3": "def", "4": "ghi",
              "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        L = len(digits)
        nums = [1]*(L)
        
        for i in range(L - 1, 0, -1):
            nums[i - 1] = nums[i] * 3 if digits[i] != "9" and digits[i] != "7" else nums[i] * 4
        
        total = nums[0] * 3 if digits[0] != "9" and digits[0] != "7" else nums[0] * 4
        
        ret = [""] * total
    
        for i in range(L):
            for j in range(total):
                ret[j] += Map[digits[i]][(j // nums[i]) % len(Map[digits[i]])]
        return ret
                    
                    
```

## Content
<p>Given a string containing digits from <code>2-9</code> inclusive, return all possible letter combinations that the number could represent.</p>

<p>A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.</p>

<p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png" /></p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input: </strong>&quot;23&quot;
<strong>Output:</strong> [&quot;ad&quot;, &quot;ae&quot;, &quot;af&quot;, &quot;bd&quot;, &quot;be&quot;, &quot;bf&quot;, &quot;cd&quot;, &quot;ce&quot;, &quot;cf&quot;].
</pre>

<p><strong>Note:</strong></p>

<p>Although the above answer is in lexicographical order, your answer could be in any order you want.</p>


## Related Problems
[Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) (Medium) <br>
[Combination Sum](https://leetcode.com/problems/combination-sum/) (Medium) <br>
[Binary Watch](https://leetcode.com/problems/binary-watch/) (Easy) <br>

## What a(n) Medium problem!
Among **1364846** total submissions, **640771** are accepted, with an acceptance rate of 46.9%. <br>

- Likes: 4203
- Dislikes: 431


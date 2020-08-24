# [51] N-Queens (Hard)

[![Backtracking_badge](https://img.shields.io/badge/topic-Backtracking-green.svg)](https://leetcode.com/problems/n-queens/) 

:+1: 2063 &nbsp; &nbsp; :thumbsdown: 77

---

## My Submission

- Language: cpp
- Runtime: 8 ms
- Completed time: 2019-09-03 00:28:59

```cpp
class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> res;
        vector<string> init;
        for (int i = 0; i < n; ++i) {
            init.push_back(string(n,'.'));
        }

        dfs(res, init, n, 0);

        return res;
    }
    
    void dfs(vector<vector<string>>& resolution, vector<string>& currentRes, const int n, int row) {
    // Base case:
    // row >= n
        if (row == n) {

            resolution.push_back(currentRes);

            return;
        }

        for (int col = 0; col < n; ++ col) {
            if (isValid(currentRes, n, row, col)) {
                currentRes[row][col] = 'Q';
                dfs(resolution, currentRes, n, row + 1);
                currentRes[row][col] = '.';
            }
        }
    }   
    
    bool isValid(vector<string>& currentRes, const int n, int row, int col) {
        for (int i = 0; i < n; ++ i) {
            if (currentRes[i][col] == 'Q')
                return false;
        }
        // 反斜线(\)
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; --i, --j) {
            if (currentRes[i][j] == 'Q')
                return false;
        }

        // 正斜线(/)
        for (int i = row - 1, j = col + 1; i >= 0&& j < n; --i, ++ j) {
            if (currentRes[i][j] == 'Q')
                return false;
        }

        return true;
    }
};
```

## Content
<p>The <em>n</em>-queens puzzle is the problem of placing <em>n</em> queens on an <em>n</em>&times;<em>n</em> chessboard such that no two queens attack each other.</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2018/10/12/8-queens.png" style="width: 258px; height: 276px;" /></p>

<p>Given an integer <em>n</em>, return all distinct solutions to the <em>n</em>-queens puzzle.</p>

<p>Each solution contains a distinct board configuration of the <em>n</em>-queens&#39; placement, where <code>&#39;Q&#39;</code> and <code>&#39;.&#39;</code> both indicate a queen and an empty space respectively.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 4
<strong>Output:</strong> [
 [&quot;.Q..&quot;,  // Solution 1
  &quot;...Q&quot;,
  &quot;Q...&quot;,
  &quot;..Q.&quot;],

 [&quot;..Q.&quot;,  // Solution 2
  &quot;Q...&quot;,
  &quot;...Q&quot;,
  &quot;.Q..&quot;]
]
<strong>Explanation:</strong> There exist two distinct solutions to the 4-queens puzzle as shown above.
</pre>


## Related Problems
[N-Queens II](https://leetcode.com/problems/n-queens-ii/) (Hard) <br>
[Grid Illumination](https://leetcode.com/problems/grid-illumination/) (Hard) <br>

## What a(n) Hard problem!
Among **448377** total submissions, **210109** are accepted, with an acceptance rate of **46.9%**. <br>

- Likes: 2063
- Dislikes: 77


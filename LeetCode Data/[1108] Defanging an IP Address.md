# [1108] Defanging an IP Address (Easy)

[![String_badge](https://img.shields.io/badge/topic-String-green.svg)](https://leetcode.com/problems/defanging-an-ip-address/) 

:+1: 439 &nbsp; &nbsp; :thumbsdown: 877

---

## My Submission

- Language: cpp
- Runtime: 4 ms
- Completed time: 2019-07-25 00:40:11

```cpp
static const auto _____ = []()
{
    // fast IO code : this I understand
    ios::sync_with_stdio(false);
    cin.tie(0);
    return 0;
}();

class Solution {
public:
    string defangIPaddr(string address) {
        int len = address.size();
        string defanged = "";
        for (int i = 0; i < len; ++ i) {
            if (address[i] == '.') {
                defanged += "[.]";
            } else 
                defanged += address[i];
        }
        return defanged;
    }
};
```

## Content
<p>Given a valid (IPv4) IP <code>address</code>, return a defanged version of that IP address.</p>

<p>A <em>defanged&nbsp;IP address</em>&nbsp;replaces every period <code>&quot;.&quot;</code> with <code>&quot;[.]&quot;</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> address = "1.1.1.1"
<strong>Output:</strong> "1[.]1[.]1[.]1"
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> address = "255.100.50.0"
<strong>Output:</strong> "255[.]100[.]50[.]0"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The given <code>address</code> is a valid IPv4 address.</li>
</ul>

## Related Problems


## What a(n) Easy problem!
Among **244554** total submissions, **214419** are accepted, with an acceptance rate of **87.7%**. <br>

- Likes: 439
- Dislikes: 877


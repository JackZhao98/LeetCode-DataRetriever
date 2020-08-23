# [191] Number of 1 Bits (Easy)

[![BitManipulation_badge](https://img.shields.io/badge/topic-BitManipulation-green.svg)](https://leetcode.com/problems/number-of-1-bits/) 

:+1: 943 &nbsp; &nbsp; :thumbsdown: 536

## My Submission

- Runtime: 4 ms
- Completed time: 2020-07-29 14:34:18

```c
int hammingWeight(uint32_t n) {
    int i;
    int ret = 0;
    for (i = 0; i < 32; i ++)
    {
        ret += ((UINT32_C(1) << i) & n) >> i;
    }
    return ret;
}                                                                                        
```

## Content
<p>Write a function that takes an unsigned integer and return&nbsp;the number of &#39;1&#39;&nbsp;bits it has (also known as the <a href="http://en.wikipedia.org/wiki/Hamming_weight" target="_blank">Hamming weight</a>).</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 00000000000000000000000000001011
<strong>Output:</strong> 3
<strong>Explanation: </strong>The input binary string <code><strong>00000000000000000000000000001011</strong>&nbsp;has a total of three &#39;1&#39; bits.</code>
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 00000000000000000000000010000000
<strong>Output:</strong> 1
<strong>Explanation: </strong>The input binary string <strong>00000000000000000000000010000000</strong>&nbsp;has a total of one &#39;1&#39; bit.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> 11111111111111111111111111111101
<strong>Output:</strong> 31
<strong>Explanation: </strong>The input binary string <strong>11111111111111111111111111111101</strong> has a total of thirty one &#39;1&#39; bits.</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li>Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.</li>
	<li>In Java,&nbsp;the compiler represents the signed integers using <a href="https://en.wikipedia.org/wiki/Two%27s_complement" target="_blank">2&#39;s complement notation</a>. Therefore, in <strong>Example 3</strong>&nbsp;above the input represents the signed integer <code>-3</code>.</li>
</ul>

<p>&nbsp;</p>

<p><b>Follow up</b>:</p>

<p>If this function is called many times, how would you optimize it?</p>


## Related Problems
[Reverse Bits](https://leetcode.com/problems/reverse-bits/) (Easy) <br>
[Power of Two](https://leetcode.com/problems/power-of-two/) (Easy) <br>
[Counting Bits](https://leetcode.com/problems/counting-bits/) (Medium) <br>
[Binary Watch](https://leetcode.com/problems/binary-watch/) (Easy) <br>
[Hamming Distance](https://leetcode.com/problems/hamming-distance/) (Easy) <br>
[Binary Number with Alternating Bits](https://leetcode.com/problems/binary-number-with-alternating-bits/) (Easy) <br>
[Prime Number of Set Bits in Binary Representation](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/) (Easy) <br>

## What a(n) Easy problem!
Among **749554** total submissions, **374985** are accepted, with an acceptance rate of 50.0%. <br>

- Likes: 943
- Dislikes: 536


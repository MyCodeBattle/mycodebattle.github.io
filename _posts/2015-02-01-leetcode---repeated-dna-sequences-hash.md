---
categories: Posts
date: 2015-02-01 00:00:00
title: LeetCode - Repeated DNA Sequences (Hash)
tags: []
layout: post
---

#  [LeetCode - Repeated DNA Sequences (Hash)](/2015/02/leetcode-repeted dna sequences/ "LeetCode - Repeated DNA Sequences \(Hash\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Feb 23 2015 23:52

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

输出重复两次以上的字符串。

## 思路

一开始用map直接判重string，MLE了。

后来用了双MOD去hash，跪了。可能是不会选素数。

后来用十进制hash，本地跟服务器输出死活对不上。折腾了很久才发现LeetCode是多组数据输入。

其实只有四个数，直接四进制hash就行，这样数组就开得下，$O(1)$的hash。

## 代码

```  
class Solution {  
public:  
int idx(char c)  
{  
if (c == ‘A’) return 0;  
if (c == ‘T’) return 1;  
if (c == ‘C’) return 2;  
if (c == ‘G’) return 3;  
}  
vector findRepeatedDnaSequences(string s) {  
vector ans;  
vis.clear();  
bool mp[1048576+10] = {0};  
bool vis[1048576+10] = {0};  
for (int i = 0; i+10 <= SZ(s); i++)  
{  
string tmp = s.substr(i, 10);  
LL H = 0;  
for (int i = 0; i < 10; i++)  
H = H*4 + idx(tmp[i]);  
if (vis[H]) continue;  
if (mp[H]) ans.PB(tmp), vis[H] = 1;  
else mp[H] = 1;  
}  
return ans;  
}  
};

[Solving Reports](/categories/Solving-Reports/)

[Online Judge - LeetCode](/tags/Online-Judge-LeetCode/)[Foundation - Strings](/tags/Foundation-Strings/)

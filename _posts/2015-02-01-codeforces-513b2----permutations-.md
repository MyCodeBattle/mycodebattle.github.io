---
categories: Posts
date: 2015-02-01 00:00:00
title: Codeforces 513B2 -  Permutations (思维)
tags: []
layout: post
---

#  [Codeforces 513B2 - Permutations (思维)](/2015/02/codeforces-513b/ "Codeforces 513B2 -  Permutations \(思维\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Feb 8 2015 14:00

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

P为一个序列。

定义$F(p) = \sum_{i=1}^n \sum_{j=i}^n min(p_i, p_{i+1},..., p_{j})$

现在要求输出所有满足F(n)最大的序列中字典序第k大的序列。

## 思路

先求出怎样的序列能满足F(p)最大。

假设现在是一个空的序列，那么1是最小的元素，它只能被放在序列的最前面或者最后面。因为如果放在中间产生的结果必定小。

之后考虑2，也和1一样。把1填的那个位置去除之后2也只能放在剩下来的最前面或者最后面。以此类推。

所以总共合法的排列有$2^{n-1}$个。

接下来考虑字典序。

当放1时，如果放第一个，那么剩下来的可能数是$2^{n-1-1}$，当k大于这个数时，显然1放前面无法到达第k大字典序。所以这时候要放后面。

以此类推。把1放后面之后减去1放前面能得到的情况，然后考虑2。和考虑1是一样的。

## 代码
    
    
    12345678910111213141516171819202122232425262728

| 
    
    
    int vis[100];vector<int> ans; int main(){    LL n, k;    cin >> n >> k;    int pos = 1;    for (int i = 0; i < n; i++)        for (; pos <= n; pos++)        {            if (k > (1ll<<(n-pos-1))) k -= (1ll<<(n-pos-1));            else            {                vis[pos] = 1;                ans.PB(pos);                pos++;                break;            }        }    for (int i = n; i >= 1; i--)    {        if (vis[i]) continue;        ans.PB(i);    }    for (auto i: ans) printf("%d ", i);    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - Codeforces](/tags/Online-Judge-Codeforces/)[Foundation - Jizhi](/tags/Foundation-Jizhi/)

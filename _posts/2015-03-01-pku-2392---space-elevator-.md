---
categories: Posts
date: 2015-03-01 00:00:00
title: PKU 2392 - Space Elevator (背包)
tags: []
layout: post
---

#  [PKU 2392 - Space Elevator (背包)](/2015/03/PKU-2392/ "PKU 2392 - Space Elevator \(背包\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Mar 5 2015 23:32

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

给出几种类型的积木，高，高度限制，数量，问最高能叠多少。

## 思路

按高度限制从小到大排序，然后就背包了。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334

| 
    
    
    struct POINT{    int h, a, q;    bool operator < (const POINT &b) const    {        return a < b.a;    }}p[MAXN]; int dp[41000], num[41000]; int main(){    //ROP;    int n;    scanf("%d", &n);    for (int i = 0; i < n; i++) scanf("%d%d%d", &p[i].h, &p[i].a, &p[i].q);    sort(p, p+n);    int ans = 0;    dp[0] = 1;    for (int i = 0; i < n; i++)    {        MS(num, 0);        for (int j = p[i].h; j <= p[i].a; j++)            if (!dp[j] && dp[j-p[i].h] && num[j-p[i].h] < p[i].q)            {                dp[j] = 1;                num[j] = num[j-p[i].h] + 1;                ans = max(ans, j);            }    }    printf("%d\n", ans);    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - PKU](/tags/Online-Judge-PKU/)[DP - 背包](/tags/DP-背包/)

---
categories: Posts
date: 2014-07-01 00:00:00
title: HDU 2602 - Bone Collector
tags: []
layout: post
---

#  [HDU 2602 - Bone Collector](/2014/07/HDU-2602/ "HDU 2602 - Bone Collector")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jul 5 2014 21:18

**Contents**

  1. 1. 传送门
  2. 2. 代码

## 传送门

[HDU 2602 - Bone Collector](http://acm.hdu.edu.cn/showproblem.php?pid=2602)

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334

| 
    
    
    #include <cstdio>#include <cstring>#include <algorithm>using namespace std;const int MAXN = 1000 + 100;struct BONE{    unsigned int volumn, value;}bone[MAXN];unsigned int dp[MAXN];int main(){    //freopen("input.txt", "r", stdin);    int T, i, j, n, vol;    scanf("%d", &T);    while (T--)    {        memset(dp, 0, sizeof(dp));        scanf("%d%d", &n, &vol);        for (i = 0; i < n; i++)            scanf("%d", &bone[i].value);        for (i = 0; i < n; i++)            scanf("%d", &bone[i].volumn);        for (i = 0; i < n; i++)            for (j = vol; j >= 0; j--)                if (j >= bone[i].volumn)                    dp[j] = max(dp[j], dp[j - bone[i].volumn] + bone[i].value);        printf("%u\n", dp[vol]);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - HDU](/tags/Online-Judge-HDU/)[Dynamic Programming](/tags/Dynamic-Programming/)

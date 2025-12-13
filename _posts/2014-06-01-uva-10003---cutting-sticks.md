---
categories: Posts
date: 2014-06-01 00:00:00
title: UVa 10003 - Cutting Sticks
tags: []
layout: post
---

#  [UVa 10003 - Cutting Sticks](/2014/06/UVa-10003/ "UVa 10003 - Cutting Sticks")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jun 30 2014 16:22

**Contents**

  1. 1. 传送门
  2. 2. 思路
  3. 3. 代码

## 传送门

[UVa 10003 - Cutting Sticks](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=944)

## 思路

参考了**[wangtaoking1的解题报告](http://blog.csdn.net/wangtaoking1/article/details/7292093)**  
就是按照切点去切就行，然后返回最小值，输出TAT。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839

| 
    
    
    #include <cstdio>#include <cstring>#include <algorithm>using namespace std;const int MAXN = 50 + 10;const int INF = 2147483647;int num[MAXN];int dp[MAXN][MAXN];int DP(int i, int k){    int &ans = dp[i][k];    if (i + 1 == k)        return ans = 0;    if (ans != -1)        return ans;    ans = INF;    for (int j = i + 1; j < k; j++)        ans = min(ans, DP(i, j) + DP(j, k) + num[k] - num[i]);    return ans;}int main(){    //freopen("input.txt", "r", stdin);    int len, n, i, j;    while (scanf("%d", &len), len)    {        memset(dp, -1, sizeof(dp));        scanf("%d", &n);        for (i = 1; i <= n; i++)            scanf("%d", #[i]);        num[0] = 0, num[n + 1] = len;        int ans = DP(0, n + 1);        printf("The minimum cutting is %d.\n", ans);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Dynamic Programming](/tags/Dynamic-Programming/)

---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 10604 - Chemical Reaction
tags: []
layout: post
---

#  [UVa 10604 - Chemical Reaction](/2014/07/UVa-10604/ "UVa 10604 - Chemical Reaction")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jul 20 2014 20:18

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 10604 - Chemical Reaction](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=&problem=1545&mosmsg=Submission+received+with+ID+13913073)

## 题意

有N种化学剂，它们两两混合可以产生新的成分和热量，现在给出N个瓶子，要求计算它们混合产生的最少热量。

## 思路

用$dp[1][2][3][4][5][6]$表示六种试剂各有k瓶时能产生的最小热量。  
状态转移方程$dp[xxxxxx] = min(d[xxxxxx], dp[x - 1][y - 1][z + 1][xxx] + xy.heat)$，其中x、y是反应的两个试剂。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253

| 
    
    
    #include <bits/stdc++.h>using namespace std;const int INF = 0x3f3f3f3f;const int MAXN = 40 + 5; int dp[MAXN][MAXN][MAXN][MAXN], mp[MAXN][4], vis[25], layer[5], n; int DFS(int cnt){    int &cur = dp[layer[0]][layer[1]][layer[2]][layer[3]];    if (cnt == 5)        return cur = 0;    if (cur != -1)        return cur;    cur = 0;    for (int i = 0; i < 4; i++)    {        if (layer[i] == n)            continue;        int temp = mp[layer[i]++][i];        if (vis[temp])        {            vis[temp] = 0;            cur = max(cur, DFS(cnt - 1) + 1);            vis[temp] = 1;        }        else        {            vis[temp] = 1;            cur = max(cur, DFS(cnt + 1));            vis[temp] = 0;        }        layer[i]--;    }    return cur;} int main(){    //freopen("input.txt", "r", stdin);    int i, j;    while (scanf("%d", &n), n)    {        memset(dp, -1, sizeof dp);        memset(vis, 0, sizeof vis);        memset(layer, 0, sizeof layer);        for (i = 0; i < n; i++)            for (j = 0; j < 4; j++)                scanf("%d", ∓[i][j]);        printf("%d\n", DFS(0));    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Dynamic Programming](/tags/Dynamic-Programming/)[Online Judge - UVa](/tags/Online-Judge-UVa/)

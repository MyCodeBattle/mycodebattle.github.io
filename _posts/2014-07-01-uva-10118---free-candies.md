---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 10118 - Free Candies
tags: []
layout: post
---

#  [UVa 10118 - Free Candies](/2014/07/UVa-10118/ "UVa 10118 - Free Candies")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jul 18 2014 16:58

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 10118 - Free Candies](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=114&problem=1059&mosmsg=Submission+received+with+ID+13902208)

## 题意

四堆糖果，每次可以从最上面拿一个放到篮子里，篮子里最多只能放五个。如果篮子里有两个一样的，你就可以拿出来放到自己的口袋里！  
求最多能拿到几对糖果。

## 思路

四堆糖果，可以开一个四维数组，表示每堆糖果拿了几个。然后就一层一层记忆化搜索吧。因为两两相消，所以可以开一个数组vis，如果存在的话ans + 1

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253

| 
    
    
    #include <bits/stdc++.h>using namespace std;const int INF = 0x3f3f3f3f;const int MAXN = 40 + 5;int dp[MAXN][MAXN][MAXN][MAXN], mp[MAXN][4], vis[25], layer[5], n;int DFS(int cnt)        //layer[i]表示第i堆糖果已经拿了几个{    int &cur = dp[layer[0]][layer[1]][layer[2]][layer[3]];    if (cnt == 5)        return cur = 0;    if (cur != -1)        return cur;    cur = 0;    for (int i = 0; i < 4; i++)    {        if (layer[i] == n)            continue;        int temp = mp[layer[i]++][i];        if (vis[temp])        {            vis[temp] = 0;            cur = max(cur, DFS(cnt - 1) + 1);            vis[temp] = 1;        }        else        {            vis[temp] = 1;            cur = max(cur, DFS(cnt + 1));            vis[temp] = 0;        }        layer[i]--;    }    return cur;}int main(){    //freopen("input.txt", "r", stdin);    int i, j;    while (scanf("%d", &n), n)    {        memset(dp, -1, sizeof dp);        memset(vis, 0, sizeof vis);        memset(layer, 0, sizeof layer);        for (i = 0; i < n; i++)            for (j = 0; j < 4; j++)                scanf("%d", ∓[i][j]);        printf("%d\n", DFS(0));    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Dynamic Programming](/tags/Dynamic-Programming/)[Online Judge - UVa](/tags/Online-Judge-UVa/)

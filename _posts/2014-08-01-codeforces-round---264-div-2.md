---
categories: Posts
date: 2014-08-01 00:00:00
title: Codeforces Round - 264 (Div. 2)
tags: []
layout: post
---

## C. Gargari and Bishops

### 题意

选出两个位置，它们的主副对角线之和最大，选过的位置不能重复。

### 思路

和八皇后问题差不多。i + j和i - j可以表示出在同一斜线上的数字。在读取输入的同时求和。

不能选重复的关键是选(i + j) & 1和是偶数的就行。

### 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647

| ```c++
#include <bits/stdc++.h>#define LL long long#define lowbit(x) ((x) & (-x))const int MAXN = 2000 + 5;const int INF = 0x3f3f3f3f;using namespace std; LL mp[MAXN][MAXN], sum[MAXN * 4]; int main(){    //freopen("input.txt", "r", stdin);    int n, i, j;    scanf("%d", &n);    for (i = 1; i <= n; i++)        for (j = 1; j <= n; j++)        {            scanf("%lld", ∓[i][j]);            sum[i + j] += mp[i][j], sum[i - j + 3*n] += mp[i][j];        }    LL fans = -1, sans = -1;    int frow, fcol, srow, scol;    for (i = 1; i <= n; i++)        for (j = 1; j <= n; j++)        {            LL t = sum[i + j] + sum[i - j + 3*n] - mp[i][j];            if ((i + j) & 1)            {                if (fans < t)                {                    fans = t;                    frow = i, fcol = j;                }            }            else            {                if (sans < t)                {                    sans = t;                    srow = i, scol = j;                }            }        }    printf("%I64d\n", fans + sans);    printf("%d %d %d %d\n", frow, fcol, srow, scol);    return 0;}
```  

## D. Gargari and Permutations

### 题意

求一些排列的最长公共子序列。

### 思路

参考了别人的思路。可以转化为DAG，然后求最长路！真是奇妙。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970

| ```c++
#include <bits/stdc++.h>#define LL long long#define lowbit(x) ((x) & (-x))const int MAXN = 1000 + 5;const int INF = 0x3f3f3f3f;using namespace std; int ans = 0, pos[6][MAXN], n, k, d[MAXN], vis[MAXN];vector<int> mp[MAXN]; bool Check(int a, int b)    //check if a is behind b{    for (int i = 0; i < k; i++)        if (pos[i][a] > pos[i][b])            return false;    return true;} void SPFA(){    queue<int> qu;    qu.push(0);    while (!qu.empty())    {        int t = qu.front();        qu.pop();        vis[t] = 0;        for (int i = 0; i < mp[t].size(); i++)        {            int u = mp[t][i];            if (d[u] < d[t] + 1)            {                d[u] = d[t] + 1;                ans = max(ans, d[u]);                if (!vis[u])                {                    vis[u] = 1;                    qu.push(u);                }            }        }    }} int main(){    //freopen("input.txt", "r", stdin);    int i, j, temp;    scanf("%d%d", &n, &k);    for (i = 0; i < k; i++)        for (j = 0; j < n; j++)        {            scanf("%d", &temp);            pos[i][temp] = j;        }    for (i = 1; i <= n; i++)    {        mp[0].push_back(i);        for (j = i + 1; j <= n; j++)        {            if (Check(i, j))                mp[i].push_back(j);            else if (Check(j, i))                mp[j].push_back(i);        }    }    SPFA();    printf("%d\n", ans);    return 0;}
```
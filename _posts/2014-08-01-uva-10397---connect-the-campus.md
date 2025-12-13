---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 10397 - Connect the Campus
tags: []
layout: post
---

#  [UVa 10397 - Connect the Campus](/2014/08/UVa-10397/ "UVa 10397 - Connect the Campus")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Aug 12 2014 21:18

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 10397 - Connect the Campus](http://vjudge.net/problem/viewProblem.action?id=22163)

## 题意

学校要联网，已经有一些楼之间有电缆了，求权值的最小和.

## 思路

MST。只要把已经给出的楼的权值变为0即可。

在Find函数里忘了把查找过的结点变为根的儿子，完全一样的思路，愣是和别人差了200ms，提交了二十来次才发现（ ＴДＴ），不过这也让我熟悉了Kruskal。。。

Prim算法做这题可以达到50ms，马上去看看（๑•̀ㅂ•́)و✧

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768697071

| 
    
    
    #include <bits/stdc++.h>using namespace std;#define LL long longconst int EMAXN = 3e5;const int DMAXN = 800; struct POINT{    int x, y;}pit[DMAXN]; double dis[EMAXN], ans;int u[EMAXN], v[EMAXN], r[EMAXN], p[DMAXN], mp[DMAXN][DMAXN];int ncable, n, nbuild; int cmp(const int i, const int j){    return dis[i] < dis[j];} int Find(int x){    return p[x] == x ? x : (p[x] = Find(p[x]));} void Kruscal(){    int i, j;    sort(r, r + n, cmp);    for (int i = 0; i < n; i++)    {        int e = r[i];        int x = Find(u[e]), y = Find(v[e]);        if (x != y)            ans += dis[e], p[x] = y;    }} int main(){    //freopen("input.txt", "r", stdin);    int i, j, a, b;    while (~scanf("%d", &nbuild))    {        memset(mp, 0, sizeof mp);        n = 0, ans = 0;        for (i = 1; i <= nbuild; i++)        {            p[i] = i;            scanf("%d%d", &pit[i].x, &pit[i].y);        }        scanf("%d", &ncable);        for (i = 0; i < ncable; i++)        {            scanf("%d%d", &a, &b);            mp[a][b] = mp[b][a] = 1;        }        for (i = 1; i <= nbuild; i++)            for (j = i + 1; j <= nbuild; j++)            {                u[n] = i, v[n] = j, r[n] = n;                if (mp[i][j])                    dis[n++] = 0;                else                    dis[n++] = hypot(pit[i].x - pit[j].x, pit[i].y - pit[j].y);            }        Kruscal();        printf("%.2f\n", ans);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Data Structure - Graph](/tags/Data-Structure-Graph/)[Online Judge - UVa](/tags/Online-Judge-UVa/)[Data Structure - MST](/tags/Data-Structure-MST/)

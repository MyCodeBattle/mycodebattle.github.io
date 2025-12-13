---
categories: Posts
date: 2014-09-01 00:00:00
title: UVa 10917 - Walk Through the Forest
tags: []
layout: post
---

#  [UVa 10917 - Walk Through the Forest](/2014/09/UVa-10917/ "UVa 10917 - Walk Through the Forest")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 14 2014 11:27

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 10917 - Walk Through the Forest](http://www.bnuoj.com/v3/problem_show.php?pid=19335)

## 题意

小明要从办公室回家，当从A到家里存在一条路比B到家的任何一条路都短的话，就走A。问他有几种走法。

## 思路

意思就是A到终点的最短路比B的最短路短的时候可以走A。

先对终点进行一次Dijkstra，求出每个点到终点的距离，然后DFS。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768697071

| 
    
    
    #include<bits/stdc++.h>#define LL long long#define lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)const int MAXN = 1000 + 5;const int INF = 0x3f3f3f3f;using namespace std; typedef pair<int, int> pii;typedef vector<int> vei;typedef vector<pair<int, int> >veii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii;typedef priority_queue<pii, vector<pii>, greater<pii> >pquii; pquii pqu;int dis[MAXN], dp[MAXN];veii mp[MAXN]; void Dijkstra(){    memset(dis, INF, sizeof dis);    dis[2] = 0;    pqu.push(MP(dis[2], 2));    while (!pqu.empty())    {        pii u = pqu.top(); pqu.pop();        int x = u.second;        if (dis[x] != u.first) continue;        for (vitii it = mp[x].begin(); it != mp[x].end(); it++)        {            int a = it->first, b = it->second;            if (dis[a] > dis[x] + b)            {                dis[a] = dis[x] + b;                pqu.push(MP(dis[a], a));            }        }    }} int DFS(int x){    if (dp[x] != -1) return dp[x];    if (x == 2) return 1;    int sum = 0;    for (vitii it = mp[x].begin(); it != mp[x].end(); it++)        if (dis[it->first] < dis[x]) sum += DFS(it->first);    return dp[x] = sum;} int main(){    //freopen("input.txt", "r", stdin);    int nroad, njit, i, j;    while (scanf("%d", &njit), njit)    {        scanf("%d", &nroad);        for (i = 0; i <= njit; i++) mp[i].clear();        for (i = 0; i < nroad; i++)        {            int a, b, c;            scanf("%d%d%d", &a, &b, &c);            mp[a].push_back(MP(b, c)); mp[b].push_back(MP(a, c));        }        Dijkstra();        memset(dp, -1, sizeof dp);        printf("%d\n", DFS(1));    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Algorithm - Shortest Path](/tags/Algorithm-Shortest-Path/)

---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 10986 - Sending email
tags: []
layout: post
---

#  [UVa 10986 - Sending email](/2014/08/UVa-10986/ "UVa 10986 - Sending email")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Aug 15 2014 0:24

**Contents**

  1. 1. 传送门
  2. 2. 思路
  3. 3. 代码

## 传送门

[UVa 10986 - Sending email](http://vjudge.net/problem/viewProblem.action?id=24941)

## 思路

一般的Dijkstra。不过因为n太大了，所以要用邻接链表存。存的时候要记得两边都要存，因为是无向图，这时候就要开两倍的空间。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566

| 
    
    
    #include <bits/stdc++.h>using namespace std;#define LL long longconst int EMAXN = 1e5 + 100;const int VMAXN = 2e4 + 100;const int INF = 0x3f3f3f3f; int head[VMAXN], d[VMAXN];int next[EMAXN], u[EMAXN], v[EMAXN], w[EMAXN];typedef pair<int, int> pii;priority_queue<pii, vector<pii>, greater<pii> >q; void Dijkstra(int st){    int i, j;    for (i = 0; i < VMAXN; i++)        d[i] = INF;    d[st] = 0;    q.push(make_pair(d[st], st));    while (!q.empty())    {        pii u = q.top();        q.pop();        int x = u.second;        if (u.first != d[x])            continue;        for (int e = head[x]; e != -1; e = next[e])        {            if (d[v[e]] > d[x] + w[e])            {                d[v[e]] = d[x] + w[e];                q.push(make_pair(d[v[e]], v[e]));            }        }    }}  int main(){    //freopen("input.txt", "r", stdin);    int T, i, j, a, b, c, m, st, ed, n, cases = 0;    scanf("%d", &T);    while (T--)    {        int k = 0;        scanf("%d%d%d%d", &n, &m, &st, &ed);        memset(head, -1, sizeof head);        for (i = 0; i < m; i++)        {            scanf("%d%d%d", &a, &b, &c);            u[k] = a, v[k] = b, w[k] = c;            next[k] = head[u[k]];            head[u[k]] = k;            k++;            u[k] = b, v[k] = a, w[k] = c;            next[k] = head[u[k]];            head[u[k]] = k;            k++;        }        Dijkstra(st);        printf("Case #%d: ", ++cases);        d[ed] == INF ? printf("unreachable\n") : printf("%d\n", d[ed]);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Algorithm - Shortest Path](/tags/Algorithm-Shortest-Path/)[Online Judge - UVa](/tags/Online-Judge-UVa/)[Must Be Done Again](/tags/Must-Be-Done-Again/)

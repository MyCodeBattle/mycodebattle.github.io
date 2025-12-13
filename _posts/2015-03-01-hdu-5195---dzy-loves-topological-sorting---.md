---
categories: Posts
date: 2015-03-01 00:00:00
title: HDU 5195 - DZY Loves Topological Sorting (贪心 + 拓扑排序)
tags: []
layout: post
---

#  [HDU 5195 - DZY Loves Topological Sorting (贪心 + 拓扑排序)](/2015/03/HDU-5195/ "HDU 5195 - DZY Loves Topological Sorting \(贪心 + 拓扑排序\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Mar 29 2015 12:11

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

最多能删去k条边，求字典序最大的拓扑序列。

## 思路

选出$deg(i) <= k$的最大标号，然后删去他的所有边。这样得出的字典序肯定是最大的。  
用优先队列维护。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445

| 
    
    
    int vis[MAXN], in[MAXN];vector<int> ans, G[MAXN]; int main(){    //ROP;    int n, m, k;    while (~scanf("%d%d%d", &n, &m, &k))    {        ans.clear();        MS(vis, 0);        for (int i = 1; i <= n; i++) G[i].clear();        for (int i = 0; i < m; i++)        {            int a, b;            scanf("%d%d", &a, &b);            G[a].PB(b);            in[b]++;        }        priority_queue<int> Q;        for (int i = 1; i <= n; i++)            if (in[i] <= k) Q.push(i);        while (!Q.empty())        {            int u = Q.top(); Q.pop();            if (!vis[u] && in[u] <= k)            {                k -= in[u];                in[u] = 0;                vis[u] = 1;            }            else continue;            for (int i = 0; i < SZ(G[u]); i++)            {                int v = G[u][i];                in[v]--;                if (in[v] <= k) Q.push(v);            }            ans.PB(u);        }        for (int i = 0; i < SZ(ans); i++)            printf("%d%c", ans[i], i!=SZ(ans)-1 ? ' ' : '\n');    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - HDU](/tags/Online-Judge-HDU/)[Foundation - Greedy](/tags/Foundation-Greedy/)[Algorithm - Toposort](/tags/Algorithm-Toposort/)

---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 558 - Wormholes
tags: []
layout: post
---

## 传送门

[UVa 558 - Wormholes](http://vjudge.net/problem/viewProblem.action?id=20843)

## 题意

有个科学家想回到Big Bang时代，现在有若干个虫洞，有些可以回到过去，问他能不能实现。

## 思路

如果能找到一个负回路，就说明科学家可以成功。

如何判断负回路存在？如果是用FIFO队列优化的Bellman算法，一个点的入队次数超过n就存在负回路。

如果是Bellman算法，在进行完n-1轮后，再对每条边判断一下，加入这条边是否会使得顶点v的最短路再缩短。

## 代码


```c++
#include <bits/stdc++.h>
using namespace std;
#define LL long long
const int EMAXN = 2e3 + 100;
const int VMAXN = 1e3 + 100;
const int INF = 0x3f3f3f3f;
 
int head[VMAXN], n, m, vis[VMAXN], cnt[VMAXN];
int next[EMAXN], u[EMAXN], v[EMAXN], w[EMAXN], d[EMAXN];
 
int SPFA(int st)
{
    memset(vis, 0, sizeof vis);
    memset(cnt, 0, sizeof cnt);
    queue<int> qu;
    for (int i = 0; i < n; i++)
        d[i] = INF;
    d[st] = 0;
    cnt[st]++;
    qu.push(st);
    while (!qu.empty())
    {
        int t = qu.front();
        qu.pop();
        vis[t] = 0;
        for (int e = head[t]; e != -1; e = next[e])
            if (d[v[e]] > d[t] + w[e])
            {
                d[v[e]] = d[t] + w[e];
                if (!vis[v[e]])
                {
                    qu.push(v[e]), vis[v[e]] = 1;
                    if (++cnt[v[e]] == n)
                        return 1;
                }
            }
    }
    return 0;
}
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int T, i, j;
    scanf("%d", &T);
    while (T--)
    {
        memset(head, -1, sizeof head);
        scanf("%d%d", &n, &m);
        for (i = 0; i < m; i++)
        {
            scanf("%d%d%d", &u[i], &v[i], &w[i]);
            next[i] = head[u[i]];
            head[u[i]] = i;
        }
        printf("%s\n", SPFA(0) ? "possible" : "not possible");
    }
    return 0;
}
```
---
categories: Posts
date: 2014-09-01 00:00:00
title: UVa 11134 - Fabled Rooks
tags: []
layout: post
---

## 传送门

[UVa 11134 - Fabled Rooks](http://vjudge.net/problem/viewProblem.action?id=34086)

## 题意

在一个n*n的棋盘上放上n个车，每个车都有一个矩阵限制能放的地方。如果能放下去，输出每个车的坐标。

## 思路

对于每个棋子，可以先找它的横坐标，再找纵坐标。如果都能找到，这个棋子就能放下去。而横纵坐标的范围就是矩形的范围。

用优先队列维护当前点的横坐标最小。

因为每个位置必有一枚棋子，也就是取出来的旗子如果判断可以放下去的话就放，直到填满。

## 代码


```c++
#include <bits/stdc++.h>
#define LL long long
#define lowbit(x) ((x) & (-x))
const int MAXN = 5000 + 5;
const int INF = 0x3f3f3f3f;
using namespace std;
 
struct POINT
{
    int id, l, r;
    bool operator < (const POINT &a) const
    {
        if (l != a.l)
            return l > a.l;
        else
            return r > a.r;
    }
}rpit[MAXN], cpit[MAXN];
 
priority_queue<POINT> qu;
int n, ans[MAXN][2];
 
bool Check(POINT *arr, int pos)
{
    while (!qu.empty())
        qu.pop();
    for (int i = 0; i < n; i++)
        qu.push(arr[i]);
    int cnt = 1;
    while (!qu.empty())
    {
        POINT cur = qu.top(); qu.pop();
        if (cur.r < cnt || cur.l > cnt) return false;
        if (cur.l < cnt)
        {
            cur.l = cnt;
            qu.push(cur);
            continue;
        }
        ans[cur.id][pos] = cnt;
        cnt++;
    }
    return true;
}
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int i, j;
    while (scanf("%d", &n), n)
    {
        for (i = 0; i < n; i++)
        {
            scanf("%d%d%d%d", &rpit[i].l, &cpit[i].l, &rpit[i].r, &cpit[i].r);
            rpit[i].id = cpit[i].id = i;
        }
        if (Check(rpit, 0) && Check(cpit, 1))
            for (i = 0; i < n; i++)
                printf("%d %d\n", ans[i][0], ans[i][1]);
        else
            puts("IMPOSSIBLE");
    }
    return 0;
}
```
---
categories: Posts
date: 2014-10-03 00:00:00
title: UVa 10330 - Power Transmission (最大流 & Edmonds - Karp)
tags: []
layout: post
---

## 题意

题目看了好久才懂。

有N个发电厂，每个发电厂容量为C，有K个目的地，也有容量。给出每个发电厂连接的路和路的容量，求最大能云的电。

## 思路

网络流第一题，惯例看代码。

建立超级源点和超级汇点，然后EK。

晚上还要仔细理解一下EK。

## 代码


```c++
#include <cstdio>
#include <stack>
#include <set>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <functional>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <ctime>
#include <cstdlib>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <cmath>
#define LL long long
#define SZ(x) (int)x.size()
#define Lowbit(x) ((x) & (-x))
#define MP(a, b) make_pair(a, b)
#define MS(arr, num) memset(arr, num, sizeof(arr))
#define PB push_back
#define F first
#define S second
#define ROP freopen("input.txt", "r", stdin);
#define MID(a, b) (a + ((b - a) >> 1))
#define LC rt << 1, l, mid
#define RC rt << 1|1, mid + 1, r
#define LRT rt << 1
#define RRT rt << 1|1
#define BitCount(x) __builtin_popcount(x)
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
using namespace std;
const int MAXN = 110 + 5;
const int MOD = 20071027;
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
int a[MAXN], flow[MAXN][MAXN], cap[MAXN][MAXN], num[MAXN], p[MAXN];
int f, n;
 
void EK()
{
    queue<int> qu;
    MS(flow, 0);
    f = 0;
    while (true)
    {
        MS(a, 0);
        a[0] = INF;
        qu.push(0);
        while (!qu.empty())
        {
            int u = qu.front(); qu.pop();
            for (int v = 0; v <= n + 1; v++)
            {
                if (!a[v] && cap[u][v] > flow[u][v])
                {
                    p[v] = u;
                    qu.push(v);
                    a[v] = min(a[u], cap[u][v] - flow[u][v]);
                }
            }
        }
        if (!a[n + 1]) break;
        for (int u = n + 1; u; u = p[u])
        {
            flow[p[u]][u] += a[n + 1];
            flow[u][p[u]] -= a[n + 1];
        }
        f += a[n + 1];
    }
}
 
int main()
{
    //ROP;
    int i, j, tmp;
    while (~scanf("%d", &n))
    {
        MS(cap, 0);
        for (i = 1; i <= n; i++) scanf("%d", #[i]);
        int _, a, b, c;
        scanf("%d", &_);
        while (_--)
        {
            scanf("%d%d%d", &a, &b, &c);
            cap[a][b] = min(c, min(num[a], num[b]));
        }
        int d;
        scanf("%d%d", &b, &d);
        while (b--)
        {
            scanf("%d", &tmp);
            cap[0][tmp] = num[tmp];
        }
        while (d--)
        {
            scanf("%d", &tmp);
            cap[tmp][n + 1] = num[tmp];
        }
        EK();
        printf("%d\n", f);
    }
    return 0;
}
```
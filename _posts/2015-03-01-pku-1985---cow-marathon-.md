---
categories: Posts
date: 2015-03-01 00:00:00
title: PKU 1985 - Cow Marathon (树的直径)
tags: []
layout: post
---

## 题意

求树上两点间最远距离。

## 思路

求树的直径。先求出任意一点到达的最远点，然后接着求出最远点。距离就是第二次的距离。

## 代码


```c++
#include <stack>
#include <cstdio>
#include <list>
#include <cassert>
#include <set>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <functional>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <string>
#include <map>
#include <cmath>
using namespace std;
#define LL long long
#define ULL unsigned long long
#define SZ(x) (int)x.size()
#define Lowbit(x) ((x) & (-x))
#define MP(a, b) make_pair(a, b)
#define MS(arr, num) memset(arr, num, sizeof(arr))
#define PB push_back
#define X first
#define Y second
#define ROP freopen("input.txt", "r", stdin);
#define MID(a, b) (a + ((b - a) >> 1))
#define LC rt << 1, l, mid
#define RC rt << 1|1, mid + 1, r
#define LRT rt << 1
#define RRT rt << 1|1
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
const double eps = 1e-9;
const int MAXN = 1e5 + 10;
const int MOD = 1e9 + 7;
const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };
int cases = 0;
typedef pair<int, int> pii;
 
int ans;
vector<pii> G[MAXN];
int vis[MAXN];
 
int get_futher(int st)
{
    ans = 0;
    int point = st;
    queue<pii> Q;
    Q.push(MP(st, 0));
    vis[st] = 1;
    while (!Q.empty())
    {
        pii cur = Q.front(); Q.pop();
        int x = cur.X, y = cur.Y;
        if (y > ans)
        {
            ans = y;
            point = x;
        }
        for (int i = 0; i < SZ(G[x]); i++)
        {
            if (vis[G[x][i].X]) continue;
            vis[G[x][i].X] = 1;
            Q.push(MP(G[x][i].X, y+G[x][i].Y));
        }
    }
    return point;
}
 
int main()
{
    //ROP;
    int n, k;
    while (~scanf("%d%d", &n, &k))
    {
        MS(vis, 0);
        for (int i = 0; i <= n; i++) G[i].clear();
        for (int i = 0; i < k; i++)
        {
            int a, b, c;
            char d;
            scanf("%d %d %d %c", &a, &b, &c, &d);
            G[a].PB(MP(b, c));
            G[b].PB(MP(a, c));
        }
        int point = get_futher(1);
        MS(vis, 0);
        get_futher(point);
        printf("%d\n", ans);
    }
    return 0;
}
```
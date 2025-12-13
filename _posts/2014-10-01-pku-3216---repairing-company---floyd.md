---
categories: Posts
date: 2014-10-01 00:00:00
title: PKU 3216 - Repairing Company (最小边覆盖 + Floyd)
tags: []
layout: post
---

## 题意

有N个生意，每个生意有所在街区，最后期限，花费时间，街区到街区之间也要时间。

问最少派出几个师傅，使得所有客户都满意。

## 思路

想了半天想不到这题和二分匹配有什么关系。竟然可以把能在一个街区之后赶到的另一个街区连线。。。

这建图方式我也是醉了。

然后求最小边覆盖

Floyd很久没写了，一写就错，调了俩小时。

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
#include <string>
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
const int MAXN = 500 + 10;
const int MOD = 1e9 + 7;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
struct TASK
{
    int blo, dead, cost;
}tsk[MAXN];
 
int ncity, mp[25][25];
 
void Floyd()
{
    for (int k = 1; k <= ncity; k++)
        for (int i = 1; i <= ncity; i++)
            if (mp[i][k] != INF)
                for (int j = 1; j <= ncity; j++)
                    mp[i][j] = min(mp[i][j], mp[i][k] + mp[k][j]);
}
 
struct EDGE
{
    int from, to;
};
 
struct BIMATCHING
{
    int link[MAXN], head[MAXN], next[MAXN * MAXN];
    bool vis[MAXN];
    vector<EDGE> edges;
    void init()
    {
        MS(link, -1); MS(head, -1);
        edges.clear();
    }
    void add_edge(int from, int to)
    {
        edges.PB((EDGE){from, to});
        int m = SZ(edges);
        next[m - 1] = head[from];
        head[from] = m - 1;
    }
 
    bool dfs(int u)
    {
        for (int i = head[u]; i != -1; i = next[i])
        {
            EDGE &e = edges[i];
            int v = e.to;
            if (!vis[v])
            {
                vis[v] = 1;
                if (link[v] == -1 || dfs(link[v]))
                {
                    link[v] = u;
                    return true;
                }
            }
        }
        return false;
    }
 
    int hungary(int n)  //n是待匹配的总数，这里默认从1开始
    {
        int res = 0;
        for (int i = 1; i <= n; i++)
        {
            MS(vis, 0);
            if (dfs(i)) res++;
        }
        return res;
    }
}hun;
 
int main()
{
    //ROP;
    int ntask, i, j;
    while (scanf("%d%d", &ncity, &ntask), ncity + ntask)
    {
        hun.init();
        for (i = 1; i <= ncity; i++)
        {
            for (j = 1; j <= ncity; j++)
            {
                int tmp;
                scanf("%d", &tmp);
                if (tmp == -1) tmp = INF;
                mp[i][j] = tmp;
            }
        }
        for (i = 1; i <= ntask; i++)
            scanf("%d%d%d", &tsk[i].blo, &tsk[i].dead, &tsk[i].cost);
        Floyd();
        for (i = 1; i <= ntask; i++)
            for (j = 1; j <= ntask; j++)
            {
                if (i != j)
                {
                    if (tsk[i].dead + tsk[i].cost + mp[tsk[i].blo][tsk[j].blo] <= tsk[j].dead)
                        hun.add_edge(i, j);
                }
            }
        printf("%d\n", ntask - hun.hungary(ntask));
    }
    return 0;
}
```
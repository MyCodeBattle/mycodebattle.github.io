---
categories: Posts
date: 2014-10-01 00:00:00
title: PKU 2239 - Selecting Courses (最大匹配 & Hungarian)
tags: []
layout: post
---

## 题意

有N个选修课，时间为周一到周日，1~12节课，现在要求选最多的课程。

左边是课程，右边是时间。时间可以表示成(nwek - 1) * 12。

最大匹配！

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
const int MAXN = 300 + 10;
const int MOD = 1e9 + 7;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
struct EDGE
{
    int from, to;
};
 
int vis[MAXN], head[MAXN], next[MAXN * MAXN], link[MAXN];
int ncourse;
vector<EDGE> edges;
 
bool DFS(int u)
{
    for (int i = head[u]; i != -1; i = next[i])
    {
        int &v = edges[i].to;
        if (!vis[v])
        {
            vis[v] = 1;
            if (link[v] == -1 || DFS(link[v]))
            {
                link[v] = edges[i].from;
                return true;
            }
        }
    }
    return false;
}
 
int Hungary()
{
    int res = 0;
    MS(link, -1);
    for (int u = 1; u <= ncourse; u++)
    {
        MS(vis, 0);
        if (DFS(u)) res++;
    }
    return res;
}
 
void AddEdge(int from, int to)
{
    edges.PB((EDGE){from, to});
    int m = SZ(edges);
    next[m - 1] = head[from];
    head[from] = m - 1;
}
 
int main()
{
    //ROP;
    int i, j;
    while (~scanf("%d", &ncourse))
    {
        MS(head, -1);
        edges.clear();
        int n;
        for (i = 1; i <= ncourse; i++)
        {
            scanf("%d", &n);
            while (n--)
            {
                int ncls, nwek;
                scanf("%d%d", &nwek, &ncls);
                int num = (nwek - 1) * 12 + ncls;
                AddEdge(i, num);
            }
        }
        printf("%d\n", Hungary());
    }
    return 0;
}
```
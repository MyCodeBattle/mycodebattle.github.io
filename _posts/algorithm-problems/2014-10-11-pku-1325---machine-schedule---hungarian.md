---
categories: Posts
date: 2014-10-11 00:00:00
title: PKU 1325 - Machine Schedule (最小点覆盖 & Hungarian)
tags: []
layout: post
---

## 题意

有一些工作可以在A机器上，也可以在B机器上，每个机器都有不同的模式，如果要切换模式就要重启。  
问最少的重启次数。

一开始想人和机器分别建边，后来捣鼓不出来。。其实只要机器之间建边就行了。。真是。。神奇。

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
const int MAXN = 1000 + 10;
const int MOD = 1e9 + 7;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
struct EDGE
{
    int from, to;
};
 
struct BIMATCHING
{
    int vis[MAXN], link[MAXN], head[MAXN], next[MAXN * MAXN];
    int nrem;
    vector<EDGE> edges;
 
    int DFS(int u)
    {
        for (int i = head[u]; i != -1; i = next[i])
        {
            int &v = edges[i].to;
            if (!vis[v])
            {
                vis[v] = 1;
                if (link[v] == -1 || DFS(link[v]))
                {
                    link[v] = u;
                    return 1;
                }
            }
        }
        return 0;
    }
 
    int hungary()
    {
        int res = 0;
        for (int i = 1; i <= nrem; i++)
        {
            MS(vis, 0);
            res += DFS(i);
        }
        return res;
    }
 
    void add_edge(int from, int to)
    {
        edges.PB((EDGE){from, to});
        int m = SZ(edges);
        next[m - 1] = head[from];
        head[from] = m - 1;
    }
 
    void init(int nrem)
    {
        this->nrem = nrem;
        MS(head, -1); MS(link, -1);
        edges.clear();
    }
}hun;
 
int main()
{
    //ROP;
    int n, m, _n, i, j;
    while (scanf("%d", &n), n)
    {
        hun.init(n);
        scanf("%d%d", &m, &_n);
        int k, b, a;
        while (_n--)
        {
            scanf("%d%d%d", &k, &a, &b);
            if (a != 0 && b != 0) hun.add_edge(a, b);
        }
        printf("%d\n", hun.hungary());
    }
    return 0;
}
```
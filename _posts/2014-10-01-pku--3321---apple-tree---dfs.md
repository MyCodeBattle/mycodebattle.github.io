---
categories: Posts
date: 2014-10-01 00:00:00
title: PKU  3321 - Apple Tree (树状数组 + DFS)
tags: []
layout: post
---

## 题意

有一颗苹果树，1是树根.

有两种操作

  1. 改变一个结点的值

  2. 统计这个结点以上（包括）的果实的个数。


## 思路

学习了时间戳。

就是在访问到一个结点的时候，放一个标记，等到递归结束的时候再放一个，这个范围就是他的子树的范围，然后用树状数组统计。真是。。太巧妙了。

这题的数组版邻接表和vector版相差也很大。

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
const int MAXN = 2e5 + 10;
const int MOD = 1e9 + 7;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
struct BIT
{
    int l, r, val;
}bit[MAXN];
 
struct EDGE
{
    int from, to;
};
 
int lev, C[MAXN], head[MAXN], next[MAXN], vis[MAXN];
 
vector<EDGE> edges;
 
void AddEdge(int from, int to)
{
    edges.PB((EDGE){from, to});
    int k = SZ(edges) - 1;
    next[k] = head[from];
    head[from] = k;
}
 
void DFS(int x)
{
    vis[x] = 1;
    bit[x].l = ++lev;
    for (int i = head[x]; i != -1; i = next[i])
        if (!vis[edges[i].to]) DFS(edges[i].to);
    bit[x].r = lev;
}
 
void Update(int x, int k)
{
    for (int i = x; i <= lev; i += Lowbit(i))
        if (!k) C[i]--;
        else C[i]++;
}
 
int Query(int x)
{
    int sum = 0;
    while (x > 0)
    {
        sum += C[x];
        x -= Lowbit(x);
    }
    return sum;
}
 
int main()
{
    //ROP;
    int n, i, j;
    while (~scanf("%d", &n))
    {
        MS(head, -1); MS(C, 0); MS(vis, 0);
        lev = 0;
        for (i = 1; i <= n - 1; i++)
        {
            int u, v;
            scanf("%d%d", &u, &v);
            AddEdge(u, v);
            AddEdge(v, u);
        }
        DFS(1);
        for (i = 1; i <= n; i++)
        {
            Update(bit[i].l, 1);
            bit[i].val = 1;
        }
        scanf("%d", &n);
        while (n--)
        {
            char str[3];
            int x;
            scanf("%s%d", str, &x);
            if (str[0] == 'Q') printf("%d\n", Query(bit[x].r) - Query(bit[x].l - 1));
            else
            {
                bit[x].val ^= 1;
                Update(bit[x].l, bit[x].val);
            }
        }
    }
    return 0;
}
```
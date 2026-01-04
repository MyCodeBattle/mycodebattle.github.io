---
categories: Posts
date: 2015-01-04 00:00:00
title: HDU 5154 - Harry and Magical Computer (并查集)
tags: []
layout: post
---

## 题意

二元组（a, b)表示b要在a之前做，给出几个二元组，问能不能做事情

## 思路

有向图判环。

本来以为并查集只能判无向图的，后来看了tj的代码学习了有向图的并查集判环。

原来（3， 3）这样是不行的，并查集返回值的时候顺序反了一下，调试了好久。

试了一下用强连通判环，只比并查集慢了一丢丢。

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
#include <iomanip>
#include <cmath>
#define LL long long
#define ULL unsigned long long
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
#define BitCountll(x) __builtin_popcountll(x)
#define LeftPos(x) 32 - __builtin_clz(x) - 1
#define LeftPosll(x) 64 - __builtin_clzll(x) - 1
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
using namespace std;
const double eps = 1e-8;
const int MAXN = 100 + 10;
const int MOD = 1000007;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
int p[MAXN];
 
bool Find(int u, int v)
{
    if (p[u] == v) return true;
    if (p[u] == u) return false;
    Find(p[u], v);
}
 
int main()
{
    //ROP;
    int n, m, i, j;
    while (~scanf("%d%d", &n, &m))
    {
        bool flag = false;
        for (i = 1; i <= n; i++) p[i] = i;
        for (i = 0; i < m; i++)
        {
            int a, b;
            scanf("%d%d", &a, &b);
            if (Find(b, a)) flag = true;
            else p[a] = b;
        }
        printf("%s\n", flag ? "NO": "YES");
    }
    return 0;
}
```
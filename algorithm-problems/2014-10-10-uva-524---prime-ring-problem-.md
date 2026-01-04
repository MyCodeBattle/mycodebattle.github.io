---
categories: Posts
date: 2014-10-10 00:00:00
title: UVa 524 - Prime Ring Problem (回溯)
tags: []
layout: post
---

## 思路

回溯法的简单应用。

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
 
int vis[20], ans[20], n;
 
bool Check(int n)
{
    for (int i = 2; i <= (int)sqrt(n + 0.5); i++)
    {
        if (n % i == 0) return false;
    }
    return true;
}
 
void DFS(int pos)
{
 
    if (pos == n + 1)
    {
        for (int i = 1; i <= n; i++)
            if (i != n) printf("%d ", ans[i]);
            else printf("%d\n", ans[i]);
        return;
    }
 
    for (int i = 1; i <= n; i++)
    {
        if (!vis[i] && Check(i + ans[pos - 1]))
        {
            if (pos == n)
                if (!Check(1 + i)) continue;
            vis[i] = 1;
            ans[pos] = i;
            DFS(pos + 1);
            vis[i] = 0;
        }
    }
}
 
int main()
{
    int i, j, cases = 0;
    while (~scanf("%d", &n))
    {
        if (cases) puts("");
        MS(vis, 0);
        ans[1] = 1, vis[1] = 1;
        printf("Case %d:\n", ++cases);
        DFS(2);
    }
    return 0;
}
```
---
categories: Posts
date: 2014-12-01 00:00:00
title: Codeforces 500C - New Year Book Reading (贪心)
tags: []
layout: post
---

## 题意

问按照顺序拿书，最少所需搬运的重量是多少。

## 思路

昨晚想了一个多小时，想得凌乱了。

对于每个要借的书，只要把它前面的重量加一遍就行，直到再一次碰到自己。

现在还是似懂非懂的状态。。。

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
const int MAXN = 1100 + 10;
const int MOD = 1000007;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
int w[MAXN], brow[MAXN], vis[MAXN];
 
int main()
{
    //ROP;
    int n, m, i, j;
    scanf("%d%d", &n, &m);
    for (i = 1; i <= n; i++) scanf("%d", &w[i]);
    for (i = 1; i <= m; i++) scanf("%d", &brow[i]);
    int ans = 0;
    for (i = 1; i <= m; i++)
    {
        MS(vis, 0);
        for (j = i - 1; j > 0; j--)
        {
            if (brow[i] == brow[j]) break;
            if (!vis[brow[j]])
            {
                vis[brow[j]] = 1;
                ans += w[brow[j]];
            }
        }
    }
    printf("%d\n", ans);
    return 0;
}
```
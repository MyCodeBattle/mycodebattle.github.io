---
categories: Posts
date: 2014-11-01 00:00:00
title: Codeforces 489B - BerSU Ball (乱搞)
tags: []
layout: post
---

## 题意

只有技能值相差最多1的人才能成为一队，求最多几队。

## 思路

一开始先是想到二分匹配的，但是想想B题不太可能用到。然后看到数据这么小，直接$O(n^2)$乱搞吧。

排个序，能和前面的配对就配。

好像还可以用LCS做，不过复杂度还是一样。

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
const int MAXN = 3000 + 10;
const int MOD = 1000007;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };  //0123£¬ÉÏÏÂ×óÓÒ
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
int boy[MAXN], girl[MAXN], vis[MAXN];
 
int main()
{
    //ROP;
    int m, n, i, j;
    int ans = 0;
    scanf("%d", &m);
    for (i = 0; i < m; i++) scanf("%d", &boy[i]);
    scanf("%d", &n);
    for (i = 0; i < n; i++) scanf("%d", &girl[i]);
    sort(boy, boy + m); sort(girl, girl + n);
    for (i = 0; i < m; i++)
        for (j = 0; j < n; j++)
        {
            if (!vis[j] && abs(boy[i] - girl[j]) <= 1)
            {
                vis[j] = 1;
                ans++;
                break;
            }
        }
    printf("%d\n", ans);
    return 0;
}
```
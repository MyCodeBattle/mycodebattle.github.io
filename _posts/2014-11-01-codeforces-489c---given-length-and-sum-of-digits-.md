---
categories: Posts
date: 2014-11-01 00:00:00
title: Codeforces 489C - Given Length and Sum of Digits... (贪心)
tags: []
layout: post
---

## 题意

构造m位和为sum的最小和最大的数。

## 思路

一开始用了DFS，果断跪了。

贪心一下，如果要求最大的数，能填9的就填9，不够的补0，对于最小的数，先在第一位填1，然后从后面开始填9，不够补0，如果到了第一位有多的就全部加上去。

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
const int MAXN = 1000 + 10;
const int MOD = 1000007;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
int minAns[MAXN], maxAns[MAXN];
 
int main()
{
    int m, sum, i, j;
    scanf("%d%d", &m, ∑);
    int leave = sum;
    if (m == 1 && sum == 0)
    {
        puts("0 0");
        return 0;
    }
    if (9 * m < sum || sum == 0)
    {
        puts("-1 -1");
        return 0;
    }
    minAns[0] = 1;
    leave--;
    for (int i = m - 1; i > 0; i--)
    {
        if (leave <= 9)
        {
            minAns[i] = leave;
            leave = 0;
        }
        else
        {
            minAns[i] = 9;
            leave -= 9;
        }
    }
    minAns[0] += leave;
    leave = sum;
    for (int i = 0; i < m; i++)
    {
        if (leave <= 9)
        {
            maxAns[i] = leave;
            leave = 0;
        }
        else
        {
            maxAns[i] = 9;
            leave -= 9;
        }
    }
    for (i = 0; i < m; i++) printf("%d", minAns[i]);
    printf(" ");
    for (i = 0; i < m; i++) printf("%d", maxAns[i]);
    return 0;
}
```
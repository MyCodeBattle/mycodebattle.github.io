---
categories: Posts
date: 2014-11-01 00:00:00
title: UVa 1523 - Helicopter (暴力)
tags: []
layout: post
---

## 题意

给一个公式，求这个公式的最小值。

公式的计算方法是sqrt（每个座位到中心的横向距离的和）^2 + （到中心的纵向距离的和）^2。

## 思路

题目看得蛋疼。

看懂题目你就赢了。

看着数据才8，就用全排列乱搞了。不过竟然跑了1.5s

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
 
int wei[10];
 
int main()
{
    //ROP;
    int i, j;
    while (true)
    {
        double ans = INF;
        int jug = 0;
        for (i = 1; i <= 8; i++)
        {
            scanf("%d", &wei[i]);
            jug += wei[i];
        }
        if (jug == 0) break;
        sort(wei + 1, wei + 9);
        do
        {
            double TraSum = wei[1] + wei[4] + wei[6] - wei[3] - wei[5] - wei[8];
            double LongSum = wei[1] - wei[6] + wei[2] - wei[7] + wei[3] - wei[8];
            double tmp = hypot(TraSum, LongSum);
            ans = min(ans, tmp);
        }while (next_permutation(wei + 1, wei + 9));
        printf("%.3f\n", ans);
    }
    return 0;
}
```
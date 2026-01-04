---
categories: Posts
date: 2015-01-11 00:00:00
title: UVa 11387 - The 3-Regular Graph (构造)
tags: []
layout: post
---

## 题意

问能否找到一个图，使得所有点的度为3.如果能就输出。

## 思路

离散数学没白学了。

如果点为奇数则不能。

一开始用set + map模拟，搞了半天搞不出来。

## 代码


```c++
#include <cstdio>
#include <stack>
#include <list>
#include <set>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <functional>
#include <cstring>
#include <iomanip>
#include <algorithm>
#include <cctype>
#include <string>
#include <map>
#include <cmath>
using namespace std;
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
const double eps = 1e-8;
const int MAXN = 1000 + 10;
const int MOD = 1000007;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
map<int, int> mp;
set<pii> st;
 
int main()
{
    //ROP;
    int n, i, j;
    while (scanf("%d", &n), n)
    {
        if ((n&1) || n < 4)
        {
            puts("Impossible");
            continue;
        }
        printf("%d\n", n * 3 / 2);
        for (i = 1; i < (n>>1); i++)
        {
            printf("%d %d\n", i, i + 1);
            printf("%d %d\n", i, i + (n>>1));
        }
        while (i < n)
        {
            printf("%d %d\n", i, i + 1);
            i++;
        }
        printf("%d %d\n", 1, n);
        printf("%d %d\n", (n>>1), n);
    }
    return 0;
}
```
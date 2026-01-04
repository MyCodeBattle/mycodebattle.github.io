---
categories: Posts
date: 2015-01-11 00:00:00
title: UVa 11269 - Setting Problems (贪心)
tags: []
layout: post
---

## 题意

一个人出题，一个人验题，求最短时间。

## 思路

仰慕柯神。

拿出两个事件a、b。

分别计算出a前b后、a后b前的时间。

a前b后：a.st + max(a.chk, b.st) + b.chk  
a后b前：b.st + max(b.chk, a.st) + a.chk

取小的，sort一下。

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
struct POINT
{
    int st, chk;
    bool operator < (const POINT &a) const
    {
        return st + max(a.st, chk) + a.chk < a.st + max(a.chk, st) + chk;
    }
}arr[MAXN];
 
int main()
{
    //ROP;
    int n, i, j;
    while (~scanf("%d", &n))
    {
        for (i = 0; i < n; i++) scanf("%d", &arr[i].st);
        for (i = 0; i < n; i++) scanf("%d", &arr[i].chk);
        sort(arr, arr + n);
        int ans = 0, tmp = 0;
        for (i = 0; i < n; i++)
        {
            tmp += arr[i].st;
            ans = (tmp > ans ? tmp + arr[i].chk : ans + arr[i].chk);
        }
        printf("%d\n", ans);
    }
    return 0;
}
```
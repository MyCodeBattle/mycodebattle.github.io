---
categories: Posts
date: 2014-12-01 00:00:00
title: UVa 1374 - Power Calculus (DFSID)
tags: []
layout: post
---

## 题意

问凑成$x^n$最少需要几次

## 思路

好像前面也有一道类似的。用DFSID就行。也可以打表交

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
const double eps = 1e-6;
const int MAXN = 1100 + 10;
const int MOD = 1000007;
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
int n, arr[MAXN], depth;
 
bool DFSID(int curDep)
{
    int pre = arr[curDep - 1];
    if (curDep == depth)
    {
        if (pre == n) return true;
        return false;
    }
    if (pre << (depth - curDep) < n) return false;
    for (int i = 0; i < curDep; i++)
    {
        arr[curDep] = pre + arr[i];
        if (arr[curDep] <= 1000 && DFSID(curDep + 1)) return true;
        arr[curDep] = pre - arr[i];
        if (arr[curDep] > 0 && DFSID(curDep + 1)) return true;
    }
    return false;
}
 
int main()
{
   // ROP;
    int i, j;
    while (scanf("%d", &n), n)
    {
        arr[0] = 1;
        depth = 1;
        while (!DFSID(1)) depth++;
        printf("%d\n", depth - 1);
    }
    return 0;
}
```
---
categories: Posts
date: 2015-01-01 00:00:00
title: UVa 10624 - Super Number (DFS)
tags: []
layout: post
---

## 题意

给出n、m，要求输出一个数，前i位能整除i，n <= i <= m。

## 思路

直接DFS。然后可以打表，2900MS，吓得我飞起来了

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
const int MAXN = 100 + 10;
const int MOD = 1000007;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
int num[MAXN], n, m;
bool flag;
 
bool Judge(int k)
{
    int ans = 0;
    for (int i = 1; i <= k; i++) ans = (ans * 10 + num[i]) % k;
    return (ans % k == 0);
}
 
void DFS(int curPos)
{
    if (curPos == m + 1)
    {
        for (int i = 1; i <= m; i++) printf("%d", num[i]);
        puts("");
        flag = true;
        return;
    }
    for (int i = 0; i < 10; i++)
    {
        if (flag) return;
        if (curPos == 1 && i == 0) continue;
        num[curPos] = i;
        if (curPos < n || Judge(curPos)) DFS(curPos + 1);
    }
}
 
int main()
{
    //ROP;
    int T, i, j, cases = 0;
    scanf("%d", &T);
    while (T--)
    {
        printf("Case %d: ", ++cases);
        flag = false;
        scanf("%d%d", &n, &m);
        DFS(1);
        if (!flag) puts("-1");
    }
    return 0;
}
```
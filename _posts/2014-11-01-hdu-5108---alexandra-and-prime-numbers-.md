---
categories: Posts
date: 2014-11-01 00:00:00
title: HDU 5108 - Alexandra and Prime Numbers (暴力)
tags: []
layout: post
---

## 题意

找出一个尽量小的数，使得M / N为素数

## 思路

枚举一下因数就行。做的时候不知道怎么脑子秀逗了，去分解质因数，然后从小到大乘起来TAT

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
const int MAXN = 1e9 + 10;
const int MOD = 1000007;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
bool Check(int n)
{
    for (int i = 2; i * i <= n; i++)
        if (n % i == 0) return false;
    return true;
}
 
int main()
{
    int n, i, j;
    while (~scanf("%d", &n))
    {
        if (n == 1)
        {
            puts("0");
            continue;
        }
        int ans = INF;
        for (int i = 1; i * i <= n; i++)
        {
            if (n % i == 0)
            {
                if (Check(n / i)) ans = min(ans, i);
                if (Check(i)) ans = min(ans, n / i);
            }
        }
        printf("%d\n", ans == INF ? 0 : ans);
    }
    return 0;
}
```
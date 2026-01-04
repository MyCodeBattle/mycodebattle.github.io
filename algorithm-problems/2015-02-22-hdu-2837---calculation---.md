---
categories: Posts
date: 2015-02-22 00:00:00
title: HDU 2837 - Calculation (计算指数 + 欧拉函数)
tags: []
layout: post
---

## 题意

计算$F(n) = (n \mod 10)^{F(n/10)} \bmod m$

## 思路

用$\phi$的那个公式计算。

因为要确保$b >= \phi(c)$，所以在计算幂取模的时候都加上了模，结果一定是大于模的。

## 代码


```c++
#include <stack>
#include <cstdio>
#include <list>
#include <cassert>
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
using namespace std;
#define LL long long
#define ULL unsigned long long
#define SZ(x) (int)x.size()
#define Lowbit(x) ((x) & (-x))
#define MP(a, b) make_pair(a, b)
#define MS(arr, num) memset(arr, num, sizeof(arr))
#define PB push_back
#define X first
#define Y second
#define ROP freopen("input.txt", "r", stdin);
#define MID(a, b) (a + ((b - a) >> 1))
#define LC rt << 1, l, mid
#define RC rt << 1|1, mid + 1, r
#define LRT rt << 1
#define RRT rt << 1|1
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
const double eps = 1e-8;
const int MAXN = 1e7 + 2;
const int MOD = 1e9 + 7;
const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };
int cases = 0;
typedef pair<int, int> pii;
 
LL get_phi(int n)
{
    int m = (int)sqrt(n+0.5);
    int ans = n;
    for (int i = 2; i <= m; i++) if (n % i == 0)
    {
        ans = ans / i * (i-1);
        while (n % i == 0) n /= i;
    }
    if (n > 1) ans = ans / n * (n-1);
    return ans;
}
 
LL PowMod(LL a, LL m, LL n)
{
    LL ret = 1;
    while (m)
    {
        if (m & 1)
        {
            ret = ret * a;
            if (ret > n) ret = ret % n + n;
        }
        a = a*a;
        if (a > n) a = a % n + n;
        m >>= 1;
    }
    return ret;
}
 
LL Fun(LL n, LL m)
{
    if (n < 10) return n;
    int euler = get_phi(m);
    LL a = Fun(n/10, euler);
    return PowMod(n%10, a, m);
}
 
int main()
{
    //ROP;
    int T;
    scanf("%d", &T);
    while (T--)
    {
        int n, m;
        scanf("%d%d", &n, &m);
        printf("%I64d\n", Fun(n, m) % m);
    }
    return 0;
}
​
```
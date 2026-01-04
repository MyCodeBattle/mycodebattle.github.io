---
categories: Posts
date: 2014-08-25 00:00:00
title: UVa 11078 - Open Credit System
tags: []
layout: post
---

## 传送门

[UVa 11078 - Open Credit System](http://www.bnuoj.com/v3/problem_show.php?pid=19496)

## 思路

维护ans的最大值和vmax的最大值。

## 代码


```c++
#include <bits/stdc++.h>
#define LL long long
#define lowbit(x) ((x) & (-x))
#define MP(a, b) make_pair(a, b)
using namespace std;
const int MAXN = 1e5 + 5;
const int INF = 0x3f3f3f3f;
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int T, i, j, n, a, fst, scd;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%d", &n);
        scanf("%d%d", &fst, &scd);
        int ans = fst - scd;
        int vmax;
        n -= 2;
        vmax = max(fst, scd);
        while (n--)
        {
            scanf("%d", &a);
            ans = max(ans, vmax - a);
            vmax = max(vmax, a);
        }
        printf("%d\n", ans);
    }
    return 0;
}
```
---
categories: Posts
date: 2014-07-26 00:00:00
title: UVa 106 - Fermat vs. Pythagoras
tags: []
layout: post
---

## 传送门

[UVa 106 - Fermat vs. Pythagoras](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=115&page=show_problem&problem=42)

## 思路

继续学习。

参考了[程序控的题解](http://www.cnblogs.com/devymex/archive/2010/08/07/1799713.html)

## 代码


```c++
#include <bits/stdc++.h>
using namespace std;
#define LL long long
const int MAXN = 1e6 + 100;
const int INF = 0x3f3f3f3f;
 
int vis[MAXN];
 
int GCD(int a, int b)
{
    return b == 0 ? a : GCD(b, a % b);
}
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int fcnt, scnt, i, j, n, x, y, z;
    while (~scanf("%d", &n))
    {
        memset(vis, 0, sizeof vis);
        fcnt = scnt = 0;
        int imax = (int)sqrt((double)n + 0.5);
        for (i = 1; i <= imax; i++)
        {
            for (j = i + 1; j <= imax; j += 2)
            {
                if (GCD(i, j) != 1)
                    continue;
                z = i * i + j * j;
                if (z > n)
                    break;
                x = 2 * i * j;
                y = j * j - i * i;
                fcnt++;
                for (int k = 1; z * k <= n; k++)
                    vis[k * x] = vis[k * y] = vis[k * z] = 1;
            }
        }
        for (i = 1; i <= n; i++)
            if (!vis[i])
                scnt++;
        printf("%d %d\n", fcnt, scnt);
    }
    return 0;
}
```
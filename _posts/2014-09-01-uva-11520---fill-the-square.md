---
categories: Posts
date: 2014-09-01 00:00:00
title: UVa 11520 - Fill the Square
tags: []
layout: post
---

## 传送门

[UVa 11520 - Fill the Square](http://www.bnuoj.com/v3/problem_show.php?pid=19938)

## 题意

给一个图填上英文，要求上下左右不能有相同的，字典序从左到右从上到下最小。

## 思路

暴力。

## 代码


```c++
#include <bits/stdc++.h>
#define LL long long
#define lowbit(x) ((x) & (-x))
const int MAXN = 10 + 5;
const int INF = 0x3f3f3f3f;
using namespace std;
 
char mp[MAXN][MAXN];
 
int main()
{
    //freopen("input.txt", "r", stdin);
    bool flag;
    int T, i, j, n, cases = 0;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%d%*c", &n);
        for (i = 0; i < n; i++)
            gets(mp[i]);
        for (i = 0; i < n; i++)
            for (j = 0; j < n; j++)
            {
                if (mp[i][j] == '.')
                {
                    for (char k = 'A'; k <= 'Z'; k++)
                    {
                        flag = true;
                        if (i > 0 && k == mp[i - 1][j]) flag = false;
                        if (i < n - 1 && k == mp[i + 1][j]) flag = false;
                        if (j > 0 && k == mp[i][j - 1]) flag = false;
                        if (j < n - 1 && k == mp[i][j + 1]) flag = false;
                        if (flag)
                        {
                            mp[i][j] = k;
                            break;
                        }
                    }
                }
            }
        printf("Case %d:\n", ++cases);
        for (i = 0; i < n; i++)
            puts(mp[i]);
    }
    return 0;
}
```
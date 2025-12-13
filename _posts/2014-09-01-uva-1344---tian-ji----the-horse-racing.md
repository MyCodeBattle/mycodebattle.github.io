---
categories: Posts
date: 2014-09-01 00:00:00
title: UVa 1344 - Tian Ji -- The Horse Racing
tags: []
layout: post
---

## 传送门

[UVa 1344 - Tian Ji — The Horse Racing](http://www.bnuoj.com/v3/problem_show.php?pid=9442)

## 题意

田忌赛马，求最好的结果。

## 思路

乍一看挺简单的，但是需要考虑的还是挺多的。

  1. 如果田鸡最快的比齐王最快的快，直接比下去。

  2. 如果田鸡最快的比齐王慢，这时候就要用最慢的赖一下齐王。但是，不能马上用最慢的去赖，因为可能田鸡最慢的马还比齐王最慢的马要快那么一丢丢，如果用这只马去赖就太亏了，他还有利用价值。这时候就顺便用这只马赢一下齐王最慢的马，然后接着比较。


反正到了最后肯定要赖掉一只，注意一下平局。

## 代码


```c++
#include <bits/stdc++.h>
#define LL long long
#define lowbit(x) ((x) & (-x))
#define MP(a, b) make_pair(a, b)
const int MAXN = 1000 + 5;
const int INF = 0x3f3f3f3f;
using namespace std;
 
int t[MAXN], w[MAXN];
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int T, i, j, n;
    while (scanf("%d", &n), n)
    {
        int ans = 0;
        for (i = 0; i < n; i++)
            scanf("%d", &t[i]);
        for (i = 0; i < n; i++)
            scanf("%d", &w[i]);
        sort(t, t + n);
        sort(w, w + n);
        int len1 = n - 1, len2 = n - 1;
        int s = 0, ss = 0;
        bool flag = true;
        while (flag)
        {
            if (ss == len2) flag = false;
            if (t[len1] > w[len2])
            {
                ans++;
                len1--, len2--;
            }
            else
            {
                if (t[s] > w[ss])
                {
                    ans++;
                    s++, ss++;
                }
                else
                {
                    if(t[s] < w[len2]) ans--;
                    s++, len2--;
                }
            }
        }
        printf("%d\n", ans * 200);
    }
    return 0;
}
```
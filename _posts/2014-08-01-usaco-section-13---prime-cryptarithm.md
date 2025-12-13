---
categories: Posts
date: 2014-08-01 00:00:00
title: USACO Section 1.3 - Prime Cryptarithm
tags: []
layout: post
---

## 题意

计算出符合条件的数量

## 思路

暴力

## 代码


```c++
/*
ID: mycodeb1
LANG: C++
TASK: crypt1
*/
 
#include <cstdio>
using namespace std;
const int MAXN = 10;
 
int num[MAXN];
 
bool Check(int n)
{
    while (n)
    {
        if (!num[n % 10])
            return false;
        n /= 10;
    }
    return true;
}
int main()
{
    //freopen("input.txt", "r", stdin);
    freopen("crypt1.in", "r", stdin);
    freopen("crypt1.out", "w", stdout);
 
    int n, i, j, a;
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &a);
        num[a] = 1;
    }
    int cnt = 0;
    for (i = 100; i <= 999; i++)
    {
        if (Check(i))
            for (j = 10; j * i < 10000; j++)
                if (Check(j))
                {
                    if (i * (j % 10) < 1000)
                    {
                        if (Check(i * (j % 10)))
                        {
                            int t = j / 10;
                            if (i * t < 1000)
                                if (Check(i * t) && Check(i * j))
                                    cnt++;
                        }
                    }
                }
    }
    printf("%d\n", cnt);
    return 0;
}
```
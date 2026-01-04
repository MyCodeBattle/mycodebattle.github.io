---
categories: Posts
date: 2014-08-10 00:00:00
title: USACO Section 1.1 - Friday the Thirteenth
tags: []
layout: post
---

## 题意

计算自1900年n年以来每月13号是星期几的数量

## 思路

看到计算星期几就吐血三升。可耻地找了一个计算公式。

然后只要算出当月13号是本年的第几天就行，直接无脑暴力了。

## 代码


```c++
/*
ID: mycodeb1
LANG: C++
TASK: friday
*/
 
#include <bits/stdc++.h>
using namespace std;
 
int month[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
int cnt[10];
 
bool isLeap(int n)
{
    if (!(n % 100))
        return n % 400 ? false : true;
    return n % 4 ? false : true;
}
 
void Solve(int X, int day)
{
    int S = X - 1 + (X - 1) / 4 - (X - 1) / 100 + (X - 1) / 400 + day;
    cnt[S % 7]++;
}
 
int main()
{
    //freopen("in.txt", "r", stdin);
    freopen("friday.in", "r", stdin);
    freopen("friday.out", "w", stdout);
 
    int n, i, j, base = 1900;
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        isLeap(base + i) ? month[2]++ : 0;
        for (j = 1; j <= 12; j++)
        {
            int day = 0;
            for (int k = 1; k < j; k++)
                day += month[k];
            day += 13;
            Solve(base + i, day);
        }
        month[2] != 28 ? month[2] = 28 : 0;
    }
    printf("%d", cnt[6]);
    for (i = 0; i < 6; i++)
        printf(" %d", cnt[i]);
    printf("\n");
    return 0;
}
```
---
categories: Posts
date: 2014-07-31 00:00:00
title: UVa 10056 - What is the Probability ?
tags: []
layout: post
---

## 传送门

[UVa 10056 - What is the Probability ?](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=997)

## 题意

不知道怎么归类，就归在数论里了。

现在有一个摇点游戏，摇到点的人赢。

给出玩的人数，赢的概率，赢的人，求这个人赢的概率。

## 思路

概率 = 第一轮赢 + 第二轮赢 + …… + 第n轮赢

n如何确定？  
只要当某轮赢的概率足够小就可以停止了。

## 代码


```c++
#include <bits/stdc++.h>
#define LL long long
using namespace std;
const double esp = 1e-6;
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int T, i, j, n, k;
    scanf("%d", &T);
    while (T--)
    {
        double p, ans = 0, temp = 1.1;
        scanf("%d%lf%d", &n, &p, &k);
        for (i = 0; temp > esp; i++)
        {
            temp = pow(1 - p, n * i + k - 1) * p;
            ans += temp;
        }
        printf("%.4lf\n", ans);
    }
    return 0;
}
```
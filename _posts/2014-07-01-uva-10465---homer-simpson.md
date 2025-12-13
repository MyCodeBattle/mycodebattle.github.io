---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 10465 - Homer Simpson
tags: []
layout: post
---

## 传送门

[UVa 10465 - Homer Simpson](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=114&problem=1406&mosmsg=Submission+received+with+ID+13844475)

## 题意

小明要吃两种汉堡，如果它能用一种方法正好在N分钟内吃完，输出吃的个数，否则输出它喝啤酒时间最少的时候的个数和喝啤酒的时间。

## 思路

参考了别人(忘记名字了)的解题报告。  
因为要凑整，所以先把DP里的数设置为<-10000的数，等到递推完成后从后面往前。如果dp[t]>0，说明正好可以吃完，输出，否则一直往下，找到第一个>0的，输出时间差。

## 代码
    
    
    123456789101112131415161718192021222324252627282930

| ```c++
#include <cstdio>#include <cstring>#include <algorithm>using namespace std;const int MAXN = 10000 + 10;const int INFS = -2147483648;int main(){    int time[2], dp[MAXN], i, j, t;    while (~scanf("%d%d%d", &time[0], &time[1], &t))    {        for (i = 0; i < MAXN; i++)            dp[i] = INFS;        dp[0] = 0;        for (i = 0; i < 2; i++)            for (j = time[i]; j <= t; j++)                dp[j] = max(dp[j], dp[j - time[i]] + 1);        for (i = t; i >= 0; i--)            if (dp[i] >= 0)            {                if (i == t)                    printf("%d\n", dp[i]);                else                    printf("%d %d\n", dp[i], t - i);                    break;            }    }    return 0;}
```
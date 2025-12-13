---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 10491 - Cows and Cars
tags: []
layout: post
---

## 传送门

[UVa 10491 - Cows and Cars](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1432)

## 题意

有一个电视节目，让你在N个门中选一个，可能是奶牛也可能是车子。当你选完以后，主持人会把k个门后是奶牛的门打开，这时候你必须重新选。  
求拿到车子的概率。

## 思路

第一次选可能是奶牛也可能是车子，分别把概率算出来相加即可。

## 代码


```c++
#include <cstdio>
#include <cmath>
 
int main()
{
    //freopen("in.txt", "r", stdin);
    int ncow, ncar, nshow, i, j;
    while (~scanf("%d%d%d", &ncow, &ncar, &nshow))
    {
        //choose cow first
        double cp1 = ncow * 1.0 / (ncow + ncar);
        int cowrem = ncow - nshow - 1;
        double cp2 = ncar * 1.0 / (cowrem + ncar);
        //choose car first
        double carp1 = ncar * 1.0 / (ncow + ncar);
        double carp2 = (ncar - 1) * 1.0 / (ncow - nshow + ncar - 1);
        double ans = cp1 * cp2 + carp1 * carp2;
        printf("%.5f\n", ans);
    }
    return 0;
}
```
---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 10791 - Minimum Sum LCM
tags: []
layout: post
---

## 传送门

[UVa 10791 - Minimum Sum LCM](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=115&problem=1732&mosmsg=Submission+received+with+ID+13955802)

## 题意

给出一个数，求以这个数为LCM的数的最小和。

## 思路

有两种情况。

  1. num为素数或者单因子数。此时最小和只能是num + 1。
  2. num为约数，此时的最小和是各个因数的数量次方的和。比如24，因数是2、2、2、3，最小和就是$2^3 + 3^1$。


## 代码


```c++
#include <bits/stdc++.h>
using namespace std;
#define LL long long
 
int main()
{
    //freopen("input.txt", "r", stdin);
    LL num, sum;
    int i, j, cnt, cases = 0;
    while (scanf("%lld", #), num)
    {
        sum = cnt = 0;
        LL r = num;
        int lim = (int)sqrt(num * 1.0 + 0.5);
        for (i = 2; i <= lim && r != 1; i++)
            if (!(r % i))
            {
                cnt++;
                LL temp = 1;
                while (!(r % i))
                {
                    temp *= i;
                    r /= i;
                }
                sum += temp;
            }
        printf("Case %d: ", ++cases);
        if (!cnt || (cnt == 1 && r == 1))
            printf("%lld\n", 1 + num);
        else if (r != 1)    //最后剩下的数可能不是1
            printf("%lld\n", sum + r);
        else
            printf("%lld\n", sum);
    }
    return 0;
}
```
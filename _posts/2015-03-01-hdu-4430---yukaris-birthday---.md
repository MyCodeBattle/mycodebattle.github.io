---
categories: Posts
date: 2015-03-01 00:00:00
title: HDU 4430 - Yukari's Birthday (二分 + 思维)
tags: []
layout: post
---

## 题意

给出N个蜡烛，问可以摆成多少个同心圆，每个同心圆的基准数是k。条件为r*k尽量小。

## 思路

分析得r最多为40。

又因为k有单调性，所以就二分了。

## 代码


```c++
LL Solve(int level, LL n)
{
    LL l = 2, r = (LL)pow(n, 1.0/level);
    while (l <= r)
    {
        LL mid = MID(l, r);
        LL cur = 1, sum = 0;
        for (int i = 1; i <= level; i++)
        {
            cur *= mid;
            sum += cur;
            if (sum > n) break;
        }
        if (sum == n) return mid;
        else if (sum > n) r = mid-1;
        else l = mid+1;
    }
    return 0;
}
 
int main()
{
    //ROP;
    LL n;
    while (~scanf("%lld", &n))
    {
        LL ansr, ansk, ans = (1ll<<62);
        for (int r = 1; r <= 40; r++)
        {
            LL tmp = Solve(r, n);
            if (tmp && ans > tmp*r)
            {
                ans = tmp*r;
                ansr = r, ansk = tmp;
            }
            tmp = Solve(r, n-1);
            if (tmp && ans > tmp*r)
            {
                ans = tmp*r;
                ansr = r, ansk = tmp;
            }
        }
        printf("%lld %lld\n", ansr, ansk);
    }
    return 0;
}
```
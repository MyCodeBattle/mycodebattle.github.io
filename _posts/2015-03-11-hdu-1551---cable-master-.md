---
categories: Posts
date: 2015-03-11 00:00:00
title: HDU 1551 - Cable master (二分)
tags: []
layout: post
---

## 题意

求最大每段电缆长度。

## 思路

二分

## 代码


```c++
bool Check(double num)
{
    int cnt = 0;
    for (int i = 0; i < n; i++) cnt += arr[i] / num;
    return cnt >= k;
}
 
int main()
{
    //ROP;
    while (scanf("%d%d", &n, &k), n)
    {
        for (int i = 0; i < n; i++) scanf("%lf", &arr[i]);
        double l = 0, r = INF, mid;
        while (r-l > 1e-4)
        {
            mid = (l+r)/2;
            if (Check(mid)) l = mid;
            else r = mid;
        }
        printf("%.2f\n", l);
    }
    return 0;
}
```
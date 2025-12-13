---
categories: Posts
date: 2015-03-01 00:00:00
title: PKU 2392 - Space Elevator (背包)
tags: []
layout: post
---

## 题意

给出几种类型的积木，高，高度限制，数量，问最高能叠多少。

## 思路

按高度限制从小到大排序，然后就背包了。

## 代码


```c++
struct POINT
{
    int h, a, q;
    bool operator < (const POINT &b) const
    {
        return a < b.a;
    }
}p[MAXN];
 
int dp[41000], num[41000];
 
int main()
{
    //ROP;
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d%d%d", &p[i].h, &p[i].a, &p[i].q);
    sort(p, p+n);
    int ans = 0;
    dp[0] = 1;
    for (int i = 0; i < n; i++)
    {
        MS(num, 0);
        for (int j = p[i].h; j <= p[i].a; j++)
            if (!dp[j] && dp[j-p[i].h] && num[j-p[i].h] < p[i].q)
            {
                dp[j] = 1;
                num[j] = num[j-p[i].h] + 1;
                ans = max(ans, j);
            }
    }
    printf("%d\n", ans);
    return 0;
}
```
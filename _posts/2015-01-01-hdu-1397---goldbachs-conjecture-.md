---
categories: Posts
date: 2015-01-01 00:00:00
title: HDU 1397 - Goldbach's Conjecture (筛素数)
tags: []
layout: post
---

## 题意

找出一个偶数能分解成几对素数和

## 思路

一遍扫描

## 代码


```c++
void GetPrimeTable()
{
    int m = (int)sqrt(MAXN + 0.5);
    for (int i = 2; i <= m; i++) if (!vis[i])
        for (int j = i*i; j < MAXN; j += i) vis[j] = 1;
}
 
int main()
{
    GetPrimeTable();
    int n;
    while (scanf("%d", &n), n)
    {
        int cnt = 0;
        for (int i = 2; i <= (n>>1); i++)
        {
            if (vis[i] || vis[n-i]) continue;
            cnt++;
        }
        printf("%d\n", cnt);
    }
    return 0;
}
```
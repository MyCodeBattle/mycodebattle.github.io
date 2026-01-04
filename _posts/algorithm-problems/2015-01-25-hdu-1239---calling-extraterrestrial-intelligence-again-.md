---
categories: Posts
date: 2015-01-25 00:00:00
title: HDU 1239 - Calling Extraterrestrial Intelligence Again (枚举)
tags: []
layout: post
---

## 题意

求出满足条件的数

## 思路

这题主要确定筛出1W而不是10W以内的素数。

分析如下：  
因为a/b >= 0.001

如果有一个质数Q > 1w，设P为另一个质数。  
如果P < 10，显然P/Q < 0.001，不符合条件  
如果P > 10，PQ > 10W，也不符合条件。

## 代码


```c++
vector<int> prime;
int vis[MAXN];
 
void GetPrimeTable()
{
    int m = (int)sqrt(MAXN + 0.5);
    for (int i = 2; i <= m; i++) if (!vis[i])
        for (int j = i*i; j < MAXN; j += i) vis[j] = 1;
    for (int i = 2; i < MAXN; i++) if (!vis[i])
        prime.PB(i);
}
 
int main()
{
    //ROP;
    GetPrimeTable();
    int m, a, b;
    while (scanf("%d%d%d", &m, &a, &b), m+a+b)
    {
        double cmp = a*1.0 / b;
        int x, y, res = -1;
        for (int i = 0; i < SZ(prime) && i < m; i++)
            for (int j = i; j < SZ(prime); j++)
            {
                if (prime[i]*prime[j] > m || prime[i]*1.0 / prime[j] < cmp) break;
                if (prime[i]*prime[j] > res)
                {
                    res = prime[i]*prime[j];
                    x = prime[i]; y = prime[j];
                }
            }
        printf("%d %d\n", x, y);
    }
    return 0;
}
```
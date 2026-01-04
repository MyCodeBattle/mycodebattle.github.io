---
categories: Posts
date: 2014-07-05 00:00:00
title: HDU 2602 - Bone Collector
tags: []
layout: post
---

## 传送门

[HDU 2602 - Bone Collector](http://acm.hdu.edu.cn/showproblem.php?pid=2602)

## 代码


```c++
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int MAXN = 1000 + 100;

struct BONE
{
    unsigned int volumn, value;
}bone[MAXN];

unsigned int dp[MAXN];

int main()
{
    //freopen("input.txt", "r", stdin);
    int T, i, j, n, vol;
    scanf("%d", &T);
    while (T--)
    {
        memset(dp, 0, sizeof(dp));
        scanf("%d%d", &n, &vol);
        for (i = 0; i < n; i++)
            scanf("%d", &bone[i].value);
        for (i = 0; i < n; i++)
            scanf("%d", &bone[i].volumn);
        for (i = 0; i < n; i++)
            for (j = vol; j >= 0; j--)
                if (j >= bone[i].volumn)
                    dp[j] = max(dp[j], dp[j - bone[i].volumn] + bone[i].value);
        printf("%u\n", dp[vol]);
    }
    return 0;
}
```
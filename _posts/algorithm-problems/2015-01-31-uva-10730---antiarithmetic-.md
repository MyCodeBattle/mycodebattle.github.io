---
categories: Posts
date: 2015-01-31 00:00:00
title: UVa 10730 - Antiarithmetic? (等差数列)
tags: []
layout: post
---

## 题意

判断一个数列中会不会出现3个的等差数

## 思路

记录每个数的位置

直接枚举公差，复杂度$O(nlogn)$

## 代码


```c++
int pos[MAXN];
 
int main()
{
    //ROP;
    int n;
    while (scanf("%d:", &n), n)
    {
        for (int i = 0; i < n; i++)
        {
            int tmp;
            scanf("%d", &tmp);
            pos[tmp] = i;
        }
        bool flag = false;
        for (int i = 0; i < n; i++)
        {
            if (flag) break;
            for (int j = 1; i + 2*j < n; j++)
            {
                if (pos[i] < pos[i+j] && pos[i+j] < pos[i+2*j]) flag = true;
                if (pos[i] > pos[i+j] && pos[i+j] > pos[i+2*j]) flag = true;
                if (flag) break;
            }
        }
        printf("%s\n", flag ? "no": "yes");
    }
    return 0;
}
```
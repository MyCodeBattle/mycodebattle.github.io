---
categories: Posts
date: 2015-03-01 00:00:00
title: PKU 1611 - The Suspects (并查集)
tags: []
layout: post
---

## 题意

问有几个人被感染。

## 思路

把一组的人全部并在一起，同时计算那组的人数。

## 代码


```c++
int f[MAXN], rnk[MAXN];
 
int Find(int a)
{
    return f[a] = (f[a] == a ? a : Find(f[a]));
}
 
void Union(int a, int b)
{
    int x = Find(a), y = Find(b);
    if (x == y) return;
    if (rnk[x] >= rnk[y])
    {
        f[y] = x;
        rnk[x] += rnk[y];
    }
    else
    {
        f[x] = y;
        rnk[y] += rnk[x];
    }
}
 
int main()
{
    //ROP;
    int n, m;
    while (scanf("%d%d", &n, &m), n+m)
    {
        for (int i = 0; i < n; i++) f[i] = i, rnk[i] = 1;
        for (int i = 0; i < m; i++)
        {
            int tmp, fir;
            scanf("%d%d", &tmp, &fir);
            for (int j = 1; j < tmp; j++)
            {
                int num;
                scanf("%d", #);
                Union(fir, num);
            }
        }
        printf("%d\n", rnk[Find(f[0])]);
    }
    return 0;
}
```
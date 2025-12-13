---
categories: Posts
date: 2015-03-01 00:00:00
title: HDU 1198 - Farm Irrigation (并查集)
tags: []
layout: post
---

## 题意

给出9种型状的水道，连通的水道只需要一个装置，问最少需要几个装置。

## 思路

把每个格子编号，然后和左边、上边判断是否联通。用并查集维护。

## 代码


```c++
int interface[][4] = { {1, 0, 1, 0}, {1, 0, 0, 1}, {0, 1, 1, 0}, {0, 1, 0, 1}, {1, 1, 0, 0}, {0, 0, 1, 1}, {1, 0, 1, 1}, {1, 1, 1, 0}, {0, 1, 1, 1}, {1, 1, 0, 1}, {1, 1, 1, 1} };
 
int idx(char c) { return c-'A'; }
 
int n, m, num[MAXN][MAXN];
char mp[MAXN][MAXN];
 
int Find(int tmp)
{
    return num[tmp/m][tmp%m] = (tmp == num[tmp/m][tmp%m] ? tmp : Find(num[tmp/m][tmp%m]));
}
 
void Union(int a, int b)
{
    int x = Find(a), y = Find(b);
    if (x != y) num[y/m][y%m] = x;
}
 
void Solve(int x, int y)
{
    if (y > 0 && interface[idx(mp[x][y])][2] && interface[idx(mp[x][y-1])][3]) Union(x*m+y, x*m+y-1);
    if (x > 0 && interface[idx(mp[x][y])][0] && interface[idx(mp[x-1][y])][1]) Union(x*m+y, (x-1)*m+y);
}
 
int main()
{
   // ROP;
    while (scanf("%d%d", &n, &m), n != -1)
    {
        for (int i = 0; i < n; i++)
        {
            scanf("%s", mp[i]);
            for (int j = 0; j < m; j++) num[i][j] = i*m+j;
        }
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) Solve(i, j);
        int ans = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (num[i][j] == i*m+j) ans++;
        printf("%d\n", ans);
    }
    return 0;
}
```
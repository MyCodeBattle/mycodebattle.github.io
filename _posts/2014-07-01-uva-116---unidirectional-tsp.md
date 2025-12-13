---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 116 - Unidirectional TSP
tags: []
layout: post
---

## 传送门

[UVa 116 - Unidirectional TSP](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=114&problem=52&mosmsg=Submission+received+with+ID+13821297)

## 题意

给一个图，最后一行向下走是第一行，第一行向上走是最后一行。要求从左边走到右边，数字之和最小，如果有相同的和，输出字典序最小的行数。

## 思路

参考了LRJ入门经典第二版。  
因为要是字典序最小，所以要从后面往前推。然后依次算出每一列的最小值，直到第一列，然后根据记录的路径输出。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758

| ```c++
#include <cstdio>#include <cstring>#include <algorithm>using namespace std;const int INF = 2147483647;int dp[20][110], Next[20][110], mp[20][110];int main(){    //freopen("input.txt", "r", stdin);    int m, n, i, j;    while (~scanf("%d%d", &m, &n))    {        memset(dp, 0, sizeof(dp));        for (i = 0; i < m; i++)            for (j = 0; j < n; j++)                scanf("%d", ∓[i][j]);        int ans = INF, first = 0;        for (int j = n - 1; j >= 0; j--)        {            for (int i = 0; i < m; i++)            {                if (j == n - 1)                    dp[i][j] = mp[i][j];                else                {                    int row[] = {i, i - 1, i + 1};                    if (i == 0)                        row[1] = m - 1;                    if (i == m - 1)                        row[2] = 0;                    sort(row, row + 3); //确保行数最小。                    dp[i][j] = INF;                    for (int k = 0; k < 3; k++)                    {                        int temp = dp[row[k]][j + 1] + mp[i][j];                        if (temp < dp[i][j])                        {                            dp[i][j] = temp;                            Next[i][j] = row[k];                        }                    }                }                if (j == 0 && dp[i][j] < ans)                {                    ans = dp[i][j];                    first = i;                }            }        }        printf("%d", first + 1);        for (i = Next[first][0], j = 1; j < n; i = Next[i][j], j++)            printf(" %d", i + 1);        printf("\n%d\n", ans);    }    return 0;}
```
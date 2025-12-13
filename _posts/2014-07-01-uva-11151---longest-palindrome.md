---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 11151 - Longest Palindrome
tags: []
layout: post
---

## 传送门

[UVa 11151 - Longest Palindrome](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=114&problem=2092&mosmsg=Submission+received+with+ID+13881450)

## 题意

给出一个字符串，通过删除某个字符，求最长的回文串。

## 思路

前几题字符串DP题目的简化版。  
求最长的回文串，就是求用最少的操作数把它变成回文串，因为一个操作数意味着少一个字符。

这样就和前几题的思路一样了。  
状态转移方程

$$dp[i][j] = \begin{cases}  
dp[i + 1][j - 1], & \text{if $str[i] == str[j]$} \\\  
min(dp[i + 1][j], dp[i][j - 1]) + 1, & \text{if $str[i] != str[j]$} \\\  
\end{cases}$$

## 代码


```c++
#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1000 + 10;

int dp[MAXN][MAXN];
char str[MAXN];

int DFS(int x, int y)
{
    int &ans = dp[x][y];
    if (x > y)
        return ans = 0;
    if (ans != -1)
        return ans;
    ans = 0;
    if (str[x] == str[y])
        ans = DFS(x + 1, y - 1);
    else
        ans = min(DFS(x + 1, y), DFS(x, y - 1)) + 1;
    return ans;
}

int main()
{
    //freopen("input.txt", "r", stdin);
    int T, i, j, len;
    scanf("%d%*c", &T);
    while (T--)
    {
        memset(dp, -1, sizeof dp);
        gets(str);
        len = strlen(str);
        if (len == 0)
        {
            printf("0\n");
            continue;
        }
        int temp = DFS(0, len - 1);
        printf("%d\n", len - temp);
    }
    return 0;
}
```
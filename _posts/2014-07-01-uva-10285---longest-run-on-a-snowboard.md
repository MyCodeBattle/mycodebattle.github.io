---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 10285 - Longest Run on a Snowboard
tags: []
layout: post
---

## 传送门

[UVa 10285 - Longest Run on a Snowboard](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=114&problem=1226&mosmsg=Submission+received+with+ID+13844915)

## 题意

小明要滑雪，输入代表高度，只能从高的地方滑向低的地方，输出最长路。

## 思路

对每个高度的四个方向进行DFS，然后记录。之后用上就行。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546

| ```c++
#include <cstdio>#include <cstring>#include <algorithm>using namespace std;const int MAXN = 100 + 10;const int dir[][2] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };int mp[MAXN][MAXN], dp[MAXN][MAXN], row, col;int DFS(int x, int y){    int &ans = dp[x][y];    if (ans != -1)        return ans;    ans = 1;    for (int i = 0; i < 4; i++)    {        int xx = x + dir[i][0];        int yy = y + dir[i][1];        if (xx >= 0 && xx < row && yy >= 0 && yy < col && mp[x][y] > mp[xx][yy])            ans = max(ans, DFS(xx, yy) + 1);    }    return ans;}int main(){    //freopen("input.txt", "r", stdin);    int i, j, n, T, ans;    char name[MAXN];    scanf("%d", &T);    while (T--)    {        ans = -1;        memset(dp, -1, sizeof dp);        scanf("%s%d%d", name, &row, &col);        for (i = 0; i < row; i++)            for (j = 0; j < col; j++)                scanf("%d", ∓[i][j]);        for (i = 0; i < row; i++)            for (j = 0; j < col; j++)                ans = max(ans, DFS(i, j));        printf("%s: %d\n", name, ans);    }    return 0;}
```
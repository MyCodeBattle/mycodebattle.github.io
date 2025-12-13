---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 531 - Compromise
tags: []
layout: post
---

## 传送门

[UVa 531 - Compromise](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=472)

## 题意

给出两段英文单词，求它们的最长公共单词，并输出。

## 思路

看懂那个公共子序列的图就行，然后沿着路径走到头，递归输出。

![公共子序列](http://blog.chinaunix.net/attachment/201210/15/26548237_1350310972zRwl.jpg)

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768697071727374

| ```c++
#include <cstdio>#include <cstring>using namespace std; char a[110][40], b[110][40];int dp[110][110], path[110][110];int na = 0, nb = 0;bool first = true; void Initial(){    memset(dp, 0, sizeof(dp));    memset(path, 0, sizeof(path));    na = nb = 0;    first = true;} void PrintAns(int i, int j){    if (i == 0 || j == 0)        return;    if (path[i][j] == 1)    {        PrintAns(i - 1, j - 1);        if (first)            printf("%s", a[i - 1]), first = false;        else            printf(" %s", a[i - 1]);    }    else if (path[i][j] == 2)        PrintAns(i, j - 1);    else        PrintAns(i - 1, j);}         int main(){    //freopen("in.txt", "r", stdin);    int i, j;    while (~scanf("%s", a[na]))    {        if (a[na][0] == '#')        {            while (scanf("%s", b[nb]), b[nb][0] != '#')                nb++;            for (i = 1; i <= na; i++)                for (j = 1; j <= nb; j++)                {                    if (strcmp(a[i - 1], b[j - 1]) == 0)                    {                        dp[i][j] = dp[i - 1][j - 1] + 1;                        path[i][j] = 1;                    }                    else if (dp[i][j - 1] >= dp[i - 1][j])                    {                        dp[i][j] = dp[i][j - 1];                        path[i][j] = 2;                    }                    else                    {                        dp[i][j] = dp[i - 1][j];                        path[i][j] = 3;                    }                }            //printf("%d\n", dp[na][nb]);            PrintAns(na, nb);            printf("\n");            Initial();            continue;        }        na++;    }    return 0;}
```
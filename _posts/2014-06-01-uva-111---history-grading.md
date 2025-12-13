---
categories: Posts
date: 2014-06-01 00:00:00
title: UVa 111 - History Grading
tags: []
layout: post
---

传送门：**[UVa 111 - History Grading](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=114&page=show_problem&problem=47)**

## 题意

一个历史老师要改试卷，有两种评分方式。一种是年份对了就给分，一种是顺序对了给分，按最大对的顺序给。现在选择第二种方式，求分数。

## 思路

字面意思，就是求最长公共子序列。  
不会，百度学习了一下。  
注意输入， 例如  
3,2,1  
意思是事件1在第三位，事件2在第二位。。以此类推。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738

| ```c++
#include <cstdio>#include <cstring>#include <algorithm>using namespace std;const int MAXN = 20 + 10;int main(){    //freopen("input.txt", "r", stdin);    int temp, corOrder[MAXN], dp[MAXN][MAXN], wrOrder[MAXN];    int n, i, j;    scanf("%d", &n);    for (i = 1; i <= n; i++)    {        scanf("%d", &temp);        corOrder[temp] = i;    }    while (~scanf("%d", &temp))    {        memset(dp, 0, sizeof(dp));        wrOrder[temp] = 1;        for (i = 2; i <= n; i++)        {            scanf("%d", &temp);            wrOrder[temp] = i;        }        for (i = 1; i <= n; i++)            for (j = 1; j <= n; j++)            {                if (corOrder[i] == wrOrder[j])                    dp[i][j] = dp[i - 1][j - 1] + 1;                else                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]);            }        printf("%d\n", dp[n][n]);    }    return 0;}
```
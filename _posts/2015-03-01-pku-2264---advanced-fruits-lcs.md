---
categories: Posts
date: 2015-03-01 00:00:00
title: PKU 2264 - Advanced Fruits (LCS)
tags: []
layout: post
---

## 题意

求出最短的字符串，包括上两个字符串。

## 思路

LCS部分输出一次，其他部分输出一次。

也是根据那个转移图来。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556

| ```c++
char s1[MAXN], s2[MAXN];int dp[MAXN][MAXN], path[MAXN][MAXN]; void Print(int l1, int l2){    if (l1 == 0 && l2 == 0) return;    if (path[l1][l2] == 0)    {        Print(l1-1, l2-1);        printf("%c", s1[l1]);    }    else if (path[l1][l2] == 1)    {        Print(l1-1, l2);        printf("%c", s1[l1]);    }    else    {        Print(l1, l2-1);        printf("%c", s2[l2]);    }} int main(){    //ROP;    while (~scanf("%s%s", s1+1, s2+1))    {        MS(dp, 0); MS(path, 0);        int len1 = strlen(s1+1), len2 = strlen(s2+1);        for (int i = 1; i <= len1; i++) path[i][0] = 1;        for (int i = 1; i <= len2; i++) path[0][i] = 2;        for (int i = 1; i <= len1; i++)            for (int j = 1; j <= len2; j++)            {                if (s1[i] == s2[j])                {                    dp[i][j] = dp[i-1][j-1]+1;                    path[i][j] = 0;                }                else if (dp[i-1][j] >= dp[i][j-1])                {                    dp[i][j] = dp[i-1][j];                    path[i][j] = 1; //up                }                else                {                    dp[i][j] = dp[i][j-1];                    path[i][j] = 2; //left                }            }        Print(len1, len2);        puts("");    }    return 0;}
```
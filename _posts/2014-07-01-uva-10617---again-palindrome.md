---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 10617 - Again Palindrome
tags: []
layout: post
---

## 传送门

[UVa 10617 - Again Palindrome](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1558)

## 题意

计算一个字符串内有多少个回文串

## 思路

用$dp[i][j]$表示i~j之间回文串的数量。状态转移方程  
$$  
dp[i][j] =  
\begin{cases}  
dp[i + 1][j - 1] + 1 + dp[i][j - 1] + dp[i + 1][j] - dp[i + 1][j - 1], & \text{if $str[i] = str[j]$} \\\  
dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1], & \text{if $str[i] != str[j]$} \\\  
\end{cases}  
$$  
引用一下Staginner的说明

> 我们设f[i][j]为字符串i到j这个区间内回文串的个数，那么如果b[i]==b[j]，f[i][j]=f[i+1][j]+f[i][j-1]-f[i+1][j-1]+f[i+1][j-1]+1=f[i+1][j]+f[i][j-1]+1，也就是说f[i][j]包括4个部分，第一部分是b[i]和中间的字符形成的回文串，第二部分是b[j]和中间的字符形成的回文串，这两部分也就等于区间[i,j-1]内的回文串的个数加上[i+1,j]内回文串的个数再减去区间[i+1,j-1]内的回文串的个数，也就是f[i+1][j]+f[i][j-1]-f[i+1][j-1]，第三部分是b[i]、b[j]和中间的字符形成的回文串，也就是f[i+1][j-1]，第四部分是仅由b[i]和b[j]这对组成的这一个回文串，所以是1，四部分综合到一起就是f[i][j]=f[i+1][j]+f[i][j-1]+1。  
> 同理，如果b[i]!=b[j]，那么f[i][j]= f[i+1][j]+f[i][j-1]-f[i+1][j-1]。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839

| ```c++
#include <cstdio>#include <cstring>#include <algorithm>using namespace std; char str[100];long long dp[65][65]; long long DFS(int x, int y){    long long &ans = dp[x][y];    if (ans != -1)        return ans;    if (x > y)        return ans = 0;    if (x == y)        return ans = 1;    ans = 0;    if (str[x] == str[y])        ans = DFS(x + 1, y - 1) + 1;    ans += DFS(x + 1, y) + DFS(x, y - 1) - DFS(x + 1, y - 1);    return ans;} int main(){    //freopen("input.txt", "r", stdin);    int T, i, j;    scanf("%d%*c", &T);    while (T--)    {        memset(dp, -1, sizeof dp);        gets(str);        int len = strlen(str);        DFS(0, len - 1);        printf("%lld\n", dp[0][len - 1]);    }    return 0;}
```
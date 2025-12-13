---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 10739 - String to Palindrome
tags: []
layout: post
---

## 传送门

[UVa 10739 - String to Palindrome](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1680)

## 题意

给一个字符串，可以再任意位置增加、删去、替换字符，求让他变成回文串的最少操作数

## 思路

参考。用dp[i][j]表示区间i~j的最少步数、

  1. s[i] == s[j] 显然只需要考虑i与j之间的字符串即可，此时dp[i][j] = dp[i+1][j-1]。

  2. s[i] != s[j]. 这时就要考虑到底是删除，插入还是替换。由于删除和插入所需要的操作步数以及影响是一致的，只需要考虑插入或者删除就行了。对于插入则dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1;对于替换则有dp[i][j] = min(dp[i][j], dp[i+1][j-1] + 1)


想了很久想不懂，只能先背下来了。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738

| ```c++
#include <cstdio>#include <algorithm>#include <cstring>using namespace std;const int MAXN = 1100;char str[MAXN];int dp[MAXN][MAXN];int DFS(int x, int y){    int &ans = dp[x][y];    if (ans != -1)        return ans;    if (x > y)        return ans = 0;    if (str[x] == str[y])        ans = DFS(x + 1, y - 1);    else        ans = min(min(DFS(x, y - 1), DFS(x + 1, y)), DFS(x + 1, y - 1)) + 1;    return ans;}int main(){    //freopen("input.txt", "r", stdin);    int T, i, j, cases = 0;    scanf("%d%*c", &T);    while (T--)    {        memset(dp, -1, sizeof dp);        gets(str);        int len = strlen(str);        DFS(0, len - 1);        printf("Case %d: %d\n", ++cases, dp[0][len - 1]);    }    return 0;}
```
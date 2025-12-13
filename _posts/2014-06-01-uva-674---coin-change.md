---
categories: Posts
date: 2014-06-01 00:00:00
title: UVa 674 - Coin Change
tags: []
layout: post
---

## 传送门

[UVa 674 - Coin Change](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=114&problem=615&mosmsg=Submission+received+with+ID+13808590)

## 思路

只能想到用动态规划的方法求出当剩余找钱数为n时得到的方法数，然后不管怎么想都写不出代码。。。  
可耻地参考了**[hcbbt的解题报告](http://blog.csdn.net/hcbbt/article/details/11861377)**  
主要就是用二维数组表示出状态，然后累加起来。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132

| ```c++
#include <cstdio>#include <cstring>using namespace std;const int MAXN = 7489 + 100;int dp[MAXN][5], money[] = {1, 5, 10, 25, 50};int DFS(int target, int k){    int &ans = dp[target][k];    if (ans != -1)        return ans;    ans = 0;    for (int i = k; i < 5; i++)        if (target >= money[i])            ans += DFS(target - money[i], i);    return ans;}int main(){    int cents, n, i, j;    memset(dp, -1, sizeof(dp));    for (i = 0; i < 5; i++)        dp[0][i] = 1;    while (~scanf("%d", &cents))    {        int ans = DFS(cents, 0);        printf("%d\n", ans);    }    return 0;}
```
---
categories: Posts
date: 2014-09-01 00:00:00
title: UVa 2678 - Subsequence
tags: []
layout: post
---

#  [UVa 2678 - Subsequence](/2014/09/UVa-2678/ "UVa 2678 - Subsequence")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 4 2014 20:39

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 2678 - Subsequence](http://www.bnuoj.com/v3/problem_show.php?pid=8854)

## 题意

求连续的序列中最少个相加大于等于sum的个数。

## 思路

s[j] - s[i] >= sum

s[i] <= s[j] - sum.

要使i最大。

这时候可以用lower_bound，直接找i，对于每个j。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031

| 
    
    
    #include <bits/stdc++.h>#define LL long long#define lowbit(x) ((x) & (-x))const int MAXN = 1e5 + 5;const int INF = 0x3f3f3f3f;using namespace std; int num[MAXN]; int main(){    //freopen("input.txt", "r", stdin);    int n, s, i, j;    while (~scanf("%d%d", &n, &s))    {        int ans = INF;        for (i = 1; i <= n; i++)        {            scanf("%d", #[i]);            num[i] += num[i - 1];        }        for (i = 1; i <= n; i++)        {            int k = lower_bound(num, num + n, num[i] - s) - num;            if (k > 0)                ans = min(ans, i - k + 1);        }        printf("%d\n", ans == INF ? 0 : ans);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)

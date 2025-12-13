---
categories: Posts
date: 2014-09-01 00:00:00
title: UVa 11389 - The Bus Driver Problem
tags: []
layout: post
---

#  [UVa 11389 - The Bus Driver Problem](/2014/09/UVa-11389/ "UVa 11389 - The Bus Driver Problem")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 12 2014 18:45

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 11389 - The Bus Driver Problem](http://www.bnuoj.com/v3/problem_show.php?pid=19807)

## 题意

有N个司机，有N个下午人物，N个夜间任务，每个人执行的时间超过d就要付加班费，每小时r，求加班费最小。

## 思路

下午随便选，让干得最少的人干最重的活。

## 代码
    
    
    123456789101112131415161718192021222324252627

| 
    
    
    #include <bits/stdc++.h>#define LL long long#define lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)const int MAXN = 100 + 5;const int INF = 0x3f3f3f3f;using namespace std; int pit[MAXN], num[MAXN]; int main(){    //freopen("input.txt", "r", stdin);    int n, d, r, i, j;    while (scanf("%d%d%d", &n, &d, &r) && n + d + r > 0)    {        for (i = 0; i < n; i++) scanf("%d", &pit[i]);        for (i = 0; i < n; i++) scanf("%d", #[i]);        sort(pit, pit + n);        sort(num, num + n, greater<int>());        int ans = 0;        for (i = 0; i < n; i++)            ans += max((pit[i] + num[i] - d) * r, 0);        printf("%d\n", ans);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Foundation - Greedy](/tags/Foundation-Greedy/)

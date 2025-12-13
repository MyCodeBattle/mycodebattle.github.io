---
categories: Posts
date: 2014-09-01 00:00:00
title: UVa 11549 - Calculator Conundrum
tags: []
layout: post
---

#  [UVa 11549 - Calculator Conundrum](/2014/09/UVa-11549/ "UVa 11549 - Calculator Conundrum")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 2 2014 16:50

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 11549 - Calculator Conundrum](http://www.bnuoj.com/v3/problem_show.php?pid=19967)

## 题意

给出一个数，和保留的位数，求它在平方的过程中产生的最大的数。

## 思路

产生的数是循环的，所以只要找到相同的就可以停止了。可以用set。

LRJ介绍了Floyd判圈算法，他说快了500ms，可是我试了一下还是一样。。看来是我写挫了。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849

| 
    
    
    #include <bits/stdc++.h>#define LL long long#define lowbit(x) ((x) & (-x))const int MAXN = 30 + 5;const int INF = 0x3f3f3f3f;using namespace std; char str[MAXN];set<int> mp; int Read(){    char ch;    int ans = 0;    for (int i = 0; i < strlen(str); i++)        ans = ans * 10 + str[i] - '0';    return ans;} int Next(int n, int k){    memset(str, 0, sizeof str);    LL t = (LL)k * k;    sprintf(str, "%lld", t);    int len = strlen(str);    if (len > n) str[n] = 0;    return Read();} int main(){    //freopen("input.txt", "r", stdin);    int T, n, k;    scanf("%d", &T);    while (T--)    {        int ans = -1;        scanf("%d%d", &n, &k);        mp.clear();        while (!mp.count(k))        {            mp.insert(k);            ans = max(ans, k);            k = Next(n, k);        }        printf("%d\n", ans);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Foundation - Simulate](/tags/Foundation-Simulate/)

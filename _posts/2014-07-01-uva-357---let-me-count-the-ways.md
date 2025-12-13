---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 357 - Let Me Count The Ways
tags: []
layout: post
---

#  [UVa 357 - Let Me Count The Ways](/2014/07/UVa-357/ "UVa 357 - Let Me Count The Ways")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jul 3 2014 15:27

**Contents**

  1. 1. 传送门
  2. 2. 思路
  3. 3. 代码

## 传送门

[UVa 357 - Let Me Count The Ways](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=114&problem=293&mosmsg=Submission+received+with+ID+13826217)

## 思路

因为不想在一片绿色中空出一道白色才做的。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940

| 
    
    
    #include <cstdio>#include <cstring>#include <algorithm>#define LL long longusing namespace std;const int MAXN = 30000 + 100;const int mon[] = {1, 5, 10, 25, 50};LL d[MAXN][5];LL DP(int rim, int us){    LL &ans = d[rim][us];    if (ans != -1)        return ans;    ans = 0;    for (int i = us; i < 5; i++)        if (rim >= mon[i])            ans += DP(rim - mon[i], i);    return ans;}int main(){    //freopen("input.txt", "r", stdin);    int temp;    LL i, j, ans, money;    memset(d, -1, sizeof(d));    for (i = 0; i < 5; i++)        d[0][i] = 1;    while (~scanf("%d", &temp))    {        ans = DP(temp, 0);        if (ans == 1)            printf("There is only 1 way to produce %d cents change.\n", temp);        else            printf("There are %lld ways to produce %d cents change.\n", ans, temp);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Dynamic Programming](/tags/Dynamic-Programming/)

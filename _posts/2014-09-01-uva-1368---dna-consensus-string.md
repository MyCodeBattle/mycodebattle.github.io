---
categories: Posts
date: 2014-09-01 00:00:00
title: UVa 1368 - DNA Consensus String
tags: []
layout: post
---

#  [UVa 1368 - DNA Consensus String](/2014/09/UVa-1368/ "UVa 1368 - DNA Consensus String")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 3 2014 16:41

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 1368 - DNA Consensus String](http://vjudge.net/problem/viewProblem.action?id=36539)

## 题意

找出一个字符串，使得它的Hamming Distance最小。

## 思路

对每个位置进行贪心，选出现次数最多的字母。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950

| 
    
    
    #include <cstdio>#include <iostream>#include <string>#include <cstring>#define LL long long#define lowbit(x) ((x) & (-x))const int MAXN = 1e3 + 5;const int INF = 0x3f3f3f3f;using namespace std; struct SCAN{    char c;    int num;}scan; char str[55][MAXN];int num[30]; int main(){    //freopen("input.txt", "r", stdin);    int n, i, j, T, leng;    scanf("%d", &T);    while (T--)    {        int nerr = 0;        scanf("%d%d%*c", &n, &leng);        string ans;        for (i = 0; i < n; i++)            scanf("%s", str[i]);        for (i = 0; i < leng; i++)        {            memset(num, 0, sizeof num);            for (j = 0; j < n; j++)                num[str[j][i] - 'A']++;            scan.c = 'A', scan.num = num[0];            for (j = 1; j < 30; j++)                if (num[j] > scan.num)                    scan.c = j + 'A', scan.num = num[j];            ans += scan.c;            for (j = 0; j < 30; j++)                if (j + 'A' != scan.c)                    nerr += num[j];        }        cout << ans << endl;        cout << nerr << endl;    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Foundation - Greedy](/tags/Foundation-Greedy/)

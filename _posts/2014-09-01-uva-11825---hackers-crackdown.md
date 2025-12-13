---
categories: Posts
date: 2014-09-01 00:00:00
title: UVa 11825 - Hackers' Crackdown
tags: []
layout: post
---

## 题意

有N个服务器，分别运行着N个相同服务。对于每一个服务器，你可以选择停止一个服务，这样和他相邻的服务器这个服务也会停掉。求最多能使几个服务瘫痪。

## 思路

例题。就是求把集合P分成尽量多组，每组的并集都是全集。

先压缩出分组情况，然后枚举每一种情况的子集。

$dp[i] = max(dp[i], dp[i \^ j] + 1)$(j符合并集是全集的条件)

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263

| ```c++
#include <cstdio>#include <algorithm>#include <functional>#include <stack>#include <iostream>#include <string>#include <vector>#include <queue>#include <cstring>#include <string>#include <sstream>#include <map>#include <cmath>#define LL long long#define lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define ROP freopen("input.txt", "r", stdin);const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std; const int MAXN = (1 << 17) + 5; int dp[MAXN], cover[MAXN], num[20]; int main(){    //ROP;    int n, i, j, cases = 0;    while (scanf("%d", &n), n)    {        for (i = 0; i < n; i++)        {            int k;            scanf("%d", &k);            num[i] = (1 << i);            for (j = 0; j < k; j++)            {                int x;                scanf("%d", &x);                num[i] |= (1 << x);            }        }        for (int S = 0; S < (1 << n); S++)        {            cover[S] = 0;            for (i = 0; i < n; i++)                if (S & (1 << i)) cover[S] |= num[i];        }        dp[0] = 0;        int tot = (1 << n) - 1;        for (int S = 1; S < (1 << n); S++)        {            dp[S] = 0;            for (int S0 = S; S0; S0 = (S0 - 1) & S)                if (cover[S0] == tot) dp[S] = max(dp[S], dp[S ^ S0] + 1);        }        printf("Case %d: %d\n", ++cases, dp[tot]);    }    return 0;}
```
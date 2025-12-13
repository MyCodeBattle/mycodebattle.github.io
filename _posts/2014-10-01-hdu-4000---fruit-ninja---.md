---
categories: Posts
date: 2014-10-01 00:00:00
title: HDU 4000 - Fruit Ninja (树状数组 + 推理)
tags: []
layout: post
---

## 题意

找出按顺序且x < z < y的个数。

## 思路

一直想以其中的一个为起点枚举，就算知道了是树状数组也不知道树状数组怎么用TAT。还是看了题解。

原来是用树状数组统计出当前数后面有几个是比他大的。那么这时候可以组成的排列是$x * (x - 1) / 2$。但是这里面包括不符合要求的x < y < z，所以要把这部分减去。涨姿势了。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687

| ```c++
#include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>#define LL long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 1e5 + 10;const int MOD = 100000007; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int C[MAXN], n; int Sum(int k){    int ret = 0;    while (k > 0)    {        ret += C[k];        k -= Lowbit(k);    }    return ret;} void Update(int k){    while (k <= n)    {        C[k]++;        k += Lowbit(k);    }} int main(){    //ROP;    int T, i, j, cases = 0;    scanf("%d", &T);    while (T--)    {        MS(C, 0);        scanf("%d", &n);        LL ans = 0;        for (i = 1; i <= n; i++)        {            int tmp;            scanf("%d", &tmp);            Update(tmp);            LL preSmall = Sum(tmp - 1);            LL preBig = i - 1 - preSmall;            LL aftBig = n - tmp - preBig;            ans -= preSmall * aftBig;            if (aftBig >= 2) ans += aftBig * (aftBig - 1) / 2;            ans %= MOD;        }        printf("Case #%d: %lld\n", ++cases, (ans + MOD) % MOD);    }    return 0;}
```
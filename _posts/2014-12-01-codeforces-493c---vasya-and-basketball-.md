---
categories: Posts
date: 2014-12-01 00:00:00
title: Codeforces 493C - Vasya and Basketball (二分)
tags: []
layout: post
---

## 题意

划定一个得分线，在这个线上算三分，以下算两分，要求A队和B队的分差尽量大

## 思路

一开始用了二分，但是没考虑到如果分数相等的时候怎么划分。这种思路应该是错的。

其实直接暴力就行了，检验一下每一个得分点。。。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768697071727374757677787980818283848586878889909192939495969798

| ```c++
#include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <ctime>#include <string>#include <map>#include <iomanip>#include <cmath>#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)#define BitCountll(x) __builtin_popcountll(x)#define LeftPos(x) 32 - __builtin_clz(x) - 1#define LeftPosll(x) 64 - __builtin_clzll(x) - 1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const double eps = 1e-6;const int MAXN = 2e5 + 10;const int MOD = 1000007;const int dir[][2] = { {1, 0}, {-1, 0}, {0, -1}, {0, 1} }; int fir[MAXN], sec[MAXN], ans, m, n, pivot = -INF;  int GetAns(int *arr, int n){    int cnt = upper_bound(arr, arr + n, ans) - arr;    return 2ll * cnt + (n - cnt) * 3;} vector<int> tot;set<int> mp; int main(){    //ROP;    int i, j;    scanf("%d", &m);    for (int i = 0; i < m; i++)    {        scanf("%d", &fir[i]);        tot.PB(fir[i]);    }    scanf("%d", &n);    for (int i = 0; i < n; i++)    {        scanf("%d", &sec[i]);        tot.PB(sec[i]);    }    tot.PB(0);    sort(fir, fir + m); sort(sec, sec + n);    LL firAns, secAns, rec;    for (int i = 0; i < SZ(tot); i++)    {        if (mp.count(tot[i])) continue;        mp.insert(tot[i]);        int firCnt = upper_bound(fir, fir + m, tot[i]) - fir, secCnt = upper_bound(sec, sec + n, tot[i]) - sec;        firAns = 2ll * firCnt + (m - firCnt) * 3, secAns = 2ll * secCnt + (n - secCnt) * 3;        if (firAns - secAns > pivot)        {            pivot = firAns - secAns;            rec = firAns;            ans = tot[i];        }        else if (firAns - secAns == pivot && firAns > rec)        {            pivot = firAns - secAns;            ans = tot[i];        }            }    firAns = GetAns(fir, m), secAns = GetAns(sec, n);    printf("%lld:%lld\n", firAns, secAns);    return 0;}
```
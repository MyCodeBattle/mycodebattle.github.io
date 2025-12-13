---
categories: Posts
date: 2014-11-01 00:00:00
title: HDU 5104 - Primes Problem (枚举)
tags: []
layout: post
---

## 题意

找出n1 + n2 + n3 = n && n1 and n2 and n3为素数的三元组数

## 思路

先打表出1W以内的素数，然后枚举n2、n3。判断n - n2 - n3是否为素数，如果是的话判断该数是否 <= n2。是的话ans + 1

一开始用lower_bound竟然T了？

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879

| ```c++
#include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)#define BitCountll(x) __builtin_popcountll(x)#define LeftPos(x) 32 - __builtin_clz(x) - 1#define LeftPosll(x) 64 - __builtin_clzll(x) - 1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const double eps = 1e-8;const int MAXN = 10000 + 10;const int MOD = 1000007;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };  //0123£¬ÉÏÏÂ×óÓÒ typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; vector<int> pri;int n, vis[MAXN]; void GetPrime(){    vis[1] = 1;    for (int i = 2; i <= MAXN; i++)        if (!vis[i])        {            pri.PB(i);            for (int j = i * 2; j <= MAXN; j += i) vis[j] = 1;        }} int main(){    //ROP;    ios::sync_with_stdio(0);     int i, j;    GetPrime();    while (cin >> n)    {        int ans = 0;        for (int i = 0; pri[i] < n && i < SZ(pri); i++)            for (j = i; pri[j] + pri[i] < n && j < SZ(pri); j++)            {                if (vis[n - pri[i] - pri[j]] == 0 && n - pri[i] - pri[j] <= pri[i])                    ans++;            }        cout << ans << endl;    }    return 0;}
```
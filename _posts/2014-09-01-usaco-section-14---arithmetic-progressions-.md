---
categories: Posts
date: 2014-09-01 00:00:00
title: USACO Section 1.4 - Arithmetic Progressions （暴力）
tags: []
layout: post
---

## 题意

给出m，要求在[0, m]的范围内，由(0 <= p, q <= m)，$p^2 + q^2$所组成的集合内，输出长度为n的等差数列。

## 思路

m最大才250，直接开个vis数组，记录达到的数。

接下来我是把这些数都存在一个数组里，从这个数组里取出来，两两枚举k，然后判断接下来的数是否vis过。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879808182838485

| ```c++
/*ID: mycodeb1LANG: C++TASK: ariprog*/ #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <ctime>#include <cstdlib>#include <fstream>#include <string>#include <sstream>#include <map>#include <cmath>#define LL long long#define lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 250 + 5; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int vis[MAXN * MAXN * 2];vector<pii> ans;vector<int> mp; int main(){    //ROP;    freopen("ariprog.in", "r", stdin);    freopen("ariprog.out", "w", stdout);     int n, m, i, j;    scanf("%d%d", &n, &m);    for (i = 0; i <= m; i++)        for (j = 0; j <= m; j++)        {            int a = i * i + j * j;            if (vis[a]) continue;            mp.PB(a);            vis[a] = 1;        }    sort(mp.begin(), mp.end());    for (i = 0; i < mp.size(); i++)        for (j = i + 1; j < mp.size(); j++)        {            int cnt = 2;            int k = mp[j] - mp[i], last = mp[j];            if (mp[i] + (n - 1) * k > mp.back()) continue;            while (cnt < n)            {                if (!vis[mp[i] + cnt * k]) break;                else cnt++;            }            if (cnt == n) ans.push_back(MP(k, mp[i]));        }    sort(ans.begin(), ans.end());    if (ans.empty())    {        puts("NONE");        return 0;    }    for (vitii it = ans.begin(); it != ans.end(); it++)        printf("%d %d\n", it->S, it->F);    return 0;}
```
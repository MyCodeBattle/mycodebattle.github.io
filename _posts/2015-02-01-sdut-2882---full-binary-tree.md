---
categories: Posts
date: 2015-02-01 00:00:00
title: SDUT 2882 - Full Binary Tree(思维)
tags: []
layout: post
---

## 思路

今天的例行水题。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768697071

| ```c++
#include <stack>#include <cstdio>#include <list>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 50 + 3;const int MOD = 1e9 + 7;const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };int cases = 0;typedef pair<int, int> pii; int main(){    //ROP;    int T;    scanf("%d", &T);    while (T--)    {        int a, b;        scanf("%d%d", &a, &b);        if (a < b) swap(a, b);        int ans = 0;        while (true)        {            while ((a>>1) >= b)            {                a >>= 1;                ans++;                if (a == b) break;            }            if (a == b) break;            a >>= 1;            ans++;            if (a == b) break;            b >>= 1;            ans++;            if (a == b) break;        }        printf("%d\n", ans);    }    return 0;}
```
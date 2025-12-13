---
categories: Posts
date: 2015-01-01 00:00:00
title: UVa 1554 - Binary Search (枚举)
tags: []
layout: post
---

## 题意

给一个最后搜索到的数字和搜索的次数，问有哪些区间内的数可以得到这个结果。

## 思路

一开始还想用BFS推出来，推了好久。后来一想我真是2数据才1W按题目给的二分方法一遍扫描过去O(nlogn)妥妥的。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990

| ```c++
#include <cstdio>#include <stack>#include <list>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)#define BitCountll(x) __builtin_popcountll(x)#define LeftPos(x) 32 - __builtin_clz(x) - 1#define LeftPosll(x) 64 - __builtin_clzll(x) - 1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 1e4 + 10;const int MOD = 1000007;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };int cases = 0;typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int A[MAXN];int N, vis[MAXN], limit; bool BinarySearch(int x){    int p, q, i, L;    p = 0;   /* Left border of the search  */    q = N-1; /* Right border of the search */    L = 0;   /* Comparison counter         */    while (p <= q) {        i = (p + q) / 2;        ++L;        if (A[i] == x) return L == limit;        if (x < A[i])          q = i - 1;        else          p = i + 1;    }    return false;} int main(){    //ROP;    int i, j, target;    for (i = 0; i <= MAXN; i++) A[i] = i;    while (~scanf("%d%d", ⌖, &limit))    {        bool flag = false;        MS(vis, 0);        for (N = 1; N <= 10000; N++)            if (BinarySearch(target)) vis[N] = 1;        int pre;        vector<pii> ans;        for (i = 1; i <= N; i++)        {            if (vis[i] && !vis[i - 1]) pre = i;            if (vis[i] && !vis[i + 1]) ans.PB({pre, i});        }        printf("%d\n", SZ(ans));        for (i = 0; i < SZ(ans); i++) printf("%d %d\n", ans[i].X, ans[i].Y);    }    return 0;}
```
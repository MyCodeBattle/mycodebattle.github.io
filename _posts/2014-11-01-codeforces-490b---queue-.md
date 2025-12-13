---
categories: Posts
date: 2014-11-01 00:00:00
title: Codeforces 490B - Queue (模拟)
tags: []
layout: post
---

## 题意

给出每个人前一个人和后一个人的编号，求完整的队列。

## 思路

我是模拟的TAT

统计每个元素的入度和出度（排在前面的是入度，后面出度）

观察一下可发现，偶数位置上的就直接可以从0后面的那个元素接上。

奇数位置，找到入度（前一个数）为1，出度为0的，这个就是开头，用二分往下找。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114

| ```c++
#include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <iomanip>#include <cmath>#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)#define BitCountll(x) __builtin_popcountll(x)#define LeftPos(x) 32 - __builtin_clz(x) - 1#define LeftPosll(x) 64 - __builtin_clzll(x) - 1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const double eps = 1e-6;const int MAXN = 2e5 + 10;const int MOD = 1000007;typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii;  struct POINT{    int pre, next;    bool operator < (const POINT &a) const    {        return pre < a.pre;    }}pit[MAXN];  int ans[MAXN], in[MAXN], out[MAXN], n;map<int, int> inMap, outMap;  int Solve(int val){    int l = 0, r = n, mid;    while (l < r)    {        mid = MID(l, r);        if (pit[mid].pre == val) return mid;        if (pit[mid].pre < val) l = mid + 1;        else r = mid;    }    return -1;}    int main(){    //ROP;    int i, j;    scanf("%d", &n);    for (int i = 0; i < n; i++)    {        int a, b;        scanf("%d%d", &pit[i].pre, &pit[i].next);        inMap[pit[i].pre]++, outMap[pit[i].next]++;    }    sort(pit, pit + n);    int pos = 2;    int curPeo = pit[0].next;    while (curPeo != 0)    {        ans[pos] = curPeo;        pos += 2;        int tmpPos = Solve(curPeo);        if (tmpPos == -1) break;        curPeo = pit[tmpPos].next;    }    pos = 1;    for (i = 1; i <= n; i++)    {        if (inMap[pit[i].pre] == 1 && outMap[pit[i].pre] == 0)        {            curPeo = pit[i].pre;            break;        }    }    ans[pos] = curPeo; curPeo = pit[i].next;    pos += 2;    while (curPeo != 0)    {        ans[pos] = curPeo;        pos += 2;        int tmpPos = Solve(curPeo);        if (tmpPos == -1) break;        curPeo = pit[tmpPos].next;    }    for (i = 1; i <= n; i++) printf("%d ", ans[i]);    return 0;}
```
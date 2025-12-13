---
categories: Posts
date: 2014-10-01 00:00:00
title: PKU 3264 - Balanced Lineup (基础线段树)
tags: []
layout: post
---

#  [PKU 3264 - Balanced Lineup (基础线段树)](/2014/10/PKU-3264/ "PKU 3264 - Balanced Lineup \(基础线段树\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Oct 18 2014 11:25

**Contents**

  1. 1. 代码

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>#define LL long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 50000 + 10;const int MOD = 1e9 + 7;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} }; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; struct SEGMENTTREE{    int vmin, vmax;}segt[MAXN << 2]; void PushUp(int rt){    segt[rt].vmax = max(segt[LRT].vmax, segt[RRT].vmax);    segt[rt].vmin = min(segt[LRT].vmin, segt[RRT].vmin);} struct SEGTREE{    void build(int rt, int l, int r)    {        if (l == r)        {            int a;            scanf("%d", &a);            segt[rt].vmin = segt[rt].vmax = a;            return;        }        int mid = MID(l, r);        build(LC); build(RC);        PushUp(rt);    }     int queryMax(int rt, int l, int r, int L, int R)    {        if (L <= l && r <= R) return segt[rt].vmax;        int mid = MID(l, r), ans = -1;        if (L <= mid) ans = queryMax(LC, L, R);        if (R > mid) ans = max(ans, queryMax(RC, L, R));        return ans;    }     int queryMin(int rt, int l, int r, int L, int R)    {        if (L <= l && r <= R) return segt[rt].vmin;        int mid = MID(l, r), ans = INF;        if (L <= mid) ans = queryMin(LC, L, R);        if (R > mid) ans = min(ans, queryMin(RC, L, R));        return ans;    }}seg; int main(){   // ROP;    int n, nq, i, j;    scanf("%d%d", &n, &nq);    seg.build(1, 1, n);    while (nq--)    {        int a, b;        scanf("%d%d", &a, &b);        printf("%d\n", seg.queryMax(1, 1, n, a, b) - seg.queryMin(1, 1, n, a, b));    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - PKU](/tags/Online-Judge-PKU/)[Data Structure - Seg Tree](/tags/Data-Structure-Seg-Tree/)

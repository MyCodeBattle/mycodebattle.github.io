---
categories: Posts
date: 2014-10-01 00:00:00
title: PKU 3468 - A Simple Problem with Integers (线段树 + 区间修改)
tags: []
layout: post
---

#  [PKU 3468 - A Simple Problem with Integers (线段树 + 区间修改)](/2014/10/PKU-3468/ "PKU 3468 - A Simple Problem with Integers \(线段树 + 区间修改\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Oct 1 2014 10:33

**Contents**

  1. 1. 代码

## 代码

线段树第二发
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127128129130131

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <ctime>#include <cstdlib>#include <fstream>#include <string>#include <sstream>#include <map>#include <cmath>#define LL long long#define lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 1e5 + 5;const int MOD = 20071027; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; struct SEGTREE{    LL sum, add;}segt[MAXN << 2]; void PushUp(int rt){    segt[rt].sum = segt[rt << 1].sum + segt[rt << 1|1].sum;} void PushDown(int rt, int m){    LL &cur = segt[rt].add;    if (cur)    {        segt[LRT].add += cur;        segt[RRT].add += cur;        segt[LRT].sum += cur * (m - (m >> 1));        segt[RRT].sum += cur * (m >> 1);        cur = 0;    }} LL Quary(int rt, int l, int r, int L, int R){    if (L <= l && r <= R)        return segt[rt].sum;    PushDown(rt, r - l + 1);    int mid = MID(l, r);    LL ret = 0;    if (L <= mid) ret += Quary(LC, L, R);    if (R > mid) ret += Quary(RC, L, R);    return ret;} void Update(int rt, int l, int r, int L, int R, LL add){    if (L <= l && r <= R)    {        segt[rt].add += add;        segt[rt].sum += (r - l + 1) * add;        return;    }    PushDown(rt, r - l + 1);    int mid = MID(l, r);    if (L <= mid) Update(LC, L, R, add);    if (R > mid) Update(RC, L, R, add);    PushUp(rt);} void Build(int rt, int l, int r){    segt[rt].add = segt[rt].sum = 0;    if (l == r)    {        scanf("%lld", &segt[rt].sum);        return;    }    int mid = MID(l, r);    Build(LC);    Build(RC);    PushUp(rt);} int main(){    //ROP;    int n, i, j, nQuary;    scanf("%d%d", &n, &nQuary);    Build(1, 1, n);    char ch[5];    while (nQuary--)    {        scanf("%s", ch);        int a, b;        LL c;        if (ch[0] == 'Q')        {            scanf("%d%d", &a, &b);            printf("%lld\n", Quary(1, 1, n, a, b));        }        else        {            scanf("%d%d%lld", &a, &b, &c);            Update(1, 1, n, a, b, c);        }    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - PKU](/tags/Online-Judge-PKU/)[Data Structure - Seg Tree](/tags/Data-Structure-Seg-Tree/)

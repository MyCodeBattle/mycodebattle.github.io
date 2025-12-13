---
categories: Posts
date: 2015-02-01 00:00:00
title: Light 1135 - Count the Multiples of 3 (线段树 + 区间修改)
tags: []
layout: post
---

## 题意

区间统一增加1和询问区间内能被3整除的个数。

## 思路

一开始想直接维护答案，但是不行。

要维护区间内余数是0、1、2的个数。

复习了一下区间修改的写法。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127128129130

| ```c++
#include <stack>#include <cstdio>#include <list>#include <cassert>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 1e5 + 10;const int MOD = 9901;const int MOD2 = 1e9 + 9;const int seed = 188147;const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };int cases = 0;typedef pair<int, int> pii; struct SEGTREE{    int cnt[3], lazy;}t[MAXN<<2]; void maintain_node(int rt){    int *arr = t[rt].cnt;    int v0 = arr[0], v1 = arr[1], v2 = arr[2];    arr[0] = v2, arr[1] = v0, arr[2] = v1;} void Maintain(int rt){    for (int i = 0; i < 3; i++) t[rt].cnt[i] = t[LRT].cnt[i] + t[RRT].cnt[i];} void PushDown(int rt){    t[rt].lazy %= 3;    t[LRT].lazy += t[rt].lazy, t[RRT].lazy += t[rt].lazy;    for (int i = 0; i < t[rt].lazy; i++) maintain_node(LRT), maintain_node(RRT);    t[rt].lazy = 0;} int Query(int rt, int l, int r, int L, int R){    if (L <= l && r <= R) return t[rt].cnt[0];    if (t[rt].lazy) PushDown(rt);    int mid = MID(l, r), ans = 0;    if (L <= mid) ans = Query(LC, L, R);    if (R > mid) ans += Query(RC, L, R);    return ans;} void Update(int rt, int l, int r, int L, int R){    if (L <= l && r <= R)    {        maintain_node(rt);        t[rt].lazy++;        return;    }    if (t[rt].lazy) PushDown(rt);    int mid = MID(l, r);    if (L <= mid) Update(LC, L, R);    if (R > mid) Update(RC, L, R);    Maintain(rt);} void Build(int rt, int l, int r){    if (l == r)    {        t[rt].cnt[0] = 1;        return;    }    int mid = MID(l, r);    Build(LC); Build(RC);    Maintain(rt);} int main(){    //ROP;    int T;    scanf("%d", &T);    while (T--)    {        MS(t, 0);        printf("Case %d:\n", ++cases);        int n, q;        scanf("%d%d", &n, &q);        Build(1, 1, n);        while (q--)        {            int a, b, c;            scanf("%d%d%d", &a, &b, &c);            b++, c++;            if (a == 0)     //increase                Update(1, 1, n, b, c);            else                printf("%d\n", Query(1, 1, n, b, c));        }    }    return 0;}
```
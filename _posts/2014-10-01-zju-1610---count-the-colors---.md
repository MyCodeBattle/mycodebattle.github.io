---
categories: Posts
date: 2014-10-01 00:00:00
title: ZJU 1610 - Count the Colors (线段树 + 区间修改)
tags: []
layout: post
---

#  [ZJU 1610 - Count the Colors (线段树 + 区间修改)](/2014/10/ZJU-1610/ "ZJU 1610 - Count the Colors \(线段树 + 区间修改\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Oct 2 2014 17:00

**Contents**

  1. 1. 代码

## 代码

基础题
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <ctime>#include <cstdlib>#include <fstream>#include <string>#include <sstream>#include <map>#include <cmath>#define LL long long#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 8000 + 5;const int MOD = 20071027; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int col[MAXN << 2], cnt, vis[MAXN];map<int, int> mp; void PushDown(int rt){    if (col[rt] != -1)    {        col[LRT] = col[RRT] = col[rt];        col[rt] = -1;        return;    }} void Query(int rt, int l, int r){    if (col[rt] != -1)    {        fill(vis + l, vis + r + 1, col[rt]);        return;    }    if (l == r) return;    int mid = MID(l, r);    Query(LC); Query(RC);} void Update(int rt, int l, int r, int L, int R, int val){    if (L <= l && r <= R)    {        col[rt] = val;        return;    }    PushDown(rt);    int mid = MID(l, r);    if (L <= mid) Update(LC, L, R, val);    if (R > mid) Update(RC, L, R, val);} int main(){    //ROP;    int n, i, j;    while (~scanf("%d", &n))    {        cnt = 0;        MS(col, -1), MS(vis, -1);        mp.clear();        int a, b, c;        for (i = 0; i < n; i++)        {            scanf("%d%d%d", &a, &b, &c);            Update(1, 1, 8000, a + 1, b, c);        }        Query(1, 1, 8000);        for (i = 1; i < MAXN; i++)        {            if (vis[i] != -1)            {                for (j = i; j <= MAXN && vis[j] == vis[i]; j++);                mp[vis[i]]++;                i = j - 1;            }        }        for (map<int, int>::iterator it = mp.begin(); it != mp.end(); it++)            printf("%d %d\n", it->F, it->S);        puts("");    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - ZJU](/tags/Online-Judge-ZJU/)[Data Structure - Seg Tree](/tags/Data-Structure-Seg-Tree/)

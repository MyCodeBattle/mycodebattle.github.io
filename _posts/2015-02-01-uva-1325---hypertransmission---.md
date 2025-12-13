---
categories: Posts
date: 2015-02-01 00:00:00
title: UVa 1325 - Hypertransmission (思维 + 扫描)
tags: []
layout: post
---

#  [UVa 1325 - Hypertransmission (思维 + 扫描)](/2015/02/UVa-1325/ "UVa 1325 - Hypertransmission \(思维 + 扫描\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Feb 12 2015 12:58

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

每个星球可以收到两种广播，一种是自己人，一种是敌对势力。现在敌对势力想使星球收到的敌对广播大于自己人广播，并且使这样的星球数量最大。

在数量一样大的时候，广播的距离越小越好。

现在求最大数量和前提下的最小距离。

## 思路

答案一定在星球的两两距离之中。

所以可以求出两两距离，排序，从小的开始统计。因为半径加大，之前的答案一定是满足的。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104

| 
    
    
    #include <stack>#include <cstdio>#include <list>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1const double PI = acos(-1.0); LL INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 1000 + 10;const int MOD = 1e9 + 7;const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };int cases = 0;typedef pair<int, int> pii; struct POINT{    int x, y, z, type, cnt; }p[MAXN]; struct EDGE{    int l, r, len;    bool operator < (const EDGE &a) const    {        return len < a.len;    }}; int Dis(POINT a, POINT b){    return (a.x-b.x) * (a.x-b.x) + (a.y-b.y) * (a.y-b.y) + (a.z-b.z) * (a.z-b.z);} vector<EDGE>edges; int main(){    //ROP;    int n;    while (~scanf("%d", &n))    {        edges.clear();        int a, b, c, type;        for (int i = 0; i < n; i++)        {            scanf("%d%d%d%d", &p[i].x, &p[i].y, &p[i].z, &p[i].type);            p[i].cnt = 1;        }        for (int i = 0; i < n; i++)            for (int j = i+1; j < n; j++) edges.PB((EDGE){i, j, Dis(p[i], p[j])});        sort(edges.begin(), edges.end());        int tmp = 0, i, j;        pair<int, double> ans;        for (i = 0; i < SZ(edges); )        {            for (j = i; j < SZ(edges) && edges[i].len == edges[j].len; j++)            {                int a = edges[j].l, b = edges[j].r;                if (p[a].type != p[b].type)                {                    if (--p[a].cnt == -1) tmp++;                    if (--p[b].cnt == -1) tmp++;                }                else                {                    if (++p[a].cnt == 0) tmp--;                    if (++p[b].cnt == 0) tmp--;                }            }            if (tmp > ans.X)                ans.X = tmp, ans.Y = edges[i].len;            i = j;        }        printf("%d\n%.6f\n", ans.X, sqrt(ans.Y));    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Foundation - Jizhi](/tags/Foundation-Jizhi/)

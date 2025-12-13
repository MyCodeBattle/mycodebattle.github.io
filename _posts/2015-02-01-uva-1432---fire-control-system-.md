---
categories: Posts
date: 2015-02-01 00:00:00
title: UVa 1432 - Fire-Control System (思维)
tags: []
layout: post
---

#  [UVa 1432 - Fire-Control System (思维)](/2015/02/UVa-1432/ "UVa 1432 - Fire-Control System \(思维\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Feb 27 2015 21:53

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

输出最小面积的扇形，最少覆盖k个点。

## 思路

对于半径，只能全部枚举。

在枚举某个半径时，把在那个半径之内的点都放到一个数组里，这个数组是按角度排序的。然后选出最小的角度，维护最小面积。

一开始弄错了。

比如某个半径下的数组有3个点, k = 2。我只计算了1、2， 2、3。其实还应该计算3、1！！

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879808182838485868788899091929394959697

| 
    
    
    #include <stack>#include <cstdio>#include <list>#include <cassert>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 5e3 + 10;const int MOD = 9901;const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };int cases = 0;typedef pair<int, int> pii; struct POINT{    int r;    double deg;    bool operator < (const POINT &a) const    {        return deg < a.deg;    }}P[MAXN]; vector<int> rr;int main(){    //ROP;    //freopen("out.txt", "w", stdout);    int n, k;    while (scanf("%d%d", &n, &k), n+k)    {        rr.clear();        for (int i = 0; i < n; i++)        {            int x, y;            scanf("%d%d", &x, &y);            P[i].deg = atan2(y, x) * 180/PI;            if (P[i].deg < 0) P[i].deg += 360;            P[i].r = x*x + y*y;            rr.PB(P[i].r);        }        printf("Case #%d: ", ++cases);        if (k == 0) { printf("0.00\n"); continue; }        double ans = INF;        sort(P, P+n);        sort(rr.begin(), rr.end());        int len = unique(rr.begin(), rr.end()) - rr.begin();        for (int i = 0; i < len; i++)        {            vector<double> tmpAns;            const int r = rr[i];            const double A = PI*r/360;            for (int j = 0; j < n; j++)                if (P[j].r <= r) tmpAns.PB(P[j].deg);            double minDeg = INF;            if (SZ(tmpAns) < k) continue;            int tmp = SZ(tmpAns);            for (int j = 0; j < tmp; j++) tmpAns.PB(tmpAns[j] + 360);            for (int j = 0; j+k-1 < SZ(tmpAns); j++)            {                int tar = j+k-1;                minDeg = min(minDeg, tmpAns[tar] - tmpAns[j]);            }            ans = min(ans, minDeg*A);        }        printf("%.2f\n", ans);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Foundation - Brute Force](/tags/Foundation-Brute-Force/)

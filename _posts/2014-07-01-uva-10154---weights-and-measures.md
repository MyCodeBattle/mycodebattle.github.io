---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 10154 - Weights and Measures
tags: []
layout: post
---

## 传送门

[UVa 10154 - Weights and Measures](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=114&problem=1095&mosmsg=Submission+received+with+ID+13870908)

## 题意

给出几只乌龟的自身重量和负重量，求最多能叠几只乌龟

## 思路

参考了[Staginner的解题报告](http://www.cnblogs.com/staginner/archive/2011/11/30/2268497.html)  
引用一下他的解释

> 首先，我们不妨证明一下这个命题，如果一个力量小的乌龟可以驮着一个力量大的乌龟，那么这个力量大的乌龟也必然可以驮起这个力量小的乌龟，而且还能够使两个乌龟上方增加承重能力。
> 
> 我们不妨设力量小的乌龟的重量和力量分别为w1、s1，而力量大的乌龟为w2、s2，由于乌龟1可以驮起乌龟2，那么有$s_1>=w_1+w_2$，如果我们假设乌龟2驮不起乌龟1，那么就应该有$s_2>s_1 >= w_1+w_2$，这样就产生矛盾了，原命题得证。
> 
> 接着，如果乌龟1在乌龟2的下面，两龟上方的承重能力至多为$s_1-(w_1+w_2)$。然而如果换成乌龟2在乌龟1的下面的话，对于乌龟1来讲是无所谓的，因为之前驮得动，现在少了乌龟2肯定也驮得动，因此仅从乌龟1的承重限制来讲，两龟上方的承重能力增加了。当然仅凭乌龟1的承重限制的角度来看是不全面的，我们还要考虑乌龟2，对于乌龟2来讲，两龟承重能力是$s_2-(w_1+w_2)$，而前面也说到了，乌龟1在下的时候承重能力至多为$s1-(w1+w2)$，而$s2-(w1+w2)>s1-(w1+w2)$，因此从乌龟2的角度来讲，尽管上面多了个乌龟1，但就乌龟1和乌龟2作为整体而言，他们上方的承重能力也一定增加了。因此，无论两龟整体的承重能力取决于哪只龟，调换之后最终的整体承重能力一定增加了。

简单来说，就是如果能叠上去的话，承受力越大的放下面越好。

所以就可以把乌龟按承受能力排序，$dp[i][j]$表示前i只乌龟叠了j只的最小重量。

状态转移方程$$dp[i][j] = min(dp[i - 1][j - 1] + w[i], dp[i - 1][j])$$

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647

| ```c++
#include <cstdio>#include <cstring>#include <algorithm>using namespace std;const int INF = 0x3f3f3f3f;const int MAXN = 6000; struct TURTLE{    int w, s;    bool operator < (const TURTLE &a) const    {        return s < a.s;    }}; int dp[MAXN][MAXN];TURTLE tur[MAXN]; int main(){    //freopen("input.txt", "r", stdin);    int i, j, n = 1, a, b;    while (~scanf("%d%d", &tur[n].w, &tur[n].s))        n++;    n--;    sort(tur + 1, tur + 1 + n);    for (i = 0; i <= n; i++)        for (j = 1; j <= n; j++)            dp[i][j] = INF;    for (i = 0; i <= n; i++)        dp[i][0] = 0;    for (i = 1; i <= n; i++)        for (j = 1; j <= i; j++)        {            dp[i][j] = dp[i - 1][j];            if (dp[i - 1][j - 1] + tur[i].w <= tur[i].s && dp[i - 1][j - 1] != INF)                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + tur[i].w);        }        for (i = n; i; i--)            if (dp[n][i] != INF)            {                printf("%d\n", i);                break;            }    return 0;}
```
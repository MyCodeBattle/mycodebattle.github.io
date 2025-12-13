---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 11235 - Frequent values
tags: []
layout: post
---

#  [UVa 11235 - Frequent values](/2014/08/UVa-11235/ "UVa 11235 - Frequent values")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Aug 24 2014 22:07

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 11235 - Frequent values](http://www.bnuoj.com/v3/problem_show.php?pid=19653)

## 题意

给出非降序排列的数，给一个范围，问出现最多的数字的次数

## 思路

大白上的例题。  
照着林燕同学的代码写了一遍。。。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879808182

| 
    
    
    #include <bits/stdc++.h>#define LL long long#define lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)using namespace std;const int MAXN = 1e5 + 5;const int INF = 0x3f3f3f3f; struct SEG{    int v, cnt;}seg[MAXN]; struct POS{    int num, l, r;}pos[MAXN]; int nseg, dp[MAXN][30]; void RMQInit(){    for (int i = 1; i <= nseg; i++)        dp[i][0] = seg[i].cnt;    for (int j = 1; (1 << j) <= nseg; j++)        for (int i = 1; i + (1 << j) - 1 <= nseg; i++)            dp[i][j] = max(dp[i][j - 1], dp[i + (1 << (j - 1))][j - 1]);} int RMQ(int l, int r){    if (l > r)        return 0;    int k = 0;    while ((1 << (k + 1)) <= r - l + 1) k++;    return max(dp[l][k], dp[r - (1 << k) + 1][k]);} int main(){    //freopen("input.txt", "r", stdin);    int nnum, nq, i, j, l, r, a;    while (scanf("%d", &nnum), nnum)    {        scanf("%d", &nq);        nseg = 0;        for (i = 1; i <= nnum; i++)        {            scanf("%d", &a);            if (nseg == 0 || seg[nseg].v != a)            {                seg[++nseg].v = a;                seg[nseg].cnt = 1;            }            else                seg[nseg].cnt++;            pos[i].num = nseg;        }        int lmax = 1, rmax = seg[1].cnt;        int k = 1;        for (i = 1; i <= nseg; i++)        {            for (j = 1; j <= seg[i].cnt; j++)            {                pos[k].l = lmax;                pos[k++].r = rmax;            }            lmax += seg[i].cnt;            rmax += seg[i + 1].cnt;        }        RMQInit();        while (nq--)        {            scanf("%d%d", &l, &r);            if (pos[l].num == pos[r].num)   //if they are in the same segment                printf("%d\n", r - l + 1);            else                printf("%d\n", max(pos[l].r - l + 1, max(r - pos[r].l + 1, RMQ(pos[l].num + 1, pos[r].num - 1))));        }    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Data Structure - RMQ](/tags/Data-Structure-RMQ/)

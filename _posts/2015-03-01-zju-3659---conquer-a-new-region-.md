---
categories: Posts
date: 2015-03-01 00:00:00
title: ZJU 3659 - Conquer a New Region (并查集)
tags: []
layout: post
---

#  [ZJU 3659 - Conquer a New Region (并查集)](/2015/03/ZJU-3659/ "ZJU 3659 - Conquer a New Region \(并查集\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Mar 14 2015 18:41

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

一个点到另外一个点的最大运输量是路上容量的最小值。现在要求某个点到其他全部点的最大运输量。

## 思路

很神奇的思路。

分析可知一条边约数着两边的点。

所以把边从大到小排序。

对于边上的两个点，如果起点在左边部分，显然从左边到右边各个点的路径为当前边的权值，这时候的答案是`lans = sum[l] + cnt[r]*weigh`。同理可得起点在右边部分。

然后两两合并，最后得出答案。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162

| 
    
    
    struct EDGE{    int l, r;    LL weigh;    bool operator < (const EDGE &a) const    {        return weigh > a.weigh;    }}; struct NODE{    int cnt;    LL sum;}node[MAXN]; vector<EDGE> e;int p[MAXN]; int Find(int n){    return p[n] = (n == p[n] ? n : Find(p[n]));} int main(){    //ROP;    int n;    while (~scanf("%d", &n))    {        e.clear(); MS(node, 0);        for (int i = 1; i <= n; i++) p[i] = i, node[i].cnt = 1;        for (int i = 0; i < n-1; i++)        {            int a, b;            LL c;            scanf("%d%d%lld", &a, &b, &c);            e.PB((EDGE){a, b, c});        }        sort(e.begin(), e.end());        LL ans = 0;        for (int i = 0; i < n-1; i++)        {            EDGE cur = e[i];            int u = Find(p[cur.l]), v = Find(p[cur.r]);            LL lans = node[u].sum + node[v].cnt*cur.weigh, rans = node[v].sum + node[u].cnt*cur.weigh;            if (lans > rans)            {                node[u].sum = lans; node[u].cnt += node[v].cnt;                p[v] = u;            }            else            {                node[v].sum = rans; node[v].cnt += node[u].cnt;                p[u] = v;            }            ans = max(max(lans, rans), ans);        }        printf("%lld\n", ans);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - ZJU](/tags/Online-Judge-ZJU/)[Data Structure - Disjoint Set](/tags/Data-Structure-Disjoint-Set/)

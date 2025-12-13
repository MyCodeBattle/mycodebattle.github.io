---
categories: Posts
date: 2015-03-01 00:00:00
title: HDU 5188 - zhx and contest (排序 + 背包)
tags: []
layout: post
---

#  [HDU 5188 - zhx and contest (排序 + 背包)](/2015/03/HDU-5188/ "HDU 5188 - zhx and contest \(排序 + 背包\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Mar 20 2015 23:42

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

给出每个任务完成时候的最小时间，权，做任务的时间，求完成目标权值的最少时间。

## 思路

按l-t排序，这样排出来以后可以证明交换任务顺序结果不会变得更差（不会）。

好像背包写得有点不优雅跑了400ms。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758

| 
    
    
    struct POINT{    int l, t, v;    bool operator < (const POINT &a) const    {        return l-t < a.l-a.t;    }}p[MAXN]; int ans, maxTime, sum, remain[MAXN];int n, w; bool DFS(int curPos, int curTime, int curSum, int limit){    if (curTime > ans || curTime > limit) return false;    if (curSum >= w) return true;    if (curPos == n) return false;    if (curSum + remain[curPos] < w) return false;    if (DFS(curPos+1, max(curTime+p[curPos].t, p[curPos].l), curSum+p[curPos].v, limit)) return true;    if (DFS(curPos+1, curTime, curSum, limit)) return true;    return false;} int Solve(){    int l = 0, r = INF;    while (l < r)    {        int mid = MID(l, r);        if (DFS(0, 0, 0, mid)) ans = r = mid;        else l = mid+1;    }    return ans;} int main(){    //ROP;    while (~scanf("%d%d", &n, &w))    {        sum = 0, maxTime = 0, ans = INF;        for (int i = 0; i < n; i++)        {            scanf("%d%d%d", &p[i].t, &p[i].v, &p[i].l);            sum += p[i].v;        }        if (sum < w)        {            puts("zhx is naive!");            continue;        }        LL add = 0;        for (int i = 0; i < n; i++) remain[i] = sum-add, add += p[i].v;        sort(p, p+n);        printf("%d\n", Solve());    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - HDU](/tags/Online-Judge-HDU/)[DP - 背包](/tags/DP-背包/)

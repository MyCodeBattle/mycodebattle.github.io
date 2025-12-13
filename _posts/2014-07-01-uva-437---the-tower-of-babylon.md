---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 437 - The Tower of Babylon
tags: []
layout: post
---

#  [UVa 437 - The Tower of Babylon](/2014/07/UVa-437/ "UVa 437 - The Tower of Babylon")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jul 7 2014 23:09

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 437 - The Tower of Babylon](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=114&problem=378&mosmsg=Submission+received+with+ID+13846086)

## 题意

给出几个三维的矩形，每种数量不限。底面严格递增可以叠起来，求最长高。矩形三维可以随便换。

## 思路

因为只要比较底面，所以可以把一个矩形xyz变成xyz,xzy,yzx三种，每种的底面都不一样。然后和以前的矩形嵌套一样了。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475

| 
    
    
    #include <cstdio>#include <cstring>#include <algorithm>#include <vector>using namespace std;const int MAXN = 200; struct RECTAN{    int x, y, z;}; int n, dp[MAXN], mp[MAXN][MAXN];vector<RECTAN> ve; void Input(){    RECTAN temp;    int i;    for (i = 0; i < n; i++)    {        scanf("%d%d%d", &temp.x, &temp.y, &temp.z);        ve.push_back(temp);        swap(temp.y, temp.z);        ve.push_back(temp);        swap(temp.x, temp.z);        ve.push_back(temp);    }} bool isBigger(RECTAN a, RECTAN b){    if (a.x > a.y)        swap(a.x, a.y);    if (b.x > b.y)        swap(b.x, b.y);    if (a.x < b.x && a.y < b.y)        return true;    return false;} int DFS(int i){    int &ans = dp[i];    if (ans != -1)        return ans;    ans = 0;    for (int j = 0; j < ve.size(); j++)        if (mp[i][j])            ans = max(ans, DFS(j));    ans += ve[i].z;    return ans;} int main(){    //freopen("in.txt", "r", stdin);    int i, j, a, b, c, ans, cases = 1;    while (scanf("%d", &n), n)    {        memset(dp, -1, sizeof(dp));        memset(mp, 0, sizeof(mp));        ans = -1;        ve.clear();        Input();        for (i = 0; i < ve.size(); i++)            for (j = 0; j < ve.size(); j++)                if (isBigger(ve[i], ve[j]))                    mp[i][j] = 1;        for (i = 0; i < ve.size(); i++)            ans = max(ans, DFS(i));        printf("Case %d: maximum height = %d\n", cases++, ans);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Dynamic Programming](/tags/Dynamic-Programming/)[Online Judge - UVa](/tags/Online-Judge-UVa/)

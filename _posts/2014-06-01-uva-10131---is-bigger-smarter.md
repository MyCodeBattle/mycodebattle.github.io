---
categories: Posts
date: 2014-06-01 00:00:00
title: UVa 10131 - Is Bigger Smarter?
tags: []
layout: post
---

## 传送门

[UVa 10131 - Is Bigger Smarter?](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=114&problem=1072&mosmsg=Submission+received+with+ID+13813248)

## 题意

有人认为大象越大越聪明，我们不信，要找出越大越笨的数据。(浓缩才是精华  
按照

> W[a[1]] < W[a[2]] < … < W[a[n]]， S[a[1]] > S[a[2]] > … > S[a[n]]

的顺序找最长路。  
输出最长路。

## 思路

和那个多维矩形嵌套的题目一样，就不多说了。这次终于能自己做出来了，看来看解题报告是有效果的TAT。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263

| ```c++
#include <cstdio>#include <vector>using namespace std;const int MAXN = 1000 + 10;struct ELEPHANT{    int weigh, intel;};vector<ELEPHANT> ve;int mp[MAXN][MAXN], dp[MAXN];int DFS(int target){    int &ans = dp[target], temp;    if (ans > 0)        return ans;    ans = 1;    for (int i = 0; i < ve.size(); i++)        if (mp[target][i])        {            temp = DFS(i) + 1;            ans = max(temp, ans);        }    return ans;}void PrintAns(int pos){    printf("%d\n", pos + 1);    for (int i = 0; i < ve.size(); i++)        if (mp[pos][i] && dp[pos] == dp[i] + 1)        {            PrintAns(i);            break;        }}int main(){    //freopen("input.txt", "r", stdin);    int weigh, intel, i, j, ans = -1, pos;    ELEPHANT temp;    while (~scanf("%d%d", &temp.weigh, &temp.intel))        ve.push_back(temp);    for (i = 0; i < ve.size(); i++)        for (j = 0; j < ve.size(); j++)            if (ve[i].weigh < ve[j].weigh && ve[i].intel > ve[j].intel)                mp[i][j] = 1;    for (i = 0; i < ve.size(); i++)    {        int t = DFS(i);        if (ans < t)        {            ans = t;            pos = i;        }    }    printf("%d\n", ans);    PrintAns(pos);    return 0;}
```
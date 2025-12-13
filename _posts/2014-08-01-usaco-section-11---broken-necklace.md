---
categories: Posts
date: 2014-08-01 00:00:00
title: USACO Section 1.1 - Broken Necklace
tags: []
layout: post
---

#  [USACO Section 1.1 - Broken Necklace](/2014/08/USACO-1_1-beads/ "USACO Section 1.1 - Broken Necklace")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Aug 12 2014 9:10

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

把一串项链从任意一个位置切断，从两头向中间数，直到遇到不同颜色时候停止，求最大的相同颜色的数目。

## 思路

这题做得有点郁闷，捣鼓了很久。一开始交的时候竟然读不进数据，现在都不清楚原因。后来发现自己的思路有问题，又重新写了一遍（ ＴДＴ）

我的思路是$O(n^2)$暴力，判断每个点。

先把字符串复制两遍，这样就不用处理临界点了。如果端点是w，还要寻找适合这个端点的颜色。而且两边的扫描不能碰到一起，这样就多数了。。。总之考虑的不够全面。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879

| 
    
    
    /*ID: mycodeb1LANG: C++TASK: beads*/ #include <bits/stdc++.h>using namespace std; string str;int n; char FindBase(int i, char ch){    if (ch == 'L')    {        for (int ii = i - 1; ii >= i - n; ii++)            if (str[ii] != 'w')                return str[ii];        return 'w';    }    if (ch == 'R')        for (int ii = i; ii < i + n; ii++)            if (str[ii] != 'w')                return str[ii];    return 'w';} int main(){    //freopen("input.txt", "r", stdin);    freopen("beads.in", "r", stdin);    freopen("beads.out", "w", stdout);    ios::sync_with_stdio(false);     string temp;    int i, j, ans = 0;    cin >> n;    cin >> temp;    for (i = 0; i < 3; i++)        str += temp;    int st = n;    for (i = st; i < st + n; i++)    {        int led = -1, red = -2;        char ch;        int lcnt = 0, rcnt = 0;        ch = (str[i] == 'w' ? FindBase(i, 'L') : str[i - 1]);        for (j = i - 1; j >= i - n; j--)        {            if (str[j] == ch || str[j] == 'w')                lcnt++;            else            {                led = j + 1;                break;            }        }        if (lcnt == n)  //如果全是一样的颜色，直接输出        {            cout << n << endl;            return 0;        }        ch = (str[i] == 'w' ? FindBase(i, 'R') : str[i - 1]);        for (j = i; j < i + n && j != led + n; j++)        {            if (str[j] == ch || str[j] == 'w')                rcnt++;            else            {                red = j - 1;                break;            }        }        ans = max(ans, lcnt + rcnt);    }    cout << ans << endl;    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - USACO](/tags/Online-Judge-USACO/)[Foundation - Strings](/tags/Foundation-Strings/)[Foundation - Simulate](/tags/Foundation-Simulate/)

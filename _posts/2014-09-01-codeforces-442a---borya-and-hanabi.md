---
categories: Posts
date: 2014-09-01 00:00:00
title: Codeforces 442A - Borya and Hanabi
tags: []
layout: post
---

#  [Codeforces 442A - Borya and Hanabi](/2014/09/Codeforces-442A/ "Codeforces 442A - Borya and Hanabi")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 7 2014 10:31

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[Codeforces 442A - Borya and Hanabi](http://codeforces.com/contest/443/problem/C)

## 题意

小明有25种牌，每张有花色和数值，现在他知道手里有哪些牌，但是不知道哪个是哪个。  
旁边的人可以提示他花色，把某个花色的牌告诉他，或者数值，同理。

求最少提示次数。

## 思路

因为不用管提示的顺序，可以压缩一下再暴力。

考虑不合法的情况：

  1. 有某个属性被提示了两次。说明有两张牌没有被完全提示，这样这两张牌就分不清了。

  2. 有多余一张的牌一个属性也没被提示到。  
如果只有一张牌没有被提示到，其他的全部知道了，这张牌就可以确定。但是有两张牌就确定不了了。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970

| 
    
    
    #include <bits/stdc++.h>#define LL long long#define lowbit(x) ((x) & (-x))const int MAXN = 5000 + 5;const int INF = 0x3f3f3f3f;using namespace std; int sel[10], mp[10][10]; int Change(char *s){    if (s[0] == 'R') return 5;    if (s[0] == 'G') return 6;    if (s[0] == 'B') return 7;    if (s[0] == 'Y') return 8;    if (s[0] == 'W') return 9;} int main(){    //freopen("input.txt", "r", stdin);    int n, i, j;    scanf("%d", &n);    for (i = 0; i < n; i++)    {        char s[10];        scanf("%s", s);        int x = Change(s);        mp[x][s[1] - '1'] = 1;    }    int ans = 100;    for (int stat = 0; stat < (1 << 10); stat++)    {        memset(sel, 0, sizeof sel);        bool flag = true;        int temp = 0, emp = 0, modi = 0;        for (i = 0; i < 10; i++)            if (stat & (1 << i)) temp++;        if (temp >= ans)            continue;        for (i = 0; i < 5; i++)            for (j = 5; j < 10; j++)            {                if (mp[j][i])                {                    if (stat & (1 << i) && stat & (1 << j))                        continue;                    else if (stat & (1 << i))                    {                        sel[i]++;                        if (sel[i] > 1) flag = false;                    }                    else if (stat & (1 << j))                    {                        sel[j]++;                        if (sel[j] > 1) flag = false;                    }                    else                    {                        emp++;                        if (emp > 1) flag = false;                    }                    modi = 1;                }            }        if (flag && modi) ans = min(ans, temp);    }    printf("%d\n", ans);    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - Codeforces](/tags/Online-Judge-Codeforces/)[Foundation - Brute Force](/tags/Foundation-Brute-Force/)[Algorithm - SC](/tags/Algorithm-SC/)

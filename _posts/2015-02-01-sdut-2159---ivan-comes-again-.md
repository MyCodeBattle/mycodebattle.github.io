---
categories: Posts
date: 2015-02-01 00:00:00
title: SDUT 2159 - Ivan comes again! (模拟)
tags: []
layout: post
---

#  [SDUT 2159 - Ivan comes again! (模拟)](/2015/02/SDUT-2159/ "SDUT 2159 - Ivan comes again! \(模拟\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Feb 11 2015 23:46

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

给出一些命令，输出询问。

## 思路

模拟

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738

| 
    
    
    char s[10];multiset<pii> mp; int main(){    //ROP;    int n;    while (scanf("%d", &n), n)    {        mp.clear();        printf("Case %d:\n", ++cases);        for (int i = 0; i < n; i++)        {            scanf("%s", s);            int a, b;            scanf("%d%d", &a, &b);            if (s[0] == 'a')                mp.insert(MP(a, b));            if (s[0] == 'f')            {                mp.insert(MP(a, b));                multiset<pii>::iterator it = mp.find(MP(a, b)), tmp = it;                while (it != mp.end())                {                    if (it->X > a && it->Y > b) break;                    else it++;                }                if (it != mp.end()) printf("%d %d\n", it->X, it->Y);                if (it == mp.end()) puts("-1");                mp.erase(tmp);            }            if (s[0] == 'r')                mp.erase(MP(a, b));        }        puts("");    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - SDUT](/tags/Online-Judge-SDUT/)[Foundation - Simulate](/tags/Foundation-Simulate/)

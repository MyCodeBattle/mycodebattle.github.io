---
categories: Posts
date: 2014-12-01 00:00:00
title: Codeforces 492D - Vanya and Computer Game (二分)
tags: []
layout: post
---

## 题意

一只怪兽要被打X下才死，两个人的攻击频率各不同，求怪兽被谁打死。

## 思路

相当于第一个人y秒打一下，第二个人x秒打一下。

只要得知怪兽在第几秒被打死，就知道是被谁打死的。所以二分答案，得到怪兽惨死的时间，然后判断即可。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233

| ```c++
#include <cstdio>#include <iostream>using namespace std; const long long MAXN = 1e11 + 100; int main(){    ios::sync_with_stdio(0);         long long fx, fy, n;    cin >> n >> fx >> fy;    for (int i = 0; i < n; i++)    {        long long tmp, ans;        cin >> tmp;        long long l = 0, r = 1e15, mid;        while (l <= r)        {            mid = (l + r) >> 1;            if (mid / fx + mid / fy >= tmp)            {                ans = mid;                r = mid - 1;            }            else l = mid + 1;        }        if (ans % fx == 0 && ans % fy == 0) cout << "Both" << endl;        else if (ans % fy) cout << "Vova" << endl;        else cout << "Vanya" << endl;    }    return 0;}
```
---
categories: Posts
date: 2015-02-01 00:00:00
title: SDUT 2157 - Greatest Number (二分)
tags: []
layout: post
---

#  [SDUT 2157 - Greatest Number (二分)](/2015/02/SDUT-2157/ "SDUT 2157 - Greatest Number \(二分\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Feb 11 2015 23:47

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

选出4个以内的数，使得值最接近K。

## 思路

两两相加到一个数组里，枚举一个，另一个二分。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243

| 
    
    
    vector<int> arr, sum; int main(){    //ROP;    int n, limit;    while (~scanf("%d%d", &n, &limit), n + limit)    {        arr.clear(); sum.clear();        for (int i = 0; i < n; i++)        {            int a;            scanf("%d", &a);            if (a <= limit) arr.PB(a);        }        arr.PB(0);        for (int i = 0; i < SZ(arr); i++)            for (int j = i; j < SZ(arr); j++)                if (arr[i] + arr[j] <= limit) sum.PB(arr[i] + arr[j]);        sort(sum.begin(), sum.end());        int ans = 0;        for (int i = 0; i < SZ(sum); i++)        {            int cur = limit - sum[i];            int l = 0, r = SZ(sum), mid;            int tmp = 0;            while (l <= r)            {                mid = MID(l, r);                if (sum[mid] > cur) r = mid - 1;                else                {                    tmp = max(tmp, sum[mid]);                    l = mid + 1;                }            }            ans = max(ans, sum[i] + tmp);        }        printf("Case %d: %d\n", ++cases, ans);        puts("");    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - SDUT](/tags/Online-Judge-SDUT/)[Foundation - Jizhi](/tags/Foundation-Jizhi/)

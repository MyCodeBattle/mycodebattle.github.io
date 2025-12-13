---
categories: Posts
date: 2015-01-01 00:00:00
title: HDU 1492 - The number of divisors(约数) about Humble Numbers (唯一分解定理)
tags: []
layout: post
---

## 题意

找出每个合数有多少个因子

## 思路

唯一分解定理

## 代码
    
    
    123456789101112131415161718192021222324

| ```c++
int main(){    ios::sync_with_stdio(0);     LL n;    int arr[] = {2, 3, 5, 7};    int num[10];    while (cin >> n, n)    {        MS(num, 0);        for (int i = 0; i < 4; i++)        {            while (n % arr[i] == 0)            {                num[arr[i]]++;                n /= arr[i];            }        }        LL ans = 1;        for (int i = 0; i < 4; i++) ans *= (num[arr[i]] + 1);        cout << ans << endl;    }    return 0;}
```
---
categories: Posts
date: 2014-08-01 00:00:00
title: USACO Section 1.2 - Dual Palindromes
tags: []
layout: post
---

## 题意

找出大于s，且在十进制以内有两次以上是回文串的数字。

## 思路

改一下上一题就行。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960

| ```c++
/*ID: mycodeb1LANG: C++TASK: dualpal*/ #include <bits/stdc++.h>using namespace std;const int WMAXN = 5000;const char cstr[] = "0123456789"; string str;int base; string Convert(int num){    str.clear();    int k = 0;    while (num)    {        str += cstr[num % base];        num /= base;    }    return str;} bool isOK(string s){    int len = s.length();    for (int i = 0, j = len - 1; i < j; i++, j--)        if (s[i] != s[j])            return false;    return true;} int main(){    freopen("dualpal.in", "r", stdin);    freopen("dualpal.out", "w", stdout);    ios::sync_with_stdio(false);     int i, j, n, s, cnt;    scanf("%d%d", &n, &s);    for (cnt = 0, i = s + 1; cnt < n; i++)    {        int ccnt = 0;        for (base = 2; base <= 10; base++)            if (isOK(Convert(i)))            {                ccnt++;                if (ccnt == 2)                {                    cnt++;                    cout << i << endl;                    break;                }            }    }    return 0;}
```
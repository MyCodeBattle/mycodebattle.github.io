---
categories: Posts
date: 2015-03-01 00:00:00
title: HDU 4287 - Intelligent IME (思维)
tags: []
layout: post
---

#  [HDU 4287 - Intelligent IME (思维)](/2015/03/HDU-4287/ "HDU 4287 - Intelligent IME \(思维\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Mar 6 2015 17:03

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

给出输入的字符，再给出按手机键盘的方式，问弹出几种已经输入的字符。

## 思路

直接映射。

这个专题的题目有点水。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132

| 
    
    
    map<char, int> mp;map<int, int> ans;string word[] = {"abc","def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};int arr[MAXN];char buf[20]; int main(){   // ROP;    int T;    scanf("%d", &T);    for (int i = 0; i < 8; i++)        for (int j = 0; j < SZ(word[i]); j++)            mp[word[i][j]] = i+2;    while (T--)    {        ans.clear();        int n, k;        scanf("%d%d", &n, &k);        for (int i = 0; i < n; i++) scanf("%d", &arr[i]);        for (int i = 0; i < k; i++)        {            int tmp = 0;            scanf("%s", buf);            for (int j = 0; j < strlen(buf); j++) tmp = tmp*10 + mp[buf[j]];            ans[tmp]++;        }        for (int i = 0; i < n; i++)            printf("%d\n", ans[arr[i]]);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - HDU](/tags/Online-Judge-HDU/)[Foundation - Jizhi](/tags/Foundation-Jizhi/)

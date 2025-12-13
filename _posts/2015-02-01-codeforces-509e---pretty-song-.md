---
categories: Posts
date: 2015-02-01 00:00:00
title: Codeforces 509E - Pretty Song (思维)
tags: []
layout: post
---

#  [Codeforces 509E - Pretty Song (思维)](/2015/02/codeforces-509e/ "Codeforces 509E - Pretty Song \(思维\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Feb 1 2015 16:49

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

计算一个只包含01的字符串。

对于他的一个子串s，$value(s) = \frac {\text {s中1的和} }{\text {s的长度} }$

要求计算所有子串的value值。

## 思路

可以统计每个字符被计算了多少次，用前缀和计算。

当子串长度len为1时，显然每个字符被计算了一次。`cnt = sum[n] - sum[0]`

len = 2时，第一个和最后一个字符只被计算一次，其他的都被计算两次。所以这时候他们的和是`cnt += sum[n-1] - sum[1]`

以此类推。

## 代码
    
    
    12345678910111213141516171819202122232425262728

| 
    
    
    char str[MAXN];int sum[MAXN]; bool Check(char s){    if (s == 'A' || s == 'E' || s == 'I' || s == 'O' || s == 'U' || s == 'Y') return true;    return false;} int main(){    //ROP;    scanf("%s", str + 1);    int len = strlen(str + 1);    for (int i = 1; i <= len; i++)        sum[i] = sum[i-1] + (Check(str[i]) ? 1 : 0);    int l = 0, r = len;    double ans = 0;    LL cnt = 0;    for (int i = 1; i <= len; i++)    {        cnt += sum[r] - sum[l];        ans += cnt*1.0 / i;        r--, l++;    }    printf("%.10f\n", ans);    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - Codeforces](/tags/Online-Judge-Codeforces/)[Foundation - Jizhi](/tags/Foundation-Jizhi/)

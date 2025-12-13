---
categories: Posts
date: 2014-09-01 00:00:00
title: LeetCode - Pow(x, n)
tags: []
layout: post
---

#  [LeetCode - Pow(x, n)](/2014/09/leetcode-pow/ "LeetCode - Pow\(x, n\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 21 2014 17:20

**Contents**

  1. 1. 思路
  2. 2. 代码

## 思路

一开始直接交了一发pow(x, n)，RE了。

后来按正常的方法写了一发，TLE了。

只能用快速幂

注意处理n < 0的情况。

## 代码
    
    
    12345678910111213141516171819

| 
    
    
    class Solution {public:    double pow(double a, int m)    {        if (a == 1) return 1;        if (a == 0) return 0;        bool flag = m > 0 ? false : true;        if (flag) m = -m;        double ans = 1;        while (m > 0)        {            if (m & 1)                ans = ans * a;            a = a * a;            m >>= 1;        }        return flag ? 1 / ans : ans;    }};  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - LeetCode](/tags/Online-Judge-LeetCode/)[Math - Number Theory](/tags/Math-Number-Theory/)

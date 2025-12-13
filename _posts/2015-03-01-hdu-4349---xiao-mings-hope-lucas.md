---
categories: Posts
date: 2015-03-01 00:00:00
title: HDU 4349 - Xiao Ming's Hope (Lucas定理)
tags: []
layout: post
---

#  [HDU 4349 - Xiao Ming's Hope (Lucas定理)](/2015/03/HDU-4349/ "HDU 4349 - Xiao Ming's Hope \(Lucas定理\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Mar 24 2015 16:23

**Contents**

  1. 1. 题意
  2. 2. 代码

## 题意

题目就是求$C_n^m \bmod 2 == 1$

由Lucas定理，转化到二进制下。

当n = 0时，m对应的位必须是0.当n=1时，随意。

所以最后的答案是$(1<<Number_of_Two(n))$

## 代码
    
    
    1234567

| 
    
    
    int main(){    int n;    while (~scanf("%d", &n))        printf("%d\n", (1<<__builtin_popcount(n)));    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - HDU](/tags/Online-Judge-HDU/)[Math - Combinatorics](/tags/Math-Combinatorics/)

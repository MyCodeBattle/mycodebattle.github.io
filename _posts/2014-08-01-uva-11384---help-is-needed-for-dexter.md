---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 11384 - Help is needed for Dexter
tags: []
layout: post
---

#  [UVa 11384 - Help is needed for Dexter](/2014/08/UVa-11384/ "UVa 11384 - Help is needed for Dexter")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Aug 26 2014 18:23

**Contents**

  1. 1. 传送门
  2. 2. 代码

## 传送门

[UVa 11384 - Help is needed for Dexter](http://www.bnuoj.com/v3/problem_show.php?pid=19802)

## 代码
    
    
    123456789101112131415161718

| 
    
    
    #include <cstdio>using namespace std; int Fun(int n){    if (n == 1)        return 1;    return Fun(n / 2) + 1;} int main(){    //freopen("input.txt", "r", stdin);    int n, i, j;    while (~scanf("%d", &n))        printf("%d\n", Fun(n));    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Foundation - Others](/tags/Foundation-Others/)

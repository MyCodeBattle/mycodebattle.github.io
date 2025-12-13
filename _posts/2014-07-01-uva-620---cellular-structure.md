---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 620 - Cellular Structure
tags: []
layout: post
---

#  [UVa 620 - Cellular Structure](/2014/07/UVa-620/ "UVa 620 - Cellular Structure")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jul 8 2014 16:21

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 620 - Cellular Structure](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=114&problem=561&mosmsg=Submission+received+with+ID+13850021)

## 题意

细胞有三种增长方式。O代表现在的情况。  
一种是变成A，一种是做后面加AB，一种是在前面加B，后面加A。要求输出现在的阶段。

## 思路

记得以前做过一道一样的题目。根据给的字符串进行比较即可。

## 代码
    
    
    123456789101112131415161718192021222324252627

| 
    
    
    #include <cstdio>#include <iostream>#include <string>using namespace std; int main(){    //freopen("in.txt", "r", stdin);    int T, i, j;    string str;    scanf("%d", &T);    while (cin >> str)    {        int len = str.size();        if (len % 2 == 0)            printf("MUTANT\n");        else if (len == 1 && str[0] == 'A')            printf("SIMPLE\n");        else if (len >= 3 && str[len - 1] == 'B' && str[len - 2] == 'A')            printf("FULLY-GROWN\n");        else if (len >= 3 && str[0] == 'B' && str[len - 1] == 'A')            printf("MUTAGENIC\n");        else            printf("MUTANT\n");    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Dynamic Programming](/tags/Dynamic-Programming/)[Online Judge - UVa](/tags/Online-Judge-UVa/)

---
categories: Posts
date: 2014-09-01 00:00:00
title: CodeForces 467A - 24 Game
tags: []
layout: post
---

#  [CodeForces 467A - 24 Game](/2014/09/codeforces-467a/ "CodeForces 467A - 24 Game")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 21 2014 21:22

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

给出n，输出算出24点的步骤。

## 思路

参考了某大神的思路。

可以得出n<=3时不成立，n = 4 或者 n = 5的时候可以手写出来。当以后的n是偶数时，可以n - (n - 1)，1 * 前面算出来的24，同理n为奇数时。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <cstring>#include <string>#include <sstream>#include <map>#include <cmath>#define LL long long#define lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define ROP freopen("input.txt", "r", stdin);const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 1000 + 5; void Print(int n){    if (n == 4)    {        puts("2 * 3 = 6");        puts("4 * 6 = 24");        puts("1 * 24 = 24");    }    else if (n == 5)    {        puts("5 - 3 = 2");        puts("2 + 1 = 3");        puts("3 * 4 = 12");        puts("12 * 2 = 24");    }    else    {        if (n & 1)        {            Print(5);            while (n != 5)            {                printf("%d - %d = %d\n", n, n - 1);                printf("1 * 24 = 24\n");                n -= 2;            }        }        else        {            Print(4);            while (n != 4)            {                printf("%d - %d = 1\n", n, n - 1);                printf("1 * 24 = 24\n");                n -= 2;            }        }    }} int main(){    int n;    scanf("%d", &n);    if (n <= 3) printf("NO\n");    else    {        printf("YES\n");        Print(n);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - Codeforces](/tags/Online-Judge-Codeforces/)[Foundation - Construction](/tags/Foundation-Construction/)

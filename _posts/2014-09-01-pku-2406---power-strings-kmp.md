---
categories: Posts
date: 2014-09-01 00:00:00
title: PKU 2406 - Power Strings (KMP性质的应用)
tags: []
layout: post
---

#  [PKU 2406 - Power Strings (KMP性质的应用)](/2014/09/PKU-2406/ "PKU 2406 - Power Strings \(KMP性质的应用\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 30 2014 11:04

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

输出整个字符串中的最短循环节的数目

## 思路

和上一题一样。

> 若len可以被len - next[len]整除，则最大循环次数n为len/(len - next[len])，否则为1。

例子证明，引用自<http://www.cppblog.com/Davidlrzh/articles/115751.html>

> 设S=q1q2q3q4q5q6q7q8，并设next[9] = 6，此时str = S[len - next[len]] = q1q2，由字符串特征向量next的定义可知，q1q2q3q4q5q6 = q3q4q5q6q7q8，即有q1q2＝q3q4，q3q4＝q5q6，q5q6＝q7q8.
> 
> 即q1q2为循环子串，且易知为最短循环子串。由以上过程可知，若len可以被len - next[len]整除，则S存在循环子串，否则不存在。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <ctime>#include <cstdlib>#include <fstream>#include <string>#include <sstream>#include <map>#include <cmath>#define LL long long#define lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 1e6 + 5;const int MOD = 20071027; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; char str[MAXN];int f[MAXN], len, ans; void GetFail(){    f[0] = f[1] = 0;    for (int i = 1; i < len; i++)    {        int j = f[i];        while (j && str[j] != str[i])j = f[j];        f[i + 1] = (str[j] == str[i] ? j + 1 : 0);    }} void KMP(){    GetFail();    int j = 0;    if (f[len] && len % (len - f[len]) == 0) ans = len / (len - f[len]);    else ans = 1;}  int main(){    //ROP;    int i, j;    while (scanf("%s", str), str[0] != '.')    {        ans = 0;        len = strlen(str);        KMP();        printf("%d\n", ans);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - PKU](/tags/Online-Judge-PKU/)[Algorithm - KMP](/tags/Algorithm-KMP/)

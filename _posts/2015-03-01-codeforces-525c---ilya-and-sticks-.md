---
categories: Posts
date: 2015-03-01 00:00:00
title: Codeforces 525C - Ilya and Sticks (贪心)
tags: []
layout: post
---

#  [Codeforces 525C - Ilya and Sticks (贪心)](/2015/03/codeforces-525c/ "Codeforces 525C - Ilya and Sticks \(贪心\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Mar 27 2015 16:05

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

给出一堆数字，可以减一。问能组成的最大面积和。

## 思路

从大往小选，算一下。

一开始用队列模拟T了。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100

| 
    
    
    #include <stack>#include <stdio.h>#include <list>#include <cassert>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 1e6 + 10;const int MOD = 9901;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };int cases = 0;typedef pair<int, int> pii; int l[MAXN]; //适用于正负数,(int,long long,float,double)template <class T>bool Read(T &ret){    char c; int sgn; T bit=0.1;    if(c=getchar(),c==EOF) return 0;    while(c!='-'&&c!='.'&&(!isdigit(c))) c=getchar();    sgn=(c=='-')?-1:1;    ret=(c=='-')?0:(c-'0');    while(c=getchar(),isdigit(c)) ret=ret*10+(c-'0');    if(c==' '||c=='\n'){ ret*=sgn; return 1; }    while(c=getchar(),isdigit(c)) ret+=(c-'0')*bit,bit/=10;    ret*=sgn;    return 1;} int GetLong(){    LL last = 0, ans = 0;    for (LL i = MAXN-1; i >= 2; i--)    {        int cnt = 0;        if (l[i])        {            if (l[i+1])            {                cnt++;                l[i]--;            }            cnt += l[i]/2;            if (cnt && last)            {                ans += last*i, cnt--;                last = 0;            }            l[i] = l[i] % 2;            ans += i*i*(cnt>>1);            if (cnt&1) last = i;        }    }    printf("%I64d\n", ans);} int main(){    //ROP;    int n;    scanf("%d", &n);    for (int i = 0; i < n; i++)    {        int tmp;        Read(tmp);        l[tmp]++;    }    GetLong();    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - Codeforces](/tags/Online-Judge-Codeforces/)[Foundation - Jizhi](/tags/Foundation-Jizhi/)

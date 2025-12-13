---
categories: Posts
date: 2014-09-01 00:00:00
title: HDU 5019 - Revenge of GCD
tags: []
layout: post
---

#  [HDU 5019 - Revenge of GCD](/2014/09/HDU-5019/ "HDU 5019 - Revenge of GCD")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 19 2014 22:02

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

找出两个数的第k大公约数，如果不存在输出-1

## 思路

就是找最大公约数的第k大因子。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960

| 
    
    
    #include <cstdio>#include <algorithm>#include <functional>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <cstring>#include <string>#include <sstream>#include <map>#include <cmath>#define LL long long#define lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define ROP freopen("input.txt", "r", stdin);const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std; const int MAXN = 1000 + 5; int cnt;vector<LL> ve; int main(){    //ROP;    int T;    cin >> T;    while (T--)    {        ve.clear();        LL a, b, k;        cin >> a >> b >> k;        LL ans = __gcd(a, b);        ve.push_back(1ll);        if (ans != 1) ve.push_back(ans);        for (LL i = 2; i <= (LL)sqrt(ans * 1.0); i++)        {            int t = ans % i;            if (t == 0)            {                ve.PB(i);                if (ans / i != i) ve.PB(ans / i);            }        }        if (k > ve.size()) cout << "-1" << endl;        else        {            nth_element(ve.begin(), ve.begin() + k - 1, ve.end(), greater<LL>());            cout << ve[k - 1] << endl;        }    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - HDU](/tags/Online-Judge-HDU/)[Math - Number Theory](/tags/Math-Number-Theory/)

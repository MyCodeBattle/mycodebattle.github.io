---
categories: Posts
date: 2015-02-01 00:00:00
title: HDU 2650 - A math problem (高斯素数扩展)
tags: []
layout: post
---

#  [HDU 2650 - A math problem (高斯素数扩展)](/2015/02/HDU-2650/ "HDU 2650 - A math problem \(高斯素数扩展\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Feb 19 2015 18:10

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

判断一个高斯整数是不是高斯素数。

## 思路

对于一个高斯整数$a+bi$。

  * 如果$a = 0 || b = 0$，判断另一个数是不是形为$4n+3$或者$-(4n+3)$的素数
  * 判断$a^2 + b^2$是不是素数。如果是就是。

这题把$i^2$变成了$\sqrt {2}$，所以可以扩(Y)展(Y)一下，判断$a^2 + 2b^2$是不是素数。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768

| 
    
    
    #include <stack>#include <cstdio>#include <list>#include <cassert>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 2e3 + 10;const int MOD = 1e9 + 7;const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };const int hash_size = 4e5 + 10;int cases = 0;typedef pair<int, int> pii; int main(){    LL n, m;    while (cin >> n >> m)    {        bool flag = false;        if (n == 0)        {            if ((m+3) % 4 == 0 || (m-3) % 4 == 0) flag = true;        }        else        {            flag = true;            LL num = n*n + 2*m*m;            int k = sqrt(num + 0.5);            for (int i = 2; i <= k; i++)                if (num % i == 0)                {                    flag = false;                    break;                }        }        printf("%s\n", flag ? "Yes" : "No");    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - HDU](/tags/Online-Judge-HDU/)[Math - Number Theory](/tags/Math-Number-Theory/)

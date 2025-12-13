---
categories: Posts
date: 2015-01-01 00:00:00
title: PKU 1142 - Smith Numbers (数论)
tags: []
layout: post
---

#  [PKU 1142 - Smith Numbers (数论)](/2015/01/PKU-1142/ "PKU 1142 - Smith Numbers \(数论\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jan 22 2015 20:35

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

如果一个数是合数而且符合性质，找出比输入大的最小的这个数

## 思路

分解质因数

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879808182838485868788

| 
    
    
    #include <stack>#include <cstdio>#include <list>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)#define BitCountll(x) __builtin_popcountll(x)#define LeftPos(x) 32 - __builtin_clz(x) - 1#define LeftPosll(x) 64 - __builtin_clzll(x) - 1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 4e5 + 10;const int MOD = 1000007;const int dir[][2] = { {1, 0}, {0, 1} };int cases = 0;typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int rfrs; bool Check(int num){    int limit = sqrt(num + 0.5), origi = num;    int res = 0;    for (int i = 2; i <= limit; i++)    {        while (num % i == 0)        {             int tmp = i;             while (tmp) { res += tmp % 10; tmp /= 10; }             num /= i;        }    }    if (num == origi) return false;    else if (num != 1)        while (num) { res += num % 10; num /= 10; }    return res == rfrs;} int main(){    int n, i, j;    while (scanf("%d", &n), n)    {        n++;        while (true)        {            rfrs = 0;            int tmp = n;            while (tmp) { rfrs += tmp % 10; tmp /= 10; }            if (Check(n))            {                printf("%d\n", n);                break;            }            else n++;        }    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - PKU](/tags/Online-Judge-PKU/)[Math - Number Theory](/tags/Math-Number-Theory/)

---
categories: Posts
date: 2014-11-01 00:00:00
title: ZJU 3233 - Lucky Number (容斥原理)
tags: []
layout: post
---

#  [ZJU 3233 - Lucky Number (容斥原理)](/2014/11/ZJU-3233/ "ZJU 3233 - Lucky Number \(容斥原理\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Nov 21 2014 15:02

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

找出[low, high]之间数的数量，符合下面两个条件。

  1. 至少被一个lucky数整除。
  2. 至少不被一个unLucky数整除。

## 思路

大思路是用容斥来统计。

  1. 如何统计数的数量？  
用前缀和的思想。

  2. 如何得出某个数以内符合条件的数量？  
ans = |条件一| - |条件一 && !条件2|.

就是说答案等于所有符合条件一的数量（这时候里面包含**能被全部unlucky整除的数量** 和**至少不被一个unlucky整除的数量** ）减去**能被全部unlucky整除的数量**

求出unlucky的LCM，然后和往常一样对lucky进行容斥即可。

注意LCM是有可能溢出的，这时候可以看成绝对满足条件2，只要求出条件1的数量即可。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <iomanip>#include <cmath>#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)#define BitCountll(x) __builtin_popcountll(x)#define LeftPos(x) 32 - __builtin_clz(x) - 1#define LeftPosll(x) 64 - __builtin_clzll(x) - 1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const double eps = 1e-6;const int MAXN = 1500 + 10;const int MOD = 1000007;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; LL lucky[MAXN], unlucky[MAXN], lcm, nLuc, nUnluc;bool flag; LL LCM(LL a, LL b){    return a / __gcd(a, b) * b;} LL Solve(LL num){    int totState = (1 << nLuc);    LL ans = 0;    for (int curState = 1; curState < totState; curState++)    {        LL pro = 1;        int cnt = 0;        for (int i = 0; i < nLuc; i++)        {            if ((1 << i) & curState)            {                pro = LCM(pro, lucky[i]);                cnt++;            }        }        if (cnt & 1)        {            if (flag) ans += num / pro;            else ans += num / pro - num / LCM(pro, lcm);        }        else        {            if (flag) ans -= num / pro;            else ans -= num / pro - num / LCM(pro, lcm);        }    }    return ans;} int main(){    //ROP;    int i, j;    LL low, high;    while (cin >> nLuc >> nUnluc >> low >> high, nLuc + nUnluc + low + high)    {        lcm = 1; flag = false;        for (j = 0; j < nLuc; j++) cin >> lucky[j];        for (i = 0; i < nUnluc; i++) cin >> unlucky[i];        for (int i = 0; i < nUnluc; i++) lcm = LCM(unlucky[i], lcm);        if (lcm < 0)        {            flag = true;            cout << Solve(high) - Solve(low - 1) << endl;        }        else cout << Solve(high) - Solve(low - 1) << endl;    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - ZJU](/tags/Online-Judge-ZJU/)[Math - Combinatorics](/tags/Math-Combinatorics/)

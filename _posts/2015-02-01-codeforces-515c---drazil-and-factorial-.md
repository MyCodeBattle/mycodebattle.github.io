---
categories: Posts
date: 2015-02-01 00:00:00
title: Codeforces 515C - Drazil and Factorial (贪心)
tags: []
layout: post
---

#  [Codeforces 515C - Drazil and Factorial (贪心)](/2015/02/codeforces-515c/ "Codeforces 515C - Drazil and Factorial \(贪心\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Feb 18 2015 12:03

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

给出一些规则，输出最大的符合规则的数。

## 思路

数越大，说明数的个数越多。  
所以能分解就分解

把4、6、8、9分解成质因数相乘，然后从7开始。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768697071727374757677787980818283

| 
    
    
    #include <stack>#include <cstdio>#include <list>#include <cassert>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 1e6 + 10;const int MOD = 1e9 + 7;const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };const int hash_size = 4e5 + 10;int cases = 0;typedef pair<int, int> pii; vector<int> ans;int cnt[10]; void Resolve(int k){    for (int i = 2; i <= k; i++) cnt[i]++;    if (cnt[9]) cnt[3] += 2, cnt[9] = 0;    if (cnt[6]) cnt[2]++, cnt[3]++, cnt[6] = 0;    if (cnt[4]) cnt[2] += 2, cnt[4] = 0;    if (cnt[8]) cnt[2] += 3, cnt[8] = 0;;} int main(){    //ROP;    int len;    scanf("%d%*c", &len);    for (int i = 0; i < len; i++)    {        char tmp;        tmp = getchar();        Resolve(tmp-'0');    }    for (int i = 7; i >= 2; i--)    {        if (!cnt[i]) continue;        int k = cnt[i];        for (int j = i; j >= 2; j--)        {            if (cnt[j] == 0)            {                if (j == 4) cnt[2] -= 2*k;                if (j == 6) cnt[3] -= k, cnt[2] -= k;            }            else cnt[j] -= k;        }        for (int j = 0; j < k; j++) ans.PB(i);    }    for (int i = 0; i < SZ(ans); i++) printf("%d", ans[i]);    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - Codeforces](/tags/Online-Judge-Codeforces/)[Foundation - Greedy](/tags/Foundation-Greedy/)

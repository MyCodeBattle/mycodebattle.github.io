---
categories: Posts
date: 2015-01-01 00:00:00
title: UVa 668 - Parliament (贪心)
tags: []
layout: post
---

#  [UVa 668 - Parliament (贪心)](/2015/01/UVa-668/ "UVa 668 - Parliament \(贪心\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jan 19 2015 19:54

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

给一个数字，输出将其拆分成不同的，乘积最大的数。

## 思路

这里有一个”显(Y)然(Y)”的结论：数分得越多，越平均，乘积越大。

所以从2开始，2+3+4+…+k <= sum。

然后把sum-k从后面开始，把前面的数都+1

还可能会多1，就给最后那个。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768697071

| 
    
    
    #include <cstdio>#include <stack>#include <list>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <iomanip>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)#define BitCountll(x) __builtin_popcountll(x)#define LeftPos(x) 32 - __builtin_clz(x) - 1#define LeftPosll(x) 64 - __builtin_clzll(x) - 1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 100 + 10;const int MOD = 1000007;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };int cases = 0;typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int main(){    int T, i, j;    scanf("%d", &T);    while (T--)    {        vector<int> ans;        int n;        scanf("%d", &n);        for (int i = 2; i <= n; i++)        {            ans.PB(i);            n -= i;        }        for (int i = SZ(ans) - 1; i >= 0 && n; i--) ans[i]++, n--;        if (n) ans.back()++;        for (int i = 0; i < SZ(ans); i++)            if (i) printf(" %d", ans[i]);            else printf("%d", ans[0]);        puts("");        if (T) puts("");    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Foundation - Greedy](/tags/Foundation-Greedy/)

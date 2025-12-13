---
categories: Posts
date: 2015-01-01 00:00:00
title: UVa 11012 - Cosmic Cabbages (机智地枚举)
tags: []
layout: post
---

#  [UVa 11012 - Cosmic Cabbages (机智地枚举)](/2015/01/UVa-11012/ "UVa 11012 - Cosmic Cabbages \(机智地枚举\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jan 10 2015 17:12

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

找出两个点的最大的Manhattan Distance

## 思路

仰慕帆神。

求两个点的距离|x1 - x2| + |y1 - y2| + |z1 - z2|，可以通过去绝对值，得到八个式子，其中的最大值就是答案。

不用担心不存在的形式计算出来的答案会影响结果，因为最后的答案一定会比这种答案大。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081

| 
    
    
    #include <cstdio>#include <stack>#include <list>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <iomanip>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)#define BitCountll(x) __builtin_popcountll(x)#define LeftPos(x) 32 - __builtin_clz(x) - 1#define LeftPosll(x) 64 - __builtin_clzll(x) - 1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 100000 + 10;const int MOD = 1000007;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; struct ARRARY{    int arr[3];}num[MAXN]; int main(){    //ROP;    int T, i, j, n, cases = 0;    scanf("%d", &T);    while (T--)    {        scanf("%d", &n);        for (i = 0; i < n; i++)            for (j = 0; j < 3; j++) scanf("%d", #[i].arr[j]);        int ans = -INF;        for (i = 0; i < (1<<3); i++)        {            int maxValue = -INF, minValue = INF;            for (j = 0; j < n; j++)            {                int sum = 0;                for (int k = 0; k < 3; k++)                {                    if ((1<<k) & i) sum += num[j].arr[k];                    else sum -= num[j].arr[k];                }                maxValue = max(maxValue, sum); minValue = min(minValue, sum);            }            ans = max(ans, maxValue - minValue);        }        printf("Case #%d: %d\n", ++cases, ans);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Foundation - Brute Force](/tags/Foundation-Brute-Force/)

---
categories: Posts
date: 2015-03-01 00:00:00
title: HDU 5183 - Negative and Positive (NP) (二分 + 思维)
tags: []
layout: post
---

#  [HDU 5183 - Negative and Positive (NP) (二分 + 思维)](/2015/03/HDU-5183/ "HDU 5183 - Negative and Positive \(NP\) \(二分 + 思维\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Mar 7 2015 23:31

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

给一个数组a1、a2、a3…，问是否存在一个二元组(i, j)使得a[i]-a[i+1]+a[i+2]…. +-a[j] = k。

## 思路

也是枚举一个数然后二分查找另一个数是否在数组里。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879

| 
    
    
    #include <stack>#include <cstdio>#include <list>#include <cassert>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 1e6 + 10;const int MOD = 9901;const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };int cases = 0;typedef pair<int, int> pii; vector<LL> mp;LL sum[MAXN];int n, k; bool Solve(){    for (int i = 0; i < n; i++)    {        if (!(i & 1))        {            if (binary_search(mp.begin(), mp.end(), sum[i]+k)) return true;        }        else if (binary_search(mp.begin(), mp.end(), sum[i]-k)) return true;    }    return false;} int main(){    //ROP;    int T;    scanf("%d", &T);    while (T--)    {        mp.clear();        scanf("%d%d", &n, &k);        for (int i = 1, t = 1; i <= n; i++, t = -t)        {            scanf("%I64d", ∑[i]);            sum[i] = sum[i-1] + t*sum[i];            mp.PB(sum[i]);        }        mp.PB(0);        sort(mp.begin(), mp.end());        printf("Case #%d: %s.\n", ++cases, Solve() ? "Yes" : "No");    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - HDU](/tags/Online-Judge-HDU/)[Foundation - Jizhi](/tags/Foundation-Jizhi/)

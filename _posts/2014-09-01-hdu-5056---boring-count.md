---
categories: Posts
date: 2014-09-01 00:00:00
title: HDU 5056 - Boring count
tags: []
layout: post
---

#  [HDU 5056 - Boring count](/2014/09/HDU-5056/ "HDU 5056 - Boring count")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 28 2014 22:16

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

统计一个字符串中子串每个字符最多重复k次的子串。

## 思路

用pos记录位置，当碰到cnt>k的时候就往前移

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <ctime>#include <cstdlib>#include <fstream>#include <string>#include <sstream>#include <map>#include <cmath>#define LL long long#define lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 1e5 + 100;const int MOD = 20071027; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; char str[MAXN];int cnt[30]; int main(){    //ROP;    int n, i, j, last, T, k;    scanf("%d", &T);    while (T--)    {        MS(cnt, 0);        int pos = 1;        scanf("%s", str + 1);        scanf("%d", &k);        int len = strlen(str + 1);        LL ans = 0;        for (i = 1; i <= len; i++)        {            cnt[str[i] - 'a']++;            while (cnt[str[i] - 'a'] > k)            {                cnt[str[pos] - 'a']--;                pos++;            }            ans += i - pos + 1;        }        cout << ans << endl;    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - HDU](/tags/Online-Judge-HDU/)

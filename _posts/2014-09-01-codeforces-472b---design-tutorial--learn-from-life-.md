---
categories: Posts
date: 2014-09-01 00:00:00
title: Codeforces 472B - Design Tutorial → Learn from Life (模拟)
tags: []
layout: post
---

#  [Codeforces 472B - Design Tutorial → Learn from Life (模拟)](/2014/09/codeforces-472b/ "Codeforces 472B - Design Tutorial → Learn from Life \(模拟\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 29 2014 15:26

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

有一个载重量为K的电梯，有N个人，每个人都有想去的地方，求电梯送他们到站的最少时间。

## 思路

一开始我想从低到高来载，发现不好搞。

换个思路，先运最高的人，如果还有空的话顺路载一下低一点的人。

不过还是感觉我的思路很low。。。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879808182838485868788

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <ctime>#include <cstdlib>#include <fstream>#include <string>#include <sstream>#include <map>#include <cmath>#define LL long long#define lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 2000 + 5;const int MOD = 20071027; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int num[MAXN]; int main(){    //ROP;    int n, cap, i, j;    int tmp;    scanf("%d%d", &n, ∩);    for (i = 0; i < n; i++)    {        scanf("%d", &tmp);        num[tmp]++;    }    int cur = cap, ans = 0;    for (i = 2000; i >= 2; i--)    {        while (num[i])        {            if (cur != cap)            {                if (num[i] >= cur)                {                    num[i] -= cur;                    cur = 0;                }                else                {                    cur -= num[i];                    num[i] = 0;                }                if (cur == 0) cur = cap;                continue;            }            else if (num[i] >= cur)            {                num[i] -= cur;                cur = 0;                ans += ((i - 1) << 1);            }            else            {                ans += ((i - 1) << 1);                cur -= num[i];                num[i] = 0;            }            if (cur == 0) cur = cap;        }    }    printf("%d\n", ans);    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - Codeforces](/tags/Online-Judge-Codeforces/)[Foundation - Simulate](/tags/Foundation-Simulate/)

---
categories: Posts
date: 2015-03-02 00:00:00
title: Codeforces 521A - DNA Alignment (思维)
tags: []
layout: post
---

## 题意

设$k = p(s, t)_{max}$，现在给出s，问存在几个t。

## 思路

先仰慕q神。

首先我们来看下那个计算$p(s, t)$的公式。

我们先固定住s，这样来一个循环后就相当于s的每个位置都轮了t的每个位置一次。

我们用$N(A)$和$N(A’)$来表示s里面A的数量和t里面A的数量。以此类推。

那么现在放开s，那么就能得出最后的值

$$val = N(A)N(A’) + N(G)N(G’) + N(C)N(C’) + N(T)N(T’)$$

根据这个式子，只要我们找出最大的$N(X)$，那么让t中全部填上$X$，这样就可以取到最大值！

所以最终的答案是，找出s中出现最多的次数。如果这个次数对应的字母k个，答案就是$k^n$(每个位置可以有k种选择，n个位置)

感觉这题挺好的╰（￣▽￣）╭

## 代码


```c++
#include <stack>
#include <cstdio>
#include <list>
#include <cassert>
#include <set>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <functional>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <string>
#include <map>
#include <cmath>
using namespace std;
#define LL long long
#define ULL unsigned long long
#define SZ(x) (int)x.size()
#define Lowbit(x) ((x) & (-x))
#define MP(a, b) make_pair(a, b)
#define MS(arr, num) memset(arr, num, sizeof(arr))
#define PB push_back
#define X first
#define Y second
#define ROP freopen("input.txt", "r", stdin);
#define MID(a, b) (a + ((b - a) >> 1))
#define LC rt << 1, l, mid
#define RC rt << 1|1, mid + 1, r
#define LRT rt << 1
#define RRT rt << 1|1
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
const double eps = 1e-9;
const int MAXN = 1e6 + 10;
const int MOD = 1e9 + 7;
const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };
int cases = 0;
typedef pair<int, int> pii;
 
LL pow_mod(LL a, LL m)
{
    LL ret = 1;
    while (m)
    {
        if (m & 1) ret = ret*a % MOD;
        a = a*a % MOD;
        m >>= 1;
    }
    return ret;
}
 
int cnt[30];
 
int main()
{
    int n;
    scanf("%d%*c", &n);
    int ans = 0;
    for (int i = 0; i < n; i++)
    {
        char ch = getchar();
        cnt[ch-'A']++;
        ans = max(ans, cnt[ch-'A']);
    }
    int num = 0;
    for (int i = 0; i < 30; i++)
        if (cnt[i] == ans) num++;
    printf("%I64d\n", pow_mod(num, n));
    return 0;
}
```
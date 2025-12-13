---
categories: Posts
date: 2015-02-01 00:00:00
title: HDU 2836 - Traversal (树状数组 + DP)
tags: []
layout: post
---

## 题意

给出一串序列，求它的子序列，使$abs(相邻的元素差) \leq K$

## 思路

看了**Because Of You** 的题解。

先可以想到一个DP。

$dp[i] = \sum dp[j] \text{ |i-j| <= K}$，意思是以数字i结尾的子序列个数等于，和以i的绝对值相差<=K的数字结尾的子序列个数之和。

消去绝对值！

$i-k \leq j \leq i+k$

这样就说明j是在一个范围内。

那么我们就可以利用树状数组的特性，直接得到答案为$sum[i+k] - sum[i-k]$。

不过这里的i+k和i-k需要表示成一个输入里有的数，因为要离散化。这里可以利用二分得到。

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
const double eps = 1e-8;
const int MAXN = 1e5 + 10;
const int MOD = 9901;
const int MOD2 = 1e9 + 9;
const int seed = 188147;
const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };
int cases = 0;
typedef pair<int, int> pii;
 
int sum[MAXN], arr[MAXN], val[MAXN];
 
void Update(int idx, int num)
{
    while (idx < MAXN)
    {
        sum[idx] += num;
        if (sum[idx] > MOD) sum[idx] %= MOD;
        idx += Lowbit(idx);
    }
}
 
int Query(int r)
{
    int ret = 0;
    while (r > 0)
    {
        ret += sum[r];
        r -= Lowbit(r);
        if (ret > MOD) ret %= MOD;
    }
    return ret % MOD;
}
 
int main()
{
    //ROP;
    int n, k;
    while (~scanf("%d%d", &n, &k))
    {
        MS(sum, 0);
        for (int i = 1; i <= n; i++)
        {
            scanf("%d", &arr[i]);
            val[i] = arr[i];
        }
        sort(arr+1, arr+1+n);
        int len = unique(arr+1, arr+1+n) - (arr+1);
        int ans = 0;
        for (int i = 1; i <= n; i++)
        {
            int idx = lower_bound(arr+1, arr+1+len, val[i]) - arr;
            int lower = lower_bound(arr+1, arr+1+len, val[i]-k) - arr;
            int upper = upper_bound(arr+1, arr+1+len, val[i]+k) - arr - 1;
            int curAns = (Query(upper) - Query(lower-1)) % MOD;
            ans += curAns;
            if (ans > MOD) ans %= MOD;
            Update(idx, curAns+1);
        }
        printf("%d\n", (ans%MOD + MOD) % MOD);
    }
    return 0;
}
```
---
categories: Posts
date: 2014-09-19 00:00:00
title: Codeforces Round 267 (Div. 2) C - George and Job
tags: []
layout: post
---

## 题意

找出一个序列中k个长度为m区间的最大和。

## 思路

昨天写这题的时候真是脑洞大开，连区间DP都YY了一下。结果还是没写出来。

其实简单的背包就行。

$dp[i][j] = max(dp[i - 1][j], dp[i - m][j - 1] + sum)$

dp[i][j]表示前i个数选j个区间的最大和。

## 代码


```c++
#include <cstdio>
#include <algorithm>
#include <functional>
#include <stack>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <cstring>
#include <string>
#include <sstream>
#include <map>
#include <cmath>
#define LL long long
#define lowbit(x) ((x) & (-x))
#define MP(a, b) make_pair(a, b)
const int MAXN = 5000 + 5;
const int INF = 0x3f3f3f3f;
using namespace std;
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
LL num[MAXN], dp[MAXN][MAXN];
 
int main()
{
    //freopen("input.txt", "r", stdin);
    ios::sync_with_stdio(false);
 
    int n, m, k, i, j;
    cin >> n >> m >> k;
    for (i = 1; i <= n; i++)
    {
        cin >> num[i];
        num[i] += num[i - 1];
    }
    for (i = 1; i <= n; i++)
        for (j = 1; j <= k; j++)
        {
            dp[i][j] = dp[i - 1][j];
            if (i >= m)
                dp[i][j] = max(dp[i][j], dp[i - m][j - 1] + num[i] - num[i - m]);
        }
    cout << dp[n][k] << endl;
    return 0;
}
```
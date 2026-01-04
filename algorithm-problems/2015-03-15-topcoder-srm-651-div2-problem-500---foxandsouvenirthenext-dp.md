---
categories: Posts
date: 2015-03-15 00:00:00
title: TopCoder SRM 651 Div2 Problem 500 - FoxAndSouvenirTheNext (DP)
tags: []
layout: post
---

## 题意

问能不能选出n/2个数，使得她们的和为sum/2。

## 思路

就是说n/2个数能不能凑出sum/2。

用完全背包。

$dp[i][j] = dp[i-1][j-v[n]]$  
意思是前n个里选i个能凑出j，当前n个选i-1个里能凑出j-v[n]。

## 代码


```c++
​class FoxAndSouvenirTheNext {
public:
    int dep, sum;
    int dp[55][3000];
    string ableToSplit(vector<int> v) {
        if (SZ(v) & 1) return "Impossible";
        v.insert(v.begin(), -1);
        sum = 0;
        dp[0][0] = 1;
        for (int i = 1; i < SZ(v); i++) sum += v[i];
        if (sum & 1) return "Impossible";
        sum /= 2;
        for (int i = 1; i < SZ(v); i++)
        {
            for (int j = i; j > 0; j--)
            {
                for (int k = MAXN; k >= v[i]; k--)
                    if (!dp[j][k] && dp[j-1][k-v[i]]) dp[j][k] = 1;
            }
        }
        return dp[SZ(v)/2][sum] ? "Possible" : "Impossible";
    }
};
```
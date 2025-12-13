---
categories: Posts
date: 2015-02-01 00:00:00
title: TopCoder SRM 650 Div2 Problem 500 - TaroFillingAStringDiv2 (DP)
tags: []
layout: post
---

## 题意

有一串A、B、?组成的字符串，现在要求输出让该字符串连续相同的字符数最少的数量。

## 思路

dp。

$dp(i, j)表示前i个字符，当前位置是j字符的最少的数量$

$$dp(i, j) = \begin{cases} min(dp(i-1, 0)+1, dp(i-1, 1)) & \text{j == 0} \\\ min(dp(i-1, 0), dp(i-1, 1)+1) & \text{j==1} \\\ \end{cases} \\\ \text{if(str[i] == '?')} \\\ dp(i, 0) = min(dp(i-1, 0) + 1, dp(i-1, 1)) \\\ dp(i, 1) = min(dp(i-1, 0), dp(i-1, 1) + 1)$$

## 代码


```c++
class TaroFillingAStringDiv2 {
    public:
    int getNumber(string str) {
        if (str.empty() || SZ(str) == 1) return 0;
        MS(dp, INF);
        dp[0][0] = dp[0][1] = 0;
        if (str[0] == 'A') dp[0][1] = INF;
        if (str[0] == 'B') dp[0][0] = INF;
        for (int i = 1; i < SZ(str); i++)
        {
            if (str[i] != '?')
            {
                if (str[i] == 'A')
                {
                    dp[i][0] = min(dp[i-1][1], dp[i-1][0] + 1);
                    dp[i][1] = INF;
                }
                else
                {
                    dp[i][1] = min(dp[i-1][1] + 1, dp[i-1][0]);
                    dp[i][0] = INF;
                }
            }
            else
            {
                dp[i][0] = min(dp[i-1][1], dp[i-1][0] + 1);
                dp[i][1] = min(dp[i-1][1] + 1, dp[i-1][0]);
            }
        }
        int len = SZ(str) - 1;
        return min(dp[len][0], dp[len][1]);
    }
};
```
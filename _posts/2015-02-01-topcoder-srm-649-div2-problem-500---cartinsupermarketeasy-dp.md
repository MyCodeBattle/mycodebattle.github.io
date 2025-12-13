---
categories: Posts
date: 2015-02-01 00:00:00
title: TopCoder SRM 649 Div2 Problem 500 - CartInSupermarketEasy (区间DP)
tags: []
layout: post
---

## 题意

给出N和K。

在每一轮中，可以对现有的每个数进行下面的两个操作之一。

  1. 减一
  2. 拆成两个更小的数之和


最多只能拆K次。

现在问完全消去一个数最少要几轮。

## 思路

## 题意

给出N和K。

在每一轮中，可以对现有的每个数进行下面的两个操作之一。

  1. 减一
  2. 拆成两个更小的数之和


最多只能拆K次。

现在问完全消去一个数最少要几轮。

## 思路

昨天一直以为对半分是最优的，结果样例都过不去。

其实是一个DP。。

$dp(i, j)$表示现在数是i，还有j次分解机会，这时候最少需要的轮数。

对于某一个数，可以拆或者不拆。

如果不拆，$dp(i, j) = dp(i-1, j)+1$  
拆！$dp(i, j) = min(dp(i, j), 1+max(dp(I, J), dp(currentN-I, currentK-1-J))), 1<=I<=currentN, 0 <= K < currentK $

## 代码


```c++
int dp[110][110];
 
class CartInSupermarketEasy {
public:
    int DFS(int N, int K)
    {
        if (dp[N][K] != -1) return dp[N][K];
        if (K == 0) return dp[N][K] = N;
        if (N == 1) return dp[N][K] = 1;
        if (N == 0) return dp[N][K] = 0;
        int ans = DFS(N-1, K) + 1;
        for (int i = 1; i < N; i++)
            for (int j = 0; j < K; j++)
                ans = min(ans, 1 + max(DFS(i, j), DFS(N-i, K-1-j)));
        return dp[N][K] = ans;
    }
 
    int calc(int N, int K) {
        MS(dp, -1);
        return DFS(N, K);
    }
};
```
 

```
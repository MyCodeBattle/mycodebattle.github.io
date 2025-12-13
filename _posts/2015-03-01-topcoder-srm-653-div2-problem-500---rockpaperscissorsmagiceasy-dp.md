---
categories: Posts
date: 2015-03-01 00:00:00
title: TopCoder SRM 653 Div2 Problem 500 - RockPaperScissorsMagicEasy (DP)
tags: []
layout: post
---

## 题意

给出小明的石头剪刀布顺序，给出一个目标值，问有几种方法可以得到。

## 思路

一开始觉得是组合数学，不会，于是就开始DP。

比赛的时候想了一个三维dp。

$dp[i][j][k]$表示前i个序列中，现在出的是j（石头剪刀等），分数是k的方法数。

如果此时小明出的是剪刀，分数是k分。

这个分数可能是

  1. 赢了小明，也就是出石头得到的一分。
  2. 输了小明，以前的分数。


所以转移方程$dp[i][j][k] = dp[i-1][lose][k] + dp[i-1][win][k-1]$，然后处理一下边界。

写着写着我就觉得不太对劲，这都是重复的代码啊。。  
但是比赛的时候一时也想不出什么改进，就凑合着写了。  
直到challenge的时候看到一个代码，最后知道真相的我眼泪掉下来TAT。

大家应该能感觉到，不管小明怎么出，只要数量相同，答案肯定是相同的。反正每一种出法都有两种方法不得分，一种得一分。

去掉一个状态。

$dp[i][j]$表示前i个序列中，分数是k的方法数。

$dp[i][j] = dp[i-1][j]*2 + dp[i-1][j-1]$

没错。。就这么一条(#`O′)

还有一种组合数学的方法，不会。

## 代码简洁版
    
    
    123456789101112131415161718192021

| ```c++
class RockPaperScissorsMagicEasy {public:  int count(vector <int>, int);};  int RockPaperScissorsMagicEasy::count(vector <int> card, int score) {  int n = card.size();  if(score > n) return 0;  long long a[n+10][score+10];    memset(a, 0, sizeof(a));  a[0][0] = 1;  for(int i = 1; i <= n; ++ i) {        for(int j = 0; j <= score; ++ j) {            a[i][j] = a[i-1][j]*2;            if(j) a[i][j] += a[i-1][j-1];            a[i][j] %= 1000000007;        }  }  return (int)a[n][score];}
```  

## 代码SB版
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556

| ```c++
class RockPaperScissorsMagicEasy {    int dp[MAXN][3][MAXN];    public:    int count(vector<int> c, int score) {        reverse(c.begin(), c.end());        c.push_back(-1);        reverse(c.begin(), c.end());        int sz = SZ(c);        if (c[1] == 1) dp[1][2][1] = 1, dp[1][1][0] = 1, dp[1][0][0] = 1;        else if (c[1] == 0) dp[1][1][1] = 1, dp[1][0][0] = 1, dp[1][2][0] = 1;        else if (c[1] == 2) dp[1][0][1] = 1, dp[1][1][0] = 1, dp[1][2][0] = 1;        for (int i = 2; i < sz; i++)        {            for (int j = 0; j < 3; j++)            {                for (int k = score; k >= 0; k--)                {                    if (j == 0)                    {                        if (c[i] == 2)                        {                            if (k == 0) break;                            dp[i][j][k] = (dp[i-1][0][k-1] + dp[i-1][1][k-1]) % MOD + dp[i-1][2][k-1], dp[i][j][k] %= MOD;                        }                        else                            for (int l = 0; l < 3; l++) dp[i][j][k] = (dp[i][j][k] + dp[i-1][l][k]) % MOD;                    }                    if (j == 1)                    {                        if (c[i] == 0)                        {                            if (k == 0) break;                            for (int l = 0; l < 3; l++) (dp[i][j][k] = dp[i-1][l][k-1] + dp[i][j][k]) % MOD;                        }                        else                            for (int l = 0; l < 3; l++) dp[i][j][k] = (dp[i-1][l][k] + dp[i][j][k]) % MOD;                    }                    if (j == 2)                    {                        if (c[i] == 1)                        {                            if (k == 0) break;                            for (int l = 0; l < 3; l++) (dp[i][j][k] = dp[i-1][l][k-1] + dp[i][j][k]) % MOD;                        }                        else                            for (int l = 0; l < 3; l++) dp[i][j][k] = (dp[i-1][l][k] + dp[i][j][k]) % MOD;                    }                }            }        }        LL ans = 0;        for (int i = 0; i < 3; i++)            ans = (ans + dp[sz-1][i][score]) % MOD;        return (int)ans;    }};
```
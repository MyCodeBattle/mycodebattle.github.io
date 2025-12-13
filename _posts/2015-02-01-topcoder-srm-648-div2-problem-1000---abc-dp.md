---
categories: Posts
date: 2015-02-01 00:00:00
title: TopCoder SRM 648 Div2 Problem 1000 - ABC (DP)
tags: []
layout: post
---

## 题意

给定字符串长度和s[i] < s[j]的对数，凑出这样的字符串。

## 思路

Orz一下DP的思路

$dp[i][j][k][l]$表示i个A，j个B，k个C组成的字符串里有l对s[i] < s[j]。

如果它的值为1，就是加了个A转移过来的。  
值为2，加了个B。  
值为3，加了个C。

然后递归输出

## 代码


```c++
int dp[MAXN][MAXN][MAXN][500];
 
class ABC {
 
public:
    string ans;
    void Output(int a, int b, int c, int d)
    {
        if (a+b+c+d == 0) return;
        if (dp[a][b][c][d] == 1)
        {
            Output(a-1, b, c, d);
            ans += 'A';
        }
        else if (dp[a][b][c][d] == 2)
        {
            Output(a, b-1, c, d-a);
            ans += 'B';
        }
        else if (dp[a][b][c][d] == 3)
        {
            Output(a, b, c-1, d-a-b);
            ans += 'C';
        }
    }
    string createString(int N, int K) {
        dp[0][0][0][0] = 1;
        for (int i = 0; i <= N; i++)
            for (int j = 0; j+i <= N; j++)
                for (int k = 0; k+j+i <= N; k++)
                    for (int l = 0; l <= K; l++)
                    {
                        if (dp[i][j][k][l])
                        {
                            if (i+j+k == N && l == K)
                            {
                                Output(i, j, k, l);
                                return ans;
                            }
                            dp[i+1][j][k][l] = 1;
                            if (l+i <= K) dp[i][j+1][k][l+i] = 2;
                            if (l+i+j <= K) dp[i][j][k+1][l+i+j] = 3;
                        }
                    }
        return ans;
    }
};
```
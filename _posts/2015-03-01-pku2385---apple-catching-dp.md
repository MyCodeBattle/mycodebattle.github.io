---
categories: Posts
date: 2015-03-01 00:00:00
title: PKU2385 - Apple Catching (DP)
tags: []
layout: post
---

#  [PKU2385 - Apple Catching (DP)](/2015/03/PKU-2385/ "PKU2385 - Apple Catching \(DP\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Mar 5 2015 20:21

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

最多能收到多少苹果。

## 思路

$dp[i][j][k]$，表示前i秒现在站在j处还剩k次瞬移。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768697071727374757677

| 
    
    
    #include <stack>#include <cstdio>#include <list>#include <cassert>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 100 + 10;const int MOD = 9901;const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };int cases = 0;typedef pair<int, int> pii; int dp[1010][2][35], arr[1010];int main(){    //ROP;    int n, l;    scanf("%d%d", &n, &l);    for (int i = 1; i <= n; i++)    {        scanf("%d", &arr[i]);        arr[i]--;    }    for (int i = 1; i <= n; i++)    for (int j = 0; j < 2; j++)    for (int k = 0; k <= l; k++) dp[i][j][k] = -INF;    dp[1][arr[1]][l] = 1; dp[1][arr[1]^1][l] = 0;    for (int i = 2; i <= n; i++)    {        for (int j = 0; j < 2; j++)        {            for (int k = 0; k <= l; k++)            {                dp[i][j][k] = dp[i-1][j][k];                if (k != l) dp[i][j][k] = max(dp[i][j][k], dp[i-1][j^1][k+1]);                if (j == arr[i]) dp[i][j][k]++;            }        }    }    int ans = 0;    for (int i = 0; i <= l; i++)    {        ans = max(ans, dp[n][0][i]);        ans = max(ans, dp[n][1][i]);    }    printf("%d\n", ans);    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - PKU](/tags/Online-Judge-PKU/)[DP - 递推](/tags/DP-递推/)

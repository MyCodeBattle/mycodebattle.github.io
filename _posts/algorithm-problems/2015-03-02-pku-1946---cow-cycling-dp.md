---
categories: Posts
date: 2015-03-02 00:00:00
title: PKU 1946 - Cow Cycling (DP)
tags: []
layout: post
---

## 题意

几只牛在赛跑，每一只牛带头跑x圈/分需要消耗x*x的体力，现在问最少需要多少分。

## 思路

显然是让最后一只冲刺。


```c++
dp[i][j][k]
```
表示第i只牛跑j圈用k能量的最少分钟数。然后枚举他上一口气跑的圈数。

第
```c++
i+1
```
只牛继承第i只牛的成果。即
```c++
dp[i+1][j][j] = dp[i][j][k]
```


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
const int MOD = 9901;
const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };
int cases = 0;
typedef pair<int, int> pii;
 
int dp[25][110][110];
 
int main()
{
    int N, E, D;
    while (~scanf("%d%d%d", &N, &E, &D))
    {
        MS(dp, INF);
        dp[1][0][0] = 0;
        for (int i = 1; i <= N; i++)
            for (int j = 1; j <= D; j++)
                for (int k = 1; k <= E; k++)
                {
                    for (int l = 1; l*l <= k && l <= j; l++)
                        dp[i][j][k] = min(dp[i][j][k], dp[i][j-l][k-l*l]+1);
                    dp[i+1][j][j] = min(dp[i+1][j][j], dp[i][j][k]);
                }
        int ans = INF;
        for (int i = 1; i <= E; i++) ans = min(ans, dp[N][D][i]);
        printf("%d\n", ans);
    }
    return 0;
}
```
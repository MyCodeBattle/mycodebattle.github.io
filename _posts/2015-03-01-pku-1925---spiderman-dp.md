---
categories: Posts
date: 2015-03-01 00:00:00
title: PKU 1925 - Spiderman (DP)
tags: []
layout: post
---

## 题意

蜘蛛侠要飞到最后一栋房子上。问最少需要几步。

## 思路

根据坐标来dp。

```c++
dp[i]
```表示到i坐标需要的最少步数。

先处理出能连上某个楼的X的最长距离。

然后荡到```c++
building[i].X+j
```处，更新此处的距离。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768697071727374

| ```c++
#include <stack>#include <cstdio>#include <list>#include <cassert>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-9;const int MAXN = 1e6 + 10;const int MOD = 9901;const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };int cases = 0;typedef pair<int, int> pii; int dp[MAXN];pair<int, LL> arr[5005];double scale[5005]; int main(){    //ROP;    int T;    scanf("%d", &T);    while (T--)    {        MS(dp, -1);        int n;        scanf("%d", &n);        for (int i = 1; i <= n; i++)        {            scanf("%d%d", &arr[i].X, &arr[i].Y);            scale[i] = sqrt(arr[i].Y*arr[i].Y - (arr[i].Y-arr[1].Y)*(arr[i].Y-arr[1].Y));        }        dp[arr[1].X] = 0;        for (int i = 2; i <= n; i++)            for (int j = 1; j <= scale[i]; j++)            {                int tmp = arr[i].X-j;                if (tmp < arr[1].X) break;                if (dp[tmp] == -1) continue;                int aim = min(arr[i].X+j, arr[n].X);                dp[aim] = dp[aim] == -1 ? dp[tmp]+1 : min(dp[tmp]+1, dp[aim]);            }        printf("%d\n", dp[arr[n].X]);    }    return 0;}
```
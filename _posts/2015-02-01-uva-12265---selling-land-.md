---
categories: Posts
date: 2015-02-01 00:00:00
title: UVa 12265 - Selling Land (单挑队列)
tags: []
layout: post
---

## 题意

以一个格子为右下角做矩形，找出它的最大周长。

## 思路

还记得以前谁说过，单调队列学好了就可以单挑了，俗称单挑队列。真的是。。。

这题想了一晚上还是似懂非懂。只能寄望于日后一朝领悟了。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990

| ```c++
#include <stack>#include <cstdio>#include <list>#include <cassert>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 1e3 + 2;const int MOD = 1e9 + 7;const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };int cases = 0;typedef pair<int, int> pii; int up[MAXN][MAXN], row, col;void Solve(){    map<int, int> mp;    for (int i = 1; i <= row; i++)    {        stack<pii> S;        for (int j = 1; j <= col; j++)        {            int r = j;            while (!S.empty() && S.top().X >= up[i][j])            {                r = S.top().Y;                S.pop();            }            if (up[i][j] == 0) continue;            if (S.empty() || up[i][j] - S.top().X > r - S.top().Y)            {                mp[up[i][j] + j-r+1]++;                S.push(MP(up[i][j], r));            }            else mp[S.top().X + j-S.top().Y+1]++;        }    }    for (map<int, int>::iterator it = mp.begin(); it != mp.end(); it++)        printf("%d x %d\n", it->Y, it->X * 2);} int main(){    //ROP;    int T;    scanf("%d", &T);    while (T--)    {        MS(up, 0);        scanf("%d%d", &row, &col);        for (int i = 1; i <= row; i++)            for (int j = 1; j <= col; j++)            {                char ch = getchar();                while (ch != '.' && ch != '#') ch = getchar();                if (ch == '#') up[i][j] = 0;                else up[i][j] = up[i-1][j] + 1;            }        Solve();    }    return 0;}
```
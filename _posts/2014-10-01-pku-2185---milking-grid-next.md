---
categories: Posts
date: 2014-10-01 00:00:00
title: PKU 2185 - Milking Grid (next数组的应用)
tags: []
layout: post
---

## 题意

求一个最小的子矩阵，可以再复制无限次后覆盖原矩阵。

## 思路

对每一行求出最短重复的子串，然后求总的最小公倍数。这样求出来就是子矩阵的长度。

以此类推，求出列的最小公倍数，求出来的是子矩阵的宽度。

然后相乘即可。

学习了计算失配函数的另一种写法。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108

| ```c++
#include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>#define LL long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 10000 + 10;const int MOD = 1e9 + 7;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} }; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int next[MAXN], row, col;char str[MAXN][80]; int GetFailc(int n){    int i = 0, j = -1;    next[0] = -1;    while (i < col)    {        if (j == -1 || str[n][i] == str[n][j])        {            i++; j++;            next[i] = j;        }        else j = next[j];    }    return i - next[i];} int GetFailr(int n){    int i = 0, j = -1;    next[0] = -1;    while (i < row)    {        if (j == -1 || str[i][n] == str[j][n])        {            i++, j++;            next[i] = j;        }        else j = next[j];    }    return i - next[i];} int LCM(int a, int b){    return a * b / __gcd(a, b);} int main(){    //ROP;    int i, j;    scanf("%d%d", &row, &col);    int ansR = 1, ansC = 1;    for (i = 0; i < row; i++) scanf("%s", str[i]);    for (i = 0; i < row; i++)    {        ansR = LCM(ansR, GetFailc(i));        if (ansR > col)        {            ansR = col;            break;        }    }    for (i = 0; i < col; i++)    {        ansC = LCM(ansC, GetFailr(i));        if (ansC > row)        {            ansC = row;            break;        }    }    printf("%d\n", ansC * ansR);    return 0;}
```
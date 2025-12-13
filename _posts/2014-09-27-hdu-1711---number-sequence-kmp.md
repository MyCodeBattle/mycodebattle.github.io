---
categories: Posts
date: 2014-09-27 00:00:00
title: HDU 1711 - Number Sequence (KMP)
tags: []
layout: post
---

## 代码


```c++
#include <cstdio>
#include <stack>
#include <set>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <functional>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <ctime>
#include <cstdlib>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <cmath>
#define LL long long
#define lowbit(x) ((x) & (-x))
#define MP(a, b) make_pair(a, b)
#define MS(arr, num) memset(arr, num, sizeof(arr))
#define PB push_back
#define F first
#define S second
#define ROP freopen("input.txt", "r", stdin);
#define BitCount(x) __builtin_popcount(x)
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
using namespace std;
const int MAXN1 = 1e6 + 5;
const int MAXN2 = 1e4 + 5;
const int MOD = 20071027;
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
int n, m, an[MAXN1], bn[MAXN2], f[MAXN1];
 
void GetFail(int *P, int *f)
{
    f[0] = 0, f[1] = 0;
    for (int i = 1; i < m; i++)
    {
        int j = f[i];
        while (j && P[i] != P[j]) j = f[j];
        f[i + 1] = (P[i] == P[j] ? j + 1 : 0);
    }
}
 
int Find(int *T, int *P, int *f)
{
    GetFail(P, f);
    int j = 0;
    for (int i = 0; i < n; i++)
    {
        while (j && P[j] != T[i]) j = f[j];
        if (P[j] == T[i]) j++;
        if (j == m) return i - m + 2;
    }
    return -1;
}
 
int main()
{
    //ROP;
    int T, i, j;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%d%d%*c", &n, &m);
        for (i = 0; i < n; i++) scanf("%d", &an[i]);
        for (i = 0; i < m; i++) scanf("%d", &bn[i]);
        int ans = Find(an, bn, f);
        printf("%d\n", ans);
    }
    return 0;
}
```
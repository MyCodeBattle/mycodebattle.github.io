---
categories: Solving-Reports
date: 2015-10-24 11:41:50
title: CodeChef ADTRI - Rupsa and Equilateral Triangle (数论 + 费马平方和定理)
tags: [Online Judge - CodeChef, Math - Number Theory]
layout: post
---

 ## 题意 ## 

问是否存在两个数，使得$n^2 = a^2 + b^2$

 ## 思路 ## 

Fermat's theorem on sums of two squares

p是一个质数，$p = x^2 + y^2$ iff $p \equiv 1 (\bmod 4)$

得出来之后每个数加上本身轮一遍。

 ## 代码 ## 

```
#include <stack>
#include <cstdio>
#include <list>
#include <cassert>
#include <set>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <functional>
#include <cstring>
#include <iomanip>
#include <algorithm>
#include <cctype>
#pragma comment(linker, "/STACK:102400000,102400000")
#include <string>
#include <map>
#include <cmath>
using namespace std;
#define LL long long
#define ULL unsigned long long
#define SZ(x) (int)x.size()
#define lowbit(x) ((x) & (-x))
#define MP(a, b) make_pair(a, b)
#define MS(p, num) memset(p, num, sizeof(p))
#define PB push_back
#define X first
#define Y second
#define ROP freopen("input.txt", "r", stdin);
#define MID(a, b) (a + ((b - a) >> 1))
#define LC rt << 1, l, mid
#define RC rt << 1|1, mid+1, r
#define LRT rt << 1
#define RRT rt << 1|1
#define FOR(i, a, b) for (int i=(a); (i) < (b); (i)++)
#define FOOR(i, a, b) for (int i = (a); (i)<=(b); (i)++)
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
const double eps = 1e-8;
const int MAXN = 5e6+10;
const int MOD = 10007;
const int dir[][2] = { {1, 0}, {0, -1}, {-1, 0}, {0, 1} };
const int seed = 131;
int cases = 0;
typedef pair<int, int> pii;
 
int n, vis[MAXN];
vector<int> primes;
 
void init()
{
    int m = sqrt(MAXN);
    for (int i = 2; i <= m; i++) if (!vis[i])
        for (int j = i*i; j < MAXN; j += i) vis[j] = 1;
    for (int i = 2; i < MAXN; i++) if (!vis[i] && i % 4 == 1)
        primes.push_back(i);
    MS(vis, 0);
    for (int i : primes)
        for (int j = i; j < MAXN; j += i) vis[j] = 1;
}
 
int main()
{
    init();
    int T;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%d", &n);
        puts(vis[n] ? "YES" : "NO");
    }
    return 0;
}
```
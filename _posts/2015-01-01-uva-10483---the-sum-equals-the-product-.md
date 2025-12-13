---
categories: Posts
date: 2015-01-01 00:00:00
title: UVa 10483 - The Sum Equals the Product (枚举)
tags: []
layout: post
---

## 题意

找出一个数，使得$sum = a + b + c = a * b * c$

## 思路

看的帆神。

枚举a和b，求出c，a和b在算的过程中可以剪枝一下。

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
#include <iomanip>
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
#define F first
#define S second
#define ROP freopen("input.txt", "r", stdin);
#define MID(a, b) (a + ((b - a) >> 1))
#define LC rt << 1, l, mid
#define RC rt << 1|1, mid + 1, r
#define LRT rt << 1
#define RRT rt << 1|1
#define BitCount(x) __builtin_popcount(x)
#define BitCountll(x) __builtin_popcountll(x)
#define LeftPos(x) 32 - __builtin_clz(x) - 1
#define LeftPosll(x) 64 - __builtin_clzll(x) - 1
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
const double eps = 1e-8;
const int MAXN = 100 + 10;
const int MOD = 1000007;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
struct EQUATION
{
    double sum, a, b, c;
};
 
vector<EQUATION> ans;
int nn, mm;
 
bool cmp(const EQUATION &a, const EQUATION &b)
{
    if (fabs(a.sum - b.sum) >= eps) return a.sum < b.sum;
    if (fabs(a.a - b.a) >= eps) return a.a < b.a;
    if (fabs(a.b - b.b) >= eps) return a.b < b.b;
    if (fabs(a.c - b.c) >= eps) return a.c < b.c;
}
 
bool Judge(int a, int b, int c)
{
    if (c < a || c < b) return false;
    int x = a + b + c, y = a * b * c;
    if (x < nn || x > mm) return false;
    if (y % 10000) return false;
    if (x == y / 10000) return true;
    else return false;
}
 
int main()
{
    //ROP;
    int i, j;
    double n, m;
    while (cin >> n >> m)
    {
        ans.clear();
        nn = (int)(n * 100 + 0.5), mm = (int)(m * 100 + 0.5);
        for (i = 1; i * i * i <= mm * 10000; i++)
        {
            for (j = i; i * j * j <= mm * 10000; j++)
            {
                int a = i + j, b = i * j;
                if (b <= 10000 || 10000 * (i + j) % (i * j - 10000)) continue;
                int k = 10000 * (i + j) / (i * j - 10000);
                if (!Judge(i, j, k)) continue;
                else
                {
                    EQUATION tmp;
                    tmp.sum = (i + j + k) * 1.0 / 100;
                    tmp.a = i * 1.0 / 100; tmp.b = j * 1.0 / 100; tmp.c = k * 1.0 / 100;
                    ans.PB(tmp);
                }
            }
        }
        sort(ans.begin(), ans.end(), cmp);
        for (i = 0; i < SZ(ans); i++) printf("%.2f = %.2f + %.2f + %.2f = %.2f * %.2f * %.2f\n",
                                            ans[i].sum, ans[i].a, ans[i].b, ans[i].c, ans[i].a,
                                            ans[i].b, ans[i].c);
    }
    return 0;
}
```
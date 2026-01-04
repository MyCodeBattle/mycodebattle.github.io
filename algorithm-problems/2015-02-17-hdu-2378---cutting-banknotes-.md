---
categories: Posts
date: 2015-02-17 00:00:00
title: HDU 2378 - Cutting Banknotes (数学)
tags: []
layout: post
---

## 题意

给一个目标值k，下面给一些整数。  
这些整数只能对半分。

现在问能不能用这些整数凑成目标值，可以无限用。

## 思路

只能意会了。

## 代码


```c++
#include <stack>
#include <cstdio>
#include <list>
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
const double eps = 1e-8;
const int MAXN = 1e7 + 10;
const int MOD = 1e9 + 7;
const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };
const int hash_size = 4e5 + 10;
int cases = 0;
typedef pair<int, int> pii;

int main()
{
    //ROP;
    int T;
    scanf("%d", &T);
    while (T--)
    {
        double tmp;
        scanf("%lf", &tmp);
        int num;
        num = (int)round(tmp*100);
        int n, g;
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
        {
            int k;
            scanf("%d", &k);
            k *= 100;
            g = i ? __gcd(k, g) : k;
        }
        while ((g&1) == 0) g >>= 1;
        printf("%s\n", num % g ? "no" : "yes");
    }
    return 0;
}
```
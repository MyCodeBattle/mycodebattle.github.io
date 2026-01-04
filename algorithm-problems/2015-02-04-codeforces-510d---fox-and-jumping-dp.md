---
categories: Posts
date: 2015-02-04 00:00:00
title: Codeforces 510D - Fox And Jumping (DP)
tags: []
layout: post
---

## 题意

给出几个数字和他们的权值，要求选择k个数，他们能凑出所有的自然数，问最小权。

## 思路

最终目标是要凑出1. 几个数能凑的最小的正整数就是他们的GCD。递推一下。

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
const int MAXN = 300 + 10;
const int MOD = 29;
const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };
int cases = 0;
typedef pair<int, int> pii;
 
pii arr[MAXN];
map<int, int> mp;
int main()
{
    //ROP;
    int n;
    scanf("%d", &n);
    mp[0] = 0;
    for (int i = 0; i < n; i++) scanf("%d", &arr[i].X);
    for (int i = 0; i < n; i++) scanf("%d", &arr[i].Y);
    for (int i = 0; i < n; i++)
    {
        map<int, int>::iterator it = mp.begin();
        map<int, int> tmp;
        for (; it != mp.end(); it++)
        {
            int num = __gcd(it->X, arr[i].X);
            int cost = it->Y + arr[i].Y;
            if (!mp.count(num) || mp[num] > cost)
            {
                if (tmp.count(num) && tmp[num] < cost) continue;
                tmp[num] = cost;
            }
        }
        for (it = tmp.begin(); it != tmp.end(); it++) mp[it->X] = it->Y;
    }
    printf("%d\n", mp.count(1) ? mp[1] : -1);
    return 0;
}
```
---
categories: Posts
date: 2015-02-22 00:00:00
title: SDUT 2886 - Weighted Median (思维)
tags: []
layout: post
---

## 题意

找出一个数，满足题目的要求，复杂度为$O(n)$

## 思路

题目要求$O(n)$，在最坏情况下。感觉不太可能，用快排的思想均摊好像才是$O(n)$。

类似于快排找中位数。

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
const double eps = 1e-8;
const int MAXN = 1e7 + 2;
const int MOD = 1e9 + 7;
const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };
int cases = 0;
typedef pair<int, int> pii;
  
LL sum;
  
struct NODE
{
    int first, second;
}arr[MAXN];
  
LL QuickSort(int l, int r, LL small, LL large)
{
    int index = l, pivot = arr[l].X;
    swap(arr[l], arr[r]);
    for (int i = l; i < r; i++)
        if (arr[i].X < pivot) swap(arr[index++], arr[i]);
    swap(arr[index], arr[r]);
    LL sm = 0, equ = 0, big = 0;
    for (int i = l; i <= r; i++)
    {
        if (arr[i].X < pivot) sm += arr[i].Y;
        else if (arr[i].X == pivot) equ += arr[i].Y;
        else big += arr[i].Y;
    }
    if ((small+sm)*2 < sum && (large+big)*2 <= sum) return pivot;
    if ((small+sm)*2 >= sum) return QuickSort(l, index-1, small, large+equ+big);
    while (index < r && arr[index].X == arr[index+1].X) index++;
    if ((large+big)*2 > sum) return QuickSort(index+1, r, small+equ+sm, large);
}
  
int main()
{
    //ROP;
    int n;
    while (~scanf("%d", &n))
    {
        sum = 0;
        for (int i = 0; i < n; i++)
            scanf("%d", &arr[i].X);
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &arr[i].Y);
            sum += arr[i].Y;
        }
        printf("%lld\n", QuickSort(0, n-1, 0, 0));
    }
    return 0;
}
```
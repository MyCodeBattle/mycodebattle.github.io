---
categories: Posts
date: 2014-08-27 00:00:00
title: HDU 1394 - Minimum Inversion Number
tags: []
layout: post
---

## 传送门

[HDU 1394 - Minimum Inversion Number](http://www.bnuoj.com/v3/problem_show.php?pid=5594)

## 题意

循环移位数组中的元素，求逆序对最少数量

## 思路

考虑在第i个数字加入之前有几个比他小，用总的数量减去就是当前逆序对数。第一组答案求出来以后后面可以根据这个答案算出来。

## 代码（BIT）


```c++
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
#define LL long long
#define lowbit(x) ((x) & (-x))
const int MAXN = 5000 + 10;
const int INF = 0x3f3f3f3f;
 
int n, cnt[MAXN], a[MAXN];
 
int Sum(int num)
{
    int ret = 0;
    while (num > 0)
    {
        ret += cnt[num];
        num -= lowbit(num);
    }
    return ret;
}
 
void Add(int num)
{
    while (num <= n)
    {
        cnt[num]++;
        num += lowbit(num);
    }
}
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int i, j;
    while (~scanf("%d", &n))
    {
        int sum = 0, ans = INF;
        for (i = 0; i < n; i++)
        {
            scanf("%d", &a[i]);
            a[i]++;
            sum += Sum(n) - Sum(a[i]);
            Add(a[i]);
        }
        for (i = 0; i < n; i++)
        {
            sum = sum - 2 * a[i] + 1 + n;
            ans = min(ans, sum);
        }
        printf("%d\n", ans);
    }
    return 0;
}
```
 

## 线段树


```c++
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
#define LL long long
#define lowbit(x) ((x) & (-x))
const int MAXN = 5000 + 10;
const int INF = 0x3f3f3f3f;
 
struct SEG
{
    int l, r, sum;
}segt[MAXN << 2];
 
int a[MAXN];
 
void PushUp(int cur)
{
    segt[cur].sum = segt[cur << 1].sum + segt[cur << 1 | 1].sum;
}
 
void Build(int cur, int l, int r)
{
    segt[cur].l = l, segt[cur].r = r;
    if (segt[cur].l == segt[cur].r)
    {
        segt[cur].sum = 0;
        return;
    }
    int mid = l + ((r - l) >> 1);
    Build(cur << 1, l, mid);
    Build(cur << 1 | 1, mid + 1, r);
    segt[cur].sum = 0;
}
 
int Query(int cur, int l, int r)
{
    if (segt[cur].l == l && segt[cur].r == r)
        return segt[cur].sum;
    int mid = segt[cur].l + ((segt[cur].r - segt[cur].l) >> 1);
    if (r <= mid)
        return Query(cur << 1, l, r);
    else if (l > mid)
        return Query(cur << 1 | 1, l, r);
    else
        return Query(cur << 1, l, mid) + Query(cur << 1 | 1, mid + 1, r);
}
 
void Add(int cur, int val)
{
    if (segt[cur].l == segt[cur].r)
    {
        segt[cur].sum = 1;
        return;
    }
    int mid = segt[cur].l + ((segt[cur].r - segt[cur].l) >> 1);
    mid >= val ? Add(cur << 1, val) : Add(cur << 1 | 1, val);
    PushUp(cur);
}
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int n, i, j;
    while (~scanf("%d", &n))
    {
        Build(1, 0, n - 1);
        for (i = 0; i < n; i++)
            scanf("%d", &a[i]);
        int sum = 0, ans = INF;
        for (i = 0; i < n; i++)
        {
            sum += Query(1, a[i], n - 1);
            Add(1, a[i]);
        }
        ans = sum;
        for (i = 0; i < n; i++)
        {
            sum = sum - 2 * a[i] - 1 + n;
            ans = min(ans, sum);
        }
        printf("%d\n", ans);
    }
    return 0;
}
```
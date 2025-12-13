---
categories: Posts
date: 2014-11-01 00:00:00
title: ZSTU 3113 - Interval Challenge (树状数组 + 离散化)
tags: []
layout: post
---

## 题意

统计每个区间被覆盖的次数。

## 思路

这题的排序方法有点巧妙。把区间的范围从大到小排列，然后按Y从大到小排列。这样的话统计X的时候能统计到的都是可以覆盖当前区间的区间。

其他的没什么好说了，离散化一下就行。

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
#include <string>
#include <map>
#include <cmath>
#define LL long long
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
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
using namespace std;
const int MAXN = 2e5 + 10;
const int MOD = 1e9 + 7;
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
struct POINT
{
    int l, r, id;
    bool operator < (const POINT &a) const
    {
        if (r != a.r) return r > a.r;
        return l < a.l;
    }
}pit[MAXN];
 
int C[MAXN];
 
int Sum(int n)
{
    int ret = 0;
    while (n > 0)
    {
        ret += C[n];
        n -= Lowbit(n);
    }
    return ret;
}
 
void Update(int n)
{
    while (n <= MAXN)
    {
        C[n]++;
        n += Lowbit(n);
    }
}
 
map<pii, int> nmp;
map<int, int> mp;
vector<int> pre;
int ans[MAXN];
 
int main()
{
    //ROP;
    int n, i, j;
    while (~scanf("%d", &n))
    {
        MS(C, 0);
        mp.clear(); pre.clear(); nmp.clear();
        for (i = 0; i < n; i++)
        {
            int a, b;
            pit[i].id = i;
            scanf("%d%d", &pit[i].l, &pit[i].r);
            pre.PB(pit[i].l);
        }
        sort(pre.begin(), pre.end());
        int realNum = unique(pre.begin(), pre.end()) - pre.begin();
        for (i = 0; i < realNum; i++) mp[pre[i]] = i + 1;
        sort(pit, pit + n);
        ans[pit[0].id] = 0;
        Update(mp[pit[0].l]);
        for (i = 1; i < n; i++)
        {
            if (pit[i].l == pit[i - 1].l && pit[i].r == pit[i - 1].r)
                ans[pit[i].id] = ans[pit[i - 1].id];
            else ans[pit[i].id] = Sum(mp[pit[i].l]);
            Update(mp[pit[i].l]);
        }
        for (i = 0; i < n; i++)
        {
            if (i) printf(" %d", ans[i]);
            else printf("%d", ans[i]);
        }
        puts("");
    }
    return 0;
}
```
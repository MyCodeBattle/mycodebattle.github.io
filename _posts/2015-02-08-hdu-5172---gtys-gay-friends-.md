---
categories: Posts
date: 2015-02-08 00:00:00
title: HDU 5172 - GTY's gay friends (线段树)
tags: []
layout: post
---

## 思路

如何判断一段区间内从1~r-l+1？

  1. 判断这个区间内有没有重复的元素。
  2. 判断区间的最小元素是不是1。
  3. 判断区间的最大元素是不是r-l+1。


用线段树维护区间的最小元素和最大元素。本来可以顺便通过维护一个数之前出现的位置来判断有无重复元素的，但是这样就TLE了，感觉被卡log了。有点SXBK。

换个方法判断有无重复元素。

也是用一个数组记录这个数之前出现的位置，然后再用一个数组ans[pos]，表示pos之前自己和其他元素出现位置的最后一个位置（请原谅我语言能力有点退化）

对于一个区间$[l, r]$，如果ans[r]>=l，说明在l到r之间有某个元素的上一次出现在区间里。直接puts。

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
const int MAXN = 1e6 + 10;
const int MOD = 10000007;
const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };
int cases = 0;
typedef pair<int, int> pii;
 
struct SEGMENT
{
    int maxValue, minValue;
}t[MAXN<<2];
 
int Query(int rt, int l, int r, int L, int R, int type)
{
    if (L <= l && r <= R)
           return type == 1 ? t[rt].maxValue : t[rt].minValue;
    int mid = MID(l, r), ret = (type == 2 ? INF : 0);
    if (type == 1)
    {
        if (L <= mid) ret = max(ret, Query(LC, L, R, type));
        if (mid < R) ret = max(ret, Query(RC, L, R, type));
    }
    else
    {
        if (L <= mid) ret = min(ret, Query(LC, L, R, type));
        if (mid < R) ret = min(ret, Query(RC, L, R, type));
    }
    return ret;
}
 
int lft[MAXN], arr[MAXN], pre[MAXN], ans[MAXN];
 
void PushUp(int rt)
{
    t[rt].maxValue = max(t[LRT].maxValue, t[RRT].maxValue);
    t[rt].minValue = min(t[LRT].minValue, t[RRT].minValue);
}
 
void Build(int rt, int l, int r)
{
    if (l == r)
    {
        t[rt].minValue = t[rt].maxValue = arr[l];
        return;
    }
    int mid = MID(l, r);
    Build(LC); Build(RC);
    PushUp(rt);
}
 
int main()
{
    //ROP;
    int n, m;
    while (~scanf("%d%d", &n, &m))
    {
        MS(pre, 0);
        for (int i = 1; i <= n; i++)
        {
            scanf("%d", &arr[i]);
            lft[i] = pre[arr[i]];
            pre[arr[i]] = i;
        }
        Build(1, 1, n);
        int pos = 0;
        for (int i = 1; i <= n; i++)
        {
            if (lft[i] > 0) pos = max(pos, lft[i]);
            ans[i] = pos;
        }
        while (m--)
        {
            int a, b;
            scanf("%d%d", &a, &b);
            if (ans[b] >= a)
            {
                puts("NO");
                continue;
            }
            int maxValue = Query(1, 1, n, a, b, 1);
            int minValue = Query(1, 1, n, a, b, 2);
            puts(maxValue == b-a+1 && minValue == 1 ? "YES" : "NO");
        }
    }
    return 0;
}
```
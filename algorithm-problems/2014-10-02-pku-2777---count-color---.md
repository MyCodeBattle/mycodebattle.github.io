---
categories: Posts
date: 2014-10-02 00:00:00
title: PKU 2777 - Count Color (线段树 + 区间修改)
tags: []
layout: post
---

## 思路

线段树练习第四发

一开始用set判重，TLE了。

后来压缩了一下

这题和前几题都差不多，一开始不想写。

但是写的时候一直WA，也发现了自己的一些问题。

所以题海战术还是有用的╮(╯▽╰)╭

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
const int MAXN = 1e5 + 5;
const int MOD = 20071027;
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
int col[MAXN << 2], cnt;
set<int> mp;
 
void PushDown(int rt)
{
    if (col[rt])
    {
        col[LRT] = col[RRT] = col[rt];
        col[rt] = 0;
        return;
    }
}
 
void Query(int rt, int l, int r, int L, int R)
{
    if (col[rt])
    {
        cnt |= (1 << col[rt]);
        return;
    }
    int mid = MID(l, r);
    if (L <= mid) Query(LC, L, R);
    if (R > mid) Query(RC, L, R);
}
 
void Update(int rt, int l, int r, int L, int R, int val)
{
    if (L <= l && r <= R)
    {
        col[rt] = val;
        return;
    }
    PushDown(rt);
    int mid = MID(l, r);
    if (L <= mid) Update(LC, L, R, val);
    if (R > mid) Update(RC, L, R, val);
}
 
void Build(int rt, int l, int r)
{
    col[rt] = 1;
    if (l == r) return;
    int mid = MID(l, r);
    Build(LC); Build(RC);
}
 
int main()
{
    //ROP;
    int n, i, j, nQuary, nCol;
    while (~scanf("%d%d%d", &n, &nCol, &nQuary))
    {
        Build(1, 1, n);
        char str[2];
        int a, b, c;
        for (i = 0; i < nQuary; i++)
        {
            scanf("%s", str);
            if (str[0] == 'C')
            {
                scanf("%d%d%d", &a, &b, &c);
                if (a > b) swap(a, b);
                Update(1, 1, n, a, b, c);
            }
            else
            {
                MS(vis, 0), cnt = 0;
                scanf("%d%d", &a, &b);
                if (a > b) swap(a, b);
                Query(1, 1, n, a, b);
                printf("%d\n", BitCount(cnt));
            }
        }
    }
    return 0;
}
```
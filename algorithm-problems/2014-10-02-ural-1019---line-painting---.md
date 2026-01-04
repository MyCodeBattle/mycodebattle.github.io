---
categories: Posts
date: 2014-10-02 00:00:00
title: URAL 1019 - Line Painting (线段树 + 区间修改)
tags: []
layout: post
---

## 思路

被区间表示整了一个晚上。

和POJ那题一样，离散化，插点

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
const int MAXN = 10000 + 5;
const int MOD = 20071027;
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
struct POINT
{
    int l, r;
    char ch;
}pit[MAXN];
 
int col[MAXN << 4], cnt, vis[MAXN << 1];
vector<int> num;
 
void PushDown(int rt)
{
    if (col[rt] != -1)
    {
        col[LRT] = col[RRT] = col[rt];
        col[rt] = -1;
    }
}
 
void Query(int rt, int l, int r)
{
    if (col[rt] != -1)
    {
        if (col[rt] == 0)
            fill(vis + l, vis + r + 1, 1);
        return;
    }
    if (l == r) return;
    int mid = MID(l, r);
    Query(LC); Query(RC);
}
 
void Update(int rt, int l, int r, int L, int R, int val)
{
    if (L <= l && r <= R)
    {
        col[rt] = val;
        return;
    }
    if (col[rt] == val) return;
    PushDown(rt);
    int mid = MID(l, r);
    if (L <= mid) Update(LC, L, R, val);
    if (R > mid) Update(RC, L, R, val);
}
 
int main()
{
    //ROP;
    int n, i, j;
    while (~scanf("%d", &n))
    {
        MS(vis, 0);
        num.clear();
        char ch[2];
        for (i = 0; i < n; i++)
        {
            scanf("%d%d%s", &pit[i].l, &pit[i].r, ch);
            pit[i].ch = ch[0];
            num.PB(pit[i].l); num.PB(pit[i].r);
        }
        num.PB(0); num.PB(1e9);
        sort(num.begin(), num.end());
        int m = unique(num.begin(), num.end()) - num.begin();
        num.resize(m);
        for (i = 0; i < m - 1; i++)
            if (num[i] + 1 != num[i + 1]) num.PB(num[i] + 1);
        sort(num.begin(), num.end());
        int curSize = SZ(num);
        for (i = 0; i < n; i++)
        {
            int l = lower_bound(num.begin(), num.end(), pit[i].l) - num.begin();
            int r = lower_bound(num.begin(), num.end(), pit[i].r) - num.begin();
            if (pit[i].ch == 'w') Update(1, 0, curSize - 1, l + 1, r, 0);
            else Update(1, 0, curSize - 1, l + 1, r, 1);
        }
        Query(1, 0, curSize - 1);
        int ans = 1, L = 0, R = 1;
        for (i = 1; i < curSize; i++)
        {
            if (vis[i])
            {
                for (j = i + 1; j < curSize && vis[j]; j++);
                int cnt = num[j - 1] - num[i - 1];
                if (cnt > ans)
                {
                    ans = cnt;
                    L = i - 1, R = j - 1;
                }
                i = j - 1;
            }
        }
        printf("%d %d\n", num[L], num[R]);
    }
    return 0;
}
```
---
categories: Posts
date: 2015-02-28 00:00:00
title: HDU 3333 - Turing Tree (树状数组 + 离线处理)
tags: []
layout: post
---

## 题意

询问区间内不重复数字的和

## 思路

第一次写离线处理询问的题目。

离线后按右端点从小到大排序，用map判断当前位置上的数是否已经出现过，如果出现过就把以前的删掉，换到这里来。

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
const int MAXN = 3e4 + 10;
const int MOD = 9901;
const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };
int cases = 0;
typedef pair<int, int> pii;
 
struct POINT
{
    int x, y, id;
    bool operator < (const POINT &a) const
    {
        return y < a.y;
    }
}qarr[100000 + 10];
 
int arr[MAXN];
LL C[MAXN], ans[100000 + 10];
 
void Update(int pos, int val)
{
    while (pos < MAXN)
    {
        C[pos] += val;
        pos += Lowbit(pos);
    }
}
 
LL Query(int pos)
{
    LL ret = 0;
    while (pos > 0)
    {
        ret += C[pos];
        pos -= Lowbit(pos);
    }
    return ret;
}
 
map<int, int> mp;
 
int main()
{
    //ROP;
    int T;
    scanf("%d", &T);
    while (T--)
    {
        MS(C, 0);
        mp.clear();
        int n;
        cin >> n;
        for (int i = 1; i <= n; i++) scanf("%d", &arr[i]);
        int q;
        cin >> q;
        for (int i = 0; i < q; i++)
        {
            scanf("%d%d", &qarr[i].x, &qarr[i].y);
            qarr[i].id = i;
        }
        sort(qarr, qarr+q);
        int pos = 1;
        for (int i = 0; i < q; i++)
        {
            while (pos <= qarr[i].y)
            {
                if (mp[arr[pos]]) Update(mp[arr[pos]], -arr[pos]);
                mp[arr[pos]] = pos;
                Update(pos, arr[pos]);
                pos++;
            }
            ans[qarr[i].id] = Query(qarr[i].y) - Query(qarr[i].x-1);
        }
        for (int i = 0; i < q; i++) printf("%I64d\n", ans[i]);
    }
    return 0;
}
```
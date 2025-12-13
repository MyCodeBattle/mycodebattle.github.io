---
categories: Posts
date: 2015-02-01 00:00:00
title: UVa 202 - Repeating Decimals (模拟)
tags: []
layout: post
---

## 题意

找出一个分数中的循环节，如果超过50位小数输出部分。

## 思路

模拟即可。

这题也不难，写着有种难受的感觉。。

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
const int MAXN = 3e3 + 10;
const int MOD = 1e9 + 7;
const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };
int cases = 0;
typedef pair<int, int> pii;
 
int vis[MAXN];
 
int main()
{
    //ROP;
    int a, b;
    while (~scanf("%d%d", &a, &b))
    {
        MS(vis, -1);
        vector<int> ans;
        printf("%d/%d = %d.", a, b, a/b);
        a %= b;
        int cnt = 0, st, ed;
        while (true)
        {
            if (vis[a] != -1)
            {
                st = vis[a];
                ed = cnt;
                break;
            }
            vis[a] = cnt++;
            a *= 10;
            ans.PB(a / b);
            a %= b;
        }
        for (int i = 0; i < st; i++) printf("%d", ans[i]);
        putchar('(');
        for (int i = st; i < min(ed, 50); i++) printf("%d", ans[i]);
        if (ed > 50) printf("...)");
        else putchar(')');
        puts("");
        printf("   %d = number of digits in repeating cycle\n\n", ed - st);
    }
    return 0;
}
```
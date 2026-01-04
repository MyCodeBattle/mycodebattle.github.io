---
categories: Posts
date: 2014-10-12 00:00:00
title: HDU 5063 - Operation the Sequence (置换)
tags: []
layout: post
---

## 题意

给出三个操作和一个询问，输出询问。

## 思路

参考了某位大大的思路。

因为只要询问50组，所以不必把操作全部的数，只要记录下操作顺序，然后碰到一个询问的时候逆推回去就行。太机智了

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
const int MAXN = 1e5 + 10;
const int MOD = 1e9 + 7;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
int fun[3][MAXN];
vector<int> icmd;
 
int main()
{
    //ROP;
    int T, i, j, n, m;
    scanf("%d", &T);
    while (T--)
    {
        j = 1;
        icmd.clear();
        scanf("%d%d", &n, &m);
        for (i = 1; i <= n; i += 2) fun[1][j++] = i;
        for (i = 2; i <= n; i += 2) fun[1][j++] = i;
        j = 1;
        for (i = n; i >= 1; i--) fun[2][j++] = i;
        int cnt = 0;
        while (m--)
        {
            char cmd[3];
            int a;
            scanf("%s%d", cmd, &a);
            if (cmd[0] == 'O')
            {
                if (a == 3) cnt++;
                else icmd.PB(a);
            }
            else
            {
                LL x = a;
                for (i = SZ(icmd) - 1; i >= 0; i--) x = fun[icmd[i]][x];
                for (i = 1; i <= cnt; i++) x = x * x % MOD;
                printf("%I64d\n", x);
            }
        }
    }
    return 0;
}
```
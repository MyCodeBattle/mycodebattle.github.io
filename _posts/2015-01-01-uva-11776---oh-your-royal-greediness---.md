---
categories: Posts
date: 2015-01-01 00:00:00
title: UVa 11776 - Oh Your Royal Greediness! (贪心 + 模拟)
tags: []
layout: post
---

## 题意

有N个农民要收割农田，给出一个开始时间和结束时间，问最少要派几个人去监督

## 思路

贪心一下，按开始时间从小到大排一下。

然后这时候就开始模拟了。

用一个优先队列维护可用的人，如果当前农民的开始时间比Q.top要大，说明空一个人，不用加人，否则ans++  
最后这个人入队，入队的是结束的时间。

## 代码


```c++
#include <cstdio>
#include <stack>
#include <list>
#include <set>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <functional>
#include <cstring>
#include <iomanip>
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
#define BitCount(x) __builtin_popcount(x)
#define BitCountll(x) __builtin_popcountll(x)
#define LeftPos(x) 32 - __builtin_clz(x) - 1
#define LeftPosll(x) 64 - __builtin_clzll(x) - 1
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
const double eps = 1e-8;
const int MAXN = 1000 + 10;
const int MOD = 1000007;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
int cases = 0;
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
pii evt[MAXN];
priority_queue<int, vector<int>, greater<int> > Q;
 
int main()
{
    //ROP;
    int n, i, j;
    while (scanf("%d", &n), n != -1)
    {
        while (!Q.empty()) Q.pop();
        for (i = 0; i < n; i++)
        {
            int a, b;
            scanf("%d%d", &a, &b);
            evt[i] = {a, b};
        }
        sort(evt, evt + n);
        int ans = 0;
        for (i = 0; i < n; i++)
        {
            if (Q.empty()) ans++;
            else
            {
                int limit = Q.top();
                if (limit >= evt[i].X) ans++;
                else Q.pop();
            }
            Q.push(evt[i].Y);
        }
        printf("Case %d: %d\n", ++cases, ans);
    }
    return 0;
}
```
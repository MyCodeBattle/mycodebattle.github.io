---
categories: Posts
date: 2014-11-01 00:00:00
title: UVa 1153 - Keep the Customer Satisfied (贪心 + 优先队列)
tags: []
layout: post
---

## 题意

输出能完成的最大任务数

## 思路

一开始写了二分 + DFS，果断TLE。

后来想了很久也没想到什么好办法，参考了别人的思路。

这思路也挺神奇的，用优先队列维护一个最大任务时间。

先排序  
如果加上curLast（当前任务持续时间）会超出curDeath，就pop掉队里的最大curLast。

对此我想(ma)了(hou)想(pao)。如果curLast小于maxLast，显然把maxLast的那个任务不选，选择当前的这个任务较优。因为这样不仅能多放一个任务，还可以给后面腾出时间。

如果curLast > maxLast，那么不管替换还是不替换，不选择的任务数始终会增加一个。而且当后面任务来的时候总要被替换下来。

所以最后统计出的是被换下的任务数，用总数减一下就行。

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
#define BitCountll(x) __builtin_popcountll(x)
#define LeftPos(x) 32 - __builtin_clz(x) - 1
#define LeftPosll(x) 64 - __builtin_clzll(x) - 1
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
using namespace std;
const int MAXN = 800000 + 10;
const int MOD = 1000007;
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
struct POINT
{
    int last, death;
    bool operator < (const POINT &a) const
    {
        if (death != a.death) return death < a.death;
        return last < a.last;
    }
}pit[MAXN];
 
int n;
priority_queue<int> pqu;
 
int Solve()
{
    int curTime = 0, ans = 0;
    for (int i = 0; i < n; i++)
    {
        curTime += pit[i].last;
        pqu.push(pit[i].last);
        if (curTime > pit[i].death)
        {
            curTime -= pqu.top();
            pqu.pop();
            ans++;
        }
    }
    return ans;
}
 
int main()
{
    //ROP;
    int T, i, j;
    scanf("%d", &T);
    while (T--)
    {
        while (!pqu.empty()) pqu.pop();
        scanf("%d", &n);
        for (i = 0; i < n; i++) scanf("%d%d", &pit[i].last, &pit[i].death);
        sort(pit, pit + n);
        printf("%d\n", n - Solve());
        if (T) printf("\n");
    }
    return 0;
}
```
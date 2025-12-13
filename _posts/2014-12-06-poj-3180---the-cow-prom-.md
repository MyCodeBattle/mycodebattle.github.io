---
categories: Posts
date: 2014-12-06 00:00:00
title: POJ 3180 - The Cow Prom (强连通)
tags: []
layout: post
---

## 题意

输出图中强连通分支中顶点大于等于2的数量。

## 思路

明白题目意思就很好做了。

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
#include <string>
#include <map>
#include <iomanip>
#include <cmath>
#define LL long long
#define ULL unsigned long long
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
const double eps = 1e-6;
const int MAXN = 2e5 + 10;
const int MOD = 1000007;
const int dir[][2] = { {1, 0}, {-1, 0}, {0, -1}, {0, 1} };
 
int SCCCnt, DFSClock, pre[MAXN], lowlink[MAXN], sccno[MAXN];
stack<int> st;
vector<int> G[MAXN];
map<int, int> mp;
 
void DFS(int from)
{
    pre[from] = lowlink[from] = ++DFSClock;
    st.push(from);
    for (int i = 0; i < SZ(G[from]); i++)
    {
        int to = G[from][i];
        if (!pre[to])
        {
            DFS(to);
            lowlink[from] = min(lowlink[from], lowlink[to]);
        }
        else if (!sccno[to]) lowlink[from] = min(lowlink[from], pre[to]);
    }
    if (lowlink[from] == pre[from])
    {
        SCCCnt++;
        while (1)
        {
            int x = st.top(); st.pop();
            sccno[x] = SCCCnt;
            if (x == from) break;
        }
    }
}
 
void FindSCC(int n)
{
    DFSClock = SCCCnt = 0;
    MS(sccno, 0); MS(pre, 0);
    for (int i = 1; i <= n; i++)
        if (!pre[i]) DFS(i);
}
 
int main()
{
    //ROP;
    int n, m, i, j;
    while (~scanf("%d%d", &n, &m))
    {
        for (int i = 0; i <= n; i++) G[i].clear();
        mp.clear();
        for (i = 0; i < m; i++)
        {
            int from, to;
            scanf("%d%d", &from, &to);
            G[from].PB(to);
        }
        FindSCC(n);
        for (int i = 1; i <= n; i++)
            mp[sccno[i]]++;
        int ans = 0;
        map<int, int>::iterator it;
        for (it = mp.begin(); it != mp.end(); it++)
            if (it->S >= 2) ans++;
        printf("%d\n", ans);
    }
    return 0;
}
```
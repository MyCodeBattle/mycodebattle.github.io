---
categories: Posts
date: 2014-09-01 00:00:00
title: UVa 669 - Defragment (DFS)
tags: []
layout: post
---

## 题意

这题看了好久才懂什么意思。

简单地说就是给出一个数字原来的位置，和最后的位置，求移动顺序。

输入簇(cluster)的总数和文件个数，每个文件个数后面跟着的是各个簇的原始位置。最后要按顺序排下来。

## 思路

分两种情况。

  1. 如果没有环，直接DFS然后换掉。

  2. 如果有环，从后面开始找到第一个空的位置，然后把数移过去，然后就递归了。


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
#define lowbit(x) ((x) & (-x))
#define MP(a, b) make_pair(a, b)
#define MS(arr, num) memset(arr, num, sizeof(arr))
#define PB push_back
#define F first
#define S second
#define ROP freopen("input.txt", "r", stdin);
#define BitCount(x) __builtin_popcount(x)
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
using namespace std;
const int MAXN = 1e4 + 100;
const int MOD = 20071027;
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
int num[MAXN], vis[MAXN], N;
 
void DFS(int n)
{
    if (num[num[n]] == 0)
    {
        printf("%d %d\n", n, num[n]);
        num[num[n]] = -1;
        num[n] = 0;
        return;
    }
    if (vis[num[num[n]]])
    {
        for (int i = N; i > 0; i--)
        {
            if (num[i] == 0)
            {
                printf("%d %d\n", n, i);
                num[i] = num[n];
                num[n] = 0;
                return;
            }
        }
    }
    vis[n] = 1;
    DFS(num[n]);
    printf("%d %d\n", n, num[n]);
    num[num[n]] = -1;
    num[n] = 0;
}
 
int main()
{
    //ROP;
    int T, i, j, nfile, n;
    scanf("%d", &T);
    while (T--)
    {
        MS(num, 0);
        int pos = 1, tmp;
        scanf("%d%d", &N, &nfile);
        for (i = 0; i < nfile; i++)
        {
            scanf("%d", &n);
            for (j = 0; j < n; j++)
            {
                scanf("%d", &tmp);
                num[tmp] = pos++;
                if (tmp == pos - 1) num[tmp] = -1;  //already placed in the correct position
            }
        }
        bool rec = false;
        for (i = 1; i <= N; i++)
        {
            if (num[i] && num[i] != -1)
            {
                MS(vis, 0);
                vis[i] = 1;
                DFS(i);
                rec = true;
            }
        }
        if (!rec) puts("No optimization needed");
        if (T) puts("");
    }
    return 0;
}
```
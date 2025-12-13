---
categories: Posts
date: 2015-03-28 00:00:00
title: Codeforces 525D - Arthur and Walls (思维)
tags: []
layout: post
---

## 题意

要求把联通的’.’变成矩形，输出最少炸墙的图形。

## 思路

一开始直接去找矩形了，后来有人给了一组数据，我这种思路是错的。

可以从小的方面考虑。

如果有三个’.’一个’*’，这个墙是必须得炸掉的。然后这个墙影响到了其他的墙，再检查被它影响到的墙。  
神奇！

## 代码


```c++
#include <stack>
#include <stdio.h>
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
const int MAXN = 2000 + 10;
const int MOD = 9901;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
int cases = 0;
typedef pair<int, int> pii;
 
char mp[MAXN][MAXN];
int n, m;
 
void Check(int x, int y)
{
    int cnt = 0;
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)
        {
            int xx = x + i, yy = y + j;
            if (!xx || !yy || xx > n || yy > m) return;
            if (mp[xx][yy] == '.') cnt++;
        }
    if (cnt != 3) return;
    pii test;
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)
        {
            if (mp[x+i][y+j] == '*') test.X = x+i, test.Y = y+j;
            mp[x+i][y+j] = '.';
        }
    for (int i = -1; i < 2; i++)
        for (int j = -1; j < 2; j++)
        {
            int xx = test.X + i, yy = test.Y + j;
            if (!xx || !yy || xx > n || yy > m) continue;
            Check(xx, yy);
        }
}
 
int main()
{
    //ROP;
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i++) scanf("%s", mp[i]+1);
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++) Check(i, j);
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++) putchar(mp[i][j]);
        puts("");
    }
    return 0;
}
```
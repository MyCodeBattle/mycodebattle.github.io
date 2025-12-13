---
categories: Posts
date: 2015-02-01 00:00:00
title: Codeforces 515D - Drazil and Tiles (拓扑排序)
tags: []
layout: post
---

## 题意

给一个图，问能不能用1 _2或者2_ 1的方块覆盖，并且只有一种覆盖方法。

## 思路

二维的拓扑排序。

引用一下**Peter** 的解释(<http://blog.csdn.net/uestc_peterpan/article/details/43875195>)

> 二维拓扑排序。
> 
>   1. 将所有度数为1的点加入队列；
>   2. 把队列里的一个点v1 和 与v1相邻的一个点v2 用1×2或2×1方格覆盖，再用v2更新周围点的度数，若更新后点度数为1，则加入队列；
>   3. 若2中存在一个v1无法与一个v2匹配，或者2结束后，存在一个点没有访问过，则无解或有多解；否则输出解即可。
> 


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
const int MAXN = 2e3 + 10;
const int MOD = 1e9 + 7;
const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };
const int hash_size = 4e5 + 10;
int cases = 0;
typedef pair<int, int> pii;
 
char mp[MAXN][MAXN];
int row, col, deg[MAXN][MAXN];
queue<pii> Q;
 
void AdjustDegree(int x, int y)
{
    for (int i = 0; i < 4; i++)
    {
        int xx = x + dir[i][0], yy = y + dir[i][1];
        deg[xx][yy]--;
        if (deg[xx][yy] == 1) Q.push({xx, yy});
    }
}
 
void GetDegree()
{
    for (int i = 1; i <= row; i++)
        for (int j = 1; j <= col; j++)
        {
            if (mp[i][j] != '.') continue;
            if (i > 1 && mp[i-1][j] == '.') deg[i][j]++;
            if (j > 1 && mp[i][j-1] == '.') deg[i][j]++;
            if (i < row && mp[i+1][j] == '.') deg[i][j]++;
            if (j < col && mp[i][j+1] == '.') deg[i][j]++;
            if (deg[i][j] == 1) Q.push({i, j});
        }
}
 
void Toposort()
{
    while (!Q.empty())
    {
        pii cur = Q.front(); Q.pop();
        int x = cur.X, y = cur.Y;
        if (mp[x-1][y] == '.')
        {
            mp[x][y] = 'v';
            mp[x-1][y] = '^';
            AdjustDegree(x-1, y);
        }
        else if (mp[x+1][y] == '.')
        {
            mp[x][y] = '^';
            mp[x+1][y] = 'v';
            AdjustDegree(x+1, y);
        }
        else if (mp[x][y+1] == '.')
        {
            mp[x][y] = '<';
            mp[x][y+1] = '>';
            AdjustDegree(x, y+1);
        }
        else if (mp[x][y-1] == '.')
        {
            mp[x][y] = '>';
            mp[x][y-1] = '<';
            AdjustDegree(x, y-1);
        }
        else
        {
            if (mp[x][y] == '.')
            {
                printf("Not unique\n");
                return;
            }
        }
    }
    for (int i = 1; i <= row; i++)
        for (int j = 1; j <= col; j++)
            if (mp[i][j] == '.') { puts("Not unique"); return; }
    for (int i = 1; i <= row; i++)
        printf("%s\n", mp[i]+1);
}
 
int main()
{
    //ROP;
    scanf("%d%d", &row, &col);
    for (int i = 1; i <= row; i++)
        scanf("%s", mp[i]+1);
    GetDegree();
    Toposort();
    return 0;
}
```
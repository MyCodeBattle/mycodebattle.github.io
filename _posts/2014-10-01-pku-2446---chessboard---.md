---
categories: Posts
date: 2014-10-01 00:00:00
title: PKU 2446 - Chessboard (最大匹配 & 匈牙利)
tags: []
layout: post
---

## 思路

每个格子和上下左右建立关系，这样得出来的最大匹配是正常的两倍，判断一下相不相等。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127128129130

| ```c++
#include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>#define LL long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 1600 + 10;const int MOD = 1e9 + 7;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} }; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int mp[50][50], num[50][50], nmat, nrem; struct EDGE{    int from, to;}; struct BIMATCHING{    int vis[MAXN], link[MAXN], head[MAXN], next[MAXN * MAXN];    vector<EDGE> edges;     int DFS(int u)    {        for (int i = head[u]; i != -1; i = next[i])        {            int &v = edges[i].to;            if (!vis[v])            {                vis[v] = 1;                if (link[v] == -1 || DFS(link[v]))                {                    link[v] = u;                    return 1;                }            }        }        return 0;    }     int hungary()    {        int res = 0;        for (int i = 1; i <= nrem; i++)        {            MS(vis, 0);            res += DFS(i);        }        return res;    }     void add_edge(int from, int to)    {        edges.PB((EDGE){from, to});        int m = SZ(edges);        next[m - 1] = head[from];        head[from] = m - 1;    }     void init()    {        MS(head, -1); MS(link, -1);        edges.clear();    }}hun; int main(){    //ROP;    int row, col, nhole, i, j;    while (~scanf("%d%d%d", &row, &col, &nhole))    {        MS(mp, 0); MS(num, 0);        hun.init();        int x, y;        for (i = 0; i < nhole; i++)        {            scanf("%d%d", &x, &y);            mp[y][x] = 1;        }        int cnt = 0;        for (i = 1; i <= row; i++)            for (j = 1; j <= col; j++)                if (!mp[i][j]) num[i][j] = ++cnt;        nmat = nrem = cnt;        for (i = 1; i <= row; i++)            for (j = 1; j <= col; j++)            {                if (!mp[i][j])                for (int k = 0; k < 4; k++)                {                    int xx = i + dir[k][0], yy = j + dir[k][1];                    if (xx >= 1 && xx <= row && yy >= 1 && yy <= col && !mp[xx][yy])                        hun.add_edge(num[i][j], num[xx][yy]);                }            }        printf("%s\n", (hun.hungary() == cnt ? "YES" : "NO"));    }    return 0;}
```
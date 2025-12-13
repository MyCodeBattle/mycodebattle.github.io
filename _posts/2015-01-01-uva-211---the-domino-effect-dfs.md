---
categories: Posts
date: 2015-01-01 00:00:00
title: UVa 211 - The Domino Effect (DFS)
tags: []
layout: post
---

#  [UVa 211 - The Domino Effect (DFS)](/2015/01/UVa-211/ "UVa 211 - The Domino Effect \(DFS\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jan 21 2015 16:05

**Contents**

  1. 1. 题意
  2. 2. 代码

## 题意

多米诺骨牌有28种型号，每种型号都由两个pip组成。

比如bone 1 是由 0和0组成的，bone 18是由2和6组成的。

现在给出一个pip组成的图，要求输出所有能组成的bone型号排列。

我会说我看懂题目花了一个小时吗TAT

对于每种型号的骨牌，要么横着放，要么竖着放。一直往右DFS + 回溯即可。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124

| 
    
    
    #include <stack>#include <cstdio>#include <list>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)#define BitCountll(x) __builtin_popcountll(x)#define LeftPos(x) 32 - __builtin_clz(x) - 1#define LeftPosll(x) 64 - __builtin_clzll(x) - 1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 4e5 + 10;const int MOD = 1000007;const int dir[][2] = { {1, 0}, {0, 1} };int cases = 0;typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; const int row = 7, col = 8;int mp[row][col], cvt[row][col], vis[30], pip[row][col];int cnt; bool Input(){    for (int i = 0; i < row; i++)        for (int j = 0; j < col; j++) if (scanf("%d", &pip[i][j]) == -1) return false;    return true;} void Init(){    int num = 1;    cnt = 0;    for (int i = 0; i < row; i++)        for (int j = i; j < row; j++) cvt[i][j] = cvt[j][i] = num++;} void Output(int p[7][8]){    for (int i = 0; i < row; i++)    {        for (int j = 0; j < col; j++) printf("%4d", p[i][j]);        puts("");    }    puts("");} void DFS(int x, int y){    if (y == col)    {        x++, y = 0;        if (x == row)        {            cnt++;            Output(mp);            return;        }    }    if (mp[x][y]) DFS(x, y + 1);    else    {        for (int i = 0; i < 2; i++)        {            int xx = x + dir[i][0], yy = y + dir[i][1];            if (xx < row && yy < col && !mp[xx][yy])            {                int bone = cvt[pip[x][y]][pip[xx][yy]];                if (vis[bone]) continue;                mp[x][y] = mp[xx][yy] = bone;                vis[bone] = 1;                DFS(x, y + 1);                vis[bone] = 0;                mp[x][y] = mp[xx][yy] = 0;            }        }    }} int main(){    //ROP;    Init();    while (1)    {        cnt = 0;        if (!Input()) break;        if (cases) printf("\n\n\n");        printf("Layout #%d:\n\n", ++cases);        Output(pip);        printf("Maps resulting from layout #%d are:\n\n", cases);        DFS(0, 0);        printf("There are %d solution(s) for layout #%d.\n", cnt, cases);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Foundation - Search](/tags/Foundation-Search/)

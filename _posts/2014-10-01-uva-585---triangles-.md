---
categories: Posts
date: 2014-10-01 00:00:00
title: UVa 585 - Triangles (枚举)
tags: []
layout: post
---

#  [UVa 585 - Triangles (枚举)](/2014/10/UVa-585/ "UVa 585 - Triangles \(枚举\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Oct 16 2014 20:54

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

找出最多的子三角形。

## 思路

观察得，当三角形朝上的时候只能往下扩展，反之则网上扩展。

所以当朝上的时候往下枚举，反之亦然。

以后要完全投奔BNUVJ了，改版了的VJUDGE好不习惯。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879808182

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>#define LL long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 150 + 10;const int MOD = 1e9 + 7;//const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} }; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int n, dir;char mp[MAXN][MAXN]; int DFS(int x, int y, int cnt){    if (x <= 0 || x == n) return cnt - 1;    if (dir == -1)    {        for (int i = y; i < 2 * cnt - 1 + y; i++)            if (mp[x][i] != '-') return cnt - 1;    }    else        for (int i = y - 2 * (cnt - 1); i <= y; i++)            if (mp[x][i] != '-') return cnt - 1;    return DFS(x + dir, y, cnt + 1);} int main(){   // ROP;    int i, j, cases = 0;    while (scanf("%d", &n), n)    {        MS(mp, 0);        bool flag = false;        int len = (n << 1) - 1;        for (i = 1; i <= n; i++) scanf("%s", mp[i] + 1);        int ans = 1;        for (i = 1; i <= n; i++)            for (j = 1; j <= len - (i - 1) * 2; j++)                if (mp[i][j] == '-')                {                    flag = true;                    dir = (j & 1 ? -1 : 1);                    ans = max(ans, DFS(i + dir, j, 2));                }        printf("Triangle #%d\n", ++cases);        if (!flag) ans = 0;        printf("The largest triangle area is %d.\n\n", ans * ans);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Foundation - Brute Force](/tags/Foundation-Brute-Force/)

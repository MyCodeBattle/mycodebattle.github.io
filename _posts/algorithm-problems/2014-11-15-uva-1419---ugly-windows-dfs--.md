---
categories: Posts
date: 2014-11-15 00:00:00
title: UVa 1419 - Ugly Windows (DFS + 暴力)
tags: []
layout: post
---

## 题意

找出有几个在顶端的窗口。需要满足以下条件

  1. 窗口里面只有’.’
  2. 窗口边缘是完整的。


## 思路

在浏览器标签上呆了一个星期的题目=。=  
今天标签实在是放不下了，就去A这题，空一点位置╮(╯▽╰)╭

  1. 找出完整的窗口。
  2. 判断这个窗口里面是不是全部是.


如何找出完整的窗口？  
碰到一个字母就DFS，如果从下往上走到起点，说明这个窗口是完整的。因此在起点的时候不能往下走。

如何判断2？  
枚举出当前窗口的边界，for一下。

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
const double eps = 1e-8;
const int MAXN = 100 + 10;
const int MOD = 1000007;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };  //0123，上下左右

typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;

char mp[MAXN][MAXN];
int vis[MAXN][MAXN], n, m;
pii tar;
vector<char> ans;

bool Check(char curWindow)
{
    int i, j;
    for (i = tar.F, j = tar.S; mp[i][j] == curWindow; j++);
    int len = j - 2;
    for (i = tar.F, j = tar.S; mp[i][j] == curWindow; i++);
    int wide = i - 2;
    for (i = tar.F + 1; i <= wide; i++)
        for (j = tar.S + 1; j <= len; j++)
            if (mp[i][j] != '.') return false;
    return true;
}

void DFS(int x, int y, char curWindow)
{
	if (mp[x][y] == '.' || mp[x][y] != curWindow) return;
	vis[x][y] = 1;
	for (int i = 0; i < 4; i++)
	{
	    if (i == 1 && x == tar.F && y == tar.S) continue;   //一开始的时候不能往下走
		int xx = x + dir[i][0], yy = y + dir[i][1];
		if (i == 0 && xx == tar.F && yy == tar.S)   //如果往上走能到达起点
        {
            if (Check(curWindow))
                ans.PB(curWindow);
        }
		if (xx >= 1 && xx <= n && yy >= 1 && yy <= m && !vis[xx][yy])
			DFS(xx, yy, curWindow);
	}
}

int main()
{
    //ROP;
	int i, j;
	while (scanf("%d%d", &n, &m), n + m)
	{
		ans.clear();
		MS(vis, 0);
		for (i = 1; i <= n; i++) scanf("%s", mp[i] + 1);
		for (i = 1; i <= n; i++)
			for (j = 1; j <= m; j++)
				if (!vis[i][j] && mp[i][j] != '.')
				{
				    tar.F = i, tar.S = j;
					DFS(i, j, mp[i][j]);

				}
        sort(ans.begin(), ans.end());
		for (i = 0; i < SZ(ans); i++) putchar(ans[i]);
		puts("");
	}
	return 0;
}
```
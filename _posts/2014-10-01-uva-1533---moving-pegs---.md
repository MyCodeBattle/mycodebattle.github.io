---
categories: Posts
date: 2014-10-01 00:00:00
title: UVa 1533 - Moving Pegs (隐式图搜索 + 状态压缩)
tags: []
layout: post
---

## 题意

15个格子组成的三角形，一开始给出一个空位置，问能不能最后剩下一个棋子并且正好在这个位置上。

## 思路

一开始想用回溯，不过这跳来跳去的实在没办法表示。后来看到题目说固定的15个位置，想到每个棋子能走的地方都可以列出来。那就干脆都列出来一一判断呗。

这题是一个隐式图遍历问题。

15个格子，可以状态压缩一下。

先把原始的状态图作为基准，然后就开始跳吧，如果能达到新的状态，入队，直到找到结果或者队伍为空

我知道位运算的优先级很低，没想到比等号还低，漏了一个括号从早上调到现在TAT

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
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
using namespace std;
const int MAXN = 100 + 10;
const int MOD = 1e9 + 7;
const int dir[][6] = { {-1,-1,-1,-1,-1,-1}, {-1,-1,-1,-1,2,3}, {-1,1,-1,3,4,5}, {1,-1,2,-1,5,6},
{-1,2,-1,5,7,8}, {2,3,4,6,8,9}, {3,-1,5,-1,9,10},
{-1,4,-1,8,11,12}, {4,5,7,9,12,13}, {5,6,8,10,13,14}
, {6,-1,9,-1,14,15}, {-1,7,-1,12,-1,-1}, {7,8,11,13,-1,-1}
, {8,9,12,14,-1,-1}, {9,10,13,15,-1,-1}, {10,-1,14,-1,-1,-1} };
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
struct STATE
{
    int state, rem, path[MAXN][2];
    int pos;
};
 
set<int> mp;
int emp;
queue<STATE> Q;
STATE ans;
 
void Solve()
{
    int iniState = 0;
    STATE st;
    for (int i = 1; i <= 15; i++)
        if (i != emp) iniState |= (1 << i);
    st.state = iniState; st.rem = 14; st.pos = 0;
    Q.push(st);
    while (!Q.empty())
    {
        STATE cur = Q.front(); Q.pop();
        const int tmpState = cur.state;
        for (int i = 1; i <= 15; i++)
        {
            if ((tmpState & (1 << i)) == 0) continue; //如果这个位置是黑色
            for (int j = 0; j < 6; j++)
            {
                STATE newState = cur;
                newState.state ^= (1 << i);
                if (dir[i][j] != -1 && (tmpState & (1 << dir[i][j])))
                {
                    int t = dir[i][j];      //接下来找这个方向白色的
                    newState.state -= (1 << t);
                    while (dir[t][j] != -1 && (tmpState & (1 << dir[t][j])))
                    {
                        newState.state -= (1 << dir[t][j]); newState.rem--;
                        t = dir[t][j];
                    }
                    if (dir[t][j] == -1) continue;
                    newState.state |= (1 << dir[t][j]); newState.rem--;
                    newState.path[newState.pos][0] = i; newState.path[newState.pos++][1] = dir[t][j];
                    if (mp.count(newState.state)) continue;
                    mp.insert(newState.state);
                    Q.push(newState);
                    //if (newState.rem == 1) printf("%d\n", dir[t][j]);
                    if (newState.rem == 1 && newState.state & (1 << emp)) //如果正好跳到空白点而且只剩一个
                    {
                        ans = newState;
                        return;
                    }
                }
            }
        }
    }
}
 
void Init()
{
    while (!Q.empty()) Q.pop();
    mp.clear();
    ans.pos = INF;
}
 
int main()
{
    //ROP;
    int T, i, j;
    scanf("%d", &T);
    while (T--)
    {
        Init();
        scanf("%d", &emp);
        if (emp < 1 || emp > 15) puts("IMPOSSIBLE");
        Solve();
        if (ans.pos == INF) puts("IMPOSSIBLE");
        else
        {
            printf("%d\n", ans.pos);
            for (i = 0; i < ans.pos; i++)
            {
                if (i) printf(" %d %d", ans.path[i][0], ans.path[i][1]);
                else printf("%d %d", ans.path[i][0], ans.path[i][1]);
            }
        }
        puts("");
    }
    return 0;
}
```
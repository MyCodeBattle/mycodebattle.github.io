---
categories: Posts
date: 2014-09-01 00:00:00
title: ACDream 1191 - Dragon Maze
tags: []
layout: post
---

#  [ACDream 1191 - Dragon Maze](/2014/09/ACDream-1191/ "ACDream 1191 - Dragon Maze")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 18 2014 21:51

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[ACDream 1191 - Dragon Maze](http://acdream.info/problem?pid=1191)

## 题意

给一个图，每个点有能量，求出在能走到终点的情况下的最大能量，或者走不到。

## 思路

用优先队列，这样可以保证每一次取出来的都是当前最小步数的最大能量！

重载结构体的小于号竟然无效？（求原因），只能写一个cmp函数。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879808182838485868788899091929394959697

| 
    
    
    #include <cstdio>#include <algorithm>#include <functional>#include <stack>#include <iostream>#include <string>#include <vector>#include <queue>#include <cstring>#include <string>#include <sstream>#include <map>#include <cmath>#define LL long long#define lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)const int MAXN = 1000 + 5;const int INF = 0x3f3f3f3f;using namespace std;  typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii;  struct POINT{    int x, y, eng, steps;    POINT()    {        x = y = eng = steps = 0;    }    POINT(int xx, int yy): x(xx), y(yy), eng(0), steps(0){}};  struct cmp{    bool operator() (const POINT &a, const POINT &b)    {        if (a.steps == b.steps) return a.eng < b.eng;        else return a.steps > b.steps;    }};  priority_queue<POINT, vector<POINT>, cmp>pqu;int mp[MAXN][MAXN], vis[MAXN][MAXN], row, col;const int dir[][2] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };POINT ed;  POINT BFS(POINT st){    while (!pqu.empty())        pqu.pop();    memset(vis, 0, sizeof vis);    pqu.push(st);    while (!pqu.empty())    {        POINT cur = pqu.top(); pqu.pop();        for (int i = 0; i < 4; i++)        {            int xx = cur.x + dir[i][0], yy = cur.y + dir[i][1];            if (!vis[xx][yy] && mp[xx][yy] != -1 && xx >= 0 && xx < row && yy >= 0 && yy < col)            {                vis[xx][yy] = 1;                POINT tmp(xx, yy);                tmp.eng = cur.eng + mp[xx][yy]; tmp.steps = cur.steps + 1;                if (xx == ed.x && yy == ed.y)                    return tmp;                pqu.push(tmp);            }        }    }    POINT fal;    return fal;}  int main(){    //freopen("input.txt", "r", stdin);    int T, i, j, cases = 0;    scanf("%d", &T);    while (T--)    {        POINT st;        scanf("%d%d", &row, &col);        scanf("%d%d%d%d", &st.x, &st.y, &ed.x, &ed.y);        for (i = 0; i < row; i++)            for (j = 0; j < col; j++) scanf("%d", ∓[i][j]);        st.eng = mp[st.x][st.y];        POINT ans = BFS(st);        printf("Case #%d: ", ++cases);        if (ans.steps != 0)            printf("%d\n", ans.eng);        else            puts("Mission Impossible.");    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - ACDream](/tags/Online-Judge-ACDream/)[Data Structure - Graph](/tags/Data-Structure-Graph/)

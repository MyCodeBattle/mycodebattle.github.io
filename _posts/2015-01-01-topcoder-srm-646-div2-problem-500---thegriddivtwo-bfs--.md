---
categories: Posts
date: 2015-01-01 00:00:00
title: TopCoder SRM 646 Div2 Problem 500 - TheGridDivTwo (BFS + 优先队列)
tags: []
layout: post
---

## 题意

在一个地图上，给出一些不能走的点，给出限定的秒数，问能在X轴上走最远是多少

## 思路

一开始用DFS + 剪枝，剪了很久剪不过去。

后来用BFS。

要用优先队列的原因是我们必须保证每拿出一个点，走到这个点的时间必须是最少的。我看很多人用普通的队列就过了，感觉有点不科学。

我本来以为BFS和DFS的时间都差不多，用哪个随自己的喜好。这题把我的观点刷新了一下。。

代码里的障碍物那句，我把普通的坐标轴转换成了行和列的坐标轴，因为其他的我会想乱掉。。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546

| ```c++
int mp[MAXN][MAXN], vis[MAXN][MAXN], ans = 0;const int O = 1000; struct POINT{    int x, y, time;    bool operator < (const POINT &a) const    {        return time > a.time;    }};priority_queue<POINT> Q; class TheGridDivTwo {public:    void BFS(int k)    {        Q.push((POINT){O, O, 0});        while (!Q.empty())        {            POINT tmp = Q.top(); Q.pop();            if (k - tmp.time + tmp.y - O <= ans) continue;            for (int i = 0; i < 4; i++)            {                int x = tmp.x, y = tmp.y;                int xx = x + dir[i][0], yy = dir[i][1] + y;                if (!vis[xx][yy] && !mp[xx][yy] && xx >= 0 && yy >= 0 && xx <= 2000 && yy <= 2000)                {                    vis[xx][yy] = 1;                    if (tmp.time + 1 <= k)                    {                        ans = max(ans, yy - O);                        Q.push((POINT){xx, yy, tmp.time + 1});                    }                }            }        }    }     int find(vector<int> x, vector<int> y, int k) {        for (int i = 0; i < SZ(x); i++)            mp[-y[i] + O][x[i] + O] = 1;        BFS(k);        return ans;    }};
```
---
categories: Posts
date: 2014-09-01 00:00:00
title: UVa 1468 - Restaurant
tags: []
layout: post
---

## 传送门

[UVa 1468 - Restaurant](http://www.bnuoj.com/v3/problem_show.php?pid=37085)

## 题意

有A、B两个餐馆和其他餐馆，现在要建一个餐馆，使它到A或B的距离比任意一个餐馆到A或B的距离有一个短。求数目。

## 思路

一开始用暴力枚举，就算加了很多剪枝也TLE了TAT。

还是参考的帆神和柯神的解题报告。

要从每一列考虑。

显然在A、B两个餐馆X轴之外是不可能放置的，因为这样距离一定会比A到B或者B到A长。  
所以放置地点就限制在了AB之间（X axis）

接下来考虑每一列，显然不能放在这一列离x axis 最近的餐馆的上面，因为这样一放那个最近的餐馆就两项都比他短了（X相等，Y又比他大）。

所以边读取输入边维护h[x]的最小值。

但是还有别的限制条件。

对于一个餐馆P，后一列的点K的位置必须不能同时x + 1， y + 1，也就是划上去一个格的对角线，也就是多一个高度。如果超过了这个高度，显然K到A的距离必定大于P到A的距离。(详情请参考帆神的图)

到B也一样。

所以要从前往后从后往前各扫描一遍h[x]，维护min(h[x], h[x - 1]（h[x + 1]） + 1)

满足了以上条件的点都可以建餐厅啦~之后就是统计了。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960

| ```c++
#include<bits/stdc++.h>#define LL long long#define lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)const int MAXN = 60000 + 5;const int INF = 0x3f3f3f3f;using namespace std; typedef pair<int, int> pii;typedef vector<int> vei;typedef vector<pair<int, int> >veii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii;typedef priority_queue<pii, vector<pii>, greater<pii> >pquii; struct POINT{    int x, y;}; int h[MAXN]; int main(){    //freopen("input.txt", "r", stdin);    int T, i, j, n, len;    POINT a, b;    scanf("%d", &T);    while (T--)    {        int st = INF, ed = -1;        scanf("%d%d", &len, &n);        scanf("%d%d%d%d", &a.x, &a.y, &b.x, &b.y);        st = min(a.x, b.x), ed = max(a.x, b.x);        fill(h + st + 1, h + ed, len);        for (i = 3; i <= n; i++)        {            int x, y;            scanf("%d%d", &x, &y);            h[x] = min(h[x], abs(y - a.y));        }        h[st] = 0, h[ed] = 0;        for (i = st + 1; i < ed; i++)            h[i] = min(h[i], h[i - 1] + 1);        for (i = ed - 1; i > st; i--)            h[i] = min(h[i], h[i + 1] + 1);        LL ans = 0;        for (i = st + 1; i < ed; i++)        {            if (h[i])            {                ans++;                ans += min(a.y, h[i] - 1);                ans += min(len - a.y, h[i] - 1);            }        }        cout << ans << endl;    }    return 0;}
```
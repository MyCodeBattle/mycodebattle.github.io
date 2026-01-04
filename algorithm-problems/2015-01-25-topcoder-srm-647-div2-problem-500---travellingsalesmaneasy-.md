---
categories: Posts
date: 2015-01-25 00:00:00
title: TopCoder SRM 647 Div2 Problem 500 - TravellingSalesmanEasy (思维)
tags: []
layout: post
---

## 题意

有一个商人要卖东西。

他手头有M个商品，每个商品只能在特定的城市卖特定的价钱。

他有一个行程，每次去一个城市的时候只能卖一种商品。

问最大的利润。

## 思路

先按城市归个类，然后从大到小排序一下。

每次访问哪个城市就加上那次的价钱。如果卖完了就不加了。

## 代码


```c++
class TravellingSalesmanEasy {
    public:
    int getMaxProfit(int M, vector<int> profit, vector<int> city, vector<int> visit) {
        int vis[MAXN];
        MS(vis, 0);
        vector<int> res[MAXN];
        for (int i = 0; i < SZ(city); i++)
            res[city[i]].PB(profit[i]);
        for (int i = 1; i <= M; i++) sort(res[i].begin(), res[i].end(), greater<int>());
        int ans = 0;
        for (int i = 0; i < SZ(visit); i++)
        {
            int &ith = vis[visit[i]];
            if (ith+1 > SZ(res[visit[i]])) continue;
            ans += res[visit[i]][ith];
            ith++;
        }
        return ans;
    }
};
```
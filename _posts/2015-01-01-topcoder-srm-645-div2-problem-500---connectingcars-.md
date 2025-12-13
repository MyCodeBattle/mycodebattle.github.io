---
categories: Posts
date: 2015-01-01 00:00:00
title: TopCoder SRM 645 Div2 Problem 500 - ConnectingCars (枚举)
tags: []
layout: post
---

## 题意

要把汽车移在一起，求最小移动距离。

## 思路

昨天晚上想的时候是想如果是双数的时候就移到中间位置，如果是单数就中间的车不动，其他向它靠。

可是最后计算车的距离的时候整个人就逗了，竟然用统一移动一个距离然后加上两车之间的间距来算。我还纳闷怎么算出来比答案还少

因为数据量少，所以就可以无脑暴力了，直接算出第i辆车不动的时候的最小距离，然后取最小值。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839

| ```c++
struct CAR{	LL st, ed;	bool operator < (const CAR &a) const	{		return st < a.st;	}}car[MAXN]; class ConnectingCars {    public:    long long minimizeCost(vector<int> pos, vector<int> len) {        int i, j, num = pos.size();        for (i = 0; i < pos.size(); i++)        {            car[i].st = pos[i];            car[i].ed = pos[i] + len[i];        }        sort(car, car + num);        LL ans = (1ll<<60);        for (i = 0; i < num; i++)        {            LL curAns = 0, add = 0;            for (j = i - 1; j >= 0; j--)            {                add += car[j + 1].st - car[j].ed;                curAns += add;            }            add = 0;            for (j = i + 1; j < num; j++)            {                add += car[j].st - car[j - 1].ed;                curAns += add;            }            ans = min(ans, curAns);        }        return ans;    }};
```
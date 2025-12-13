---
categories: Posts
date: 2015-03-01 00:00:00
title: TopCoder SRM 652 Div2 Problem 1000 - NoRightTurnDiv2 (几何 + 贪心)
tags: []
layout: post
---

#  [TopCoder SRM 652 Div2 Problem 1000 - NoRightTurnDiv2 (几何 + 贪心)](/2015/03/topcoder-652-div2-1000/ "TopCoder SRM 652 Div2 Problem 1000 - NoRightTurnDiv2 \(几何 + 贪心\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Mar 10 2015 16:31

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

只能走出一个逆时针的三角形，并且路线不能交叉。求路线。

## 思路

感觉挺神奇的一题。

主要的思想就是以边角点作为起点，找到「最外面」的那个点，然后继续以那个点作为起点。  
「最外面」只是我的感觉，不知道怎么描述。

找「最外面」的点过程感觉挺奇妙。先选一个点作为next点，然后判断他和下一个点tmp能否组成一个顺时针的三角形。如果能的话，tmp就是目前的最优答案。然后把tmp作为next，继续。

至于为什么这么走不会出现交叉，我YY了一下。  
如果出现交叉，那个交叉的点就可以作为先前的最优点被选中。所以这种情况不会出现。

## 代码
    
    
    1234567891011121314151617181920212223

| 
    
    
    class NoRightTurnDiv2 {    public:    vector<int> findPath(vector<int> x, vector<int> y) {        MS(vis, 0);        int n = SZ(x), cur = 0;        vector<int> res;        cur = min_element(x.begin(), x.end()) - x.begin();        for (int k = 0; k < n; k++)        {            res.PB(cur);            vis[cur] = 1;            int nxt = -1;            for (int i = 0; i < n; i++)            {                if (vis[i]) continue;                if (nxt == -1) nxt = i;                else if ((x[nxt]-x[cur]) * (y[i]-y[cur]) - (x[i]-x[cur]) * (y[nxt]-y[cur]) < 0) nxt = i;            }            cur = nxt;        }        return res;    }};  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - TopCoder](/tags/Online-Judge-TopCoder/)[Foundation - Greedy](/tags/Foundation-Greedy/)

---
categories: Posts
date: 2015-01-01 00:00:00
title: Codeforces 508C - Anya and Ghosts (模拟 + 贪心)
tags: []
layout: post
---

#  [Codeforces 508C - Anya and Ghosts (模拟 + 贪心)](/2015/01/codeforces-508c/ "Codeforces 508C - Anya and Ghosts \(模拟 + 贪心\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jan 28 2015 9:49

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

Anya因为很喜欢看鬼片，所以鬼要来她家做客。

每个鬼到来的时候必须要有k根蜡烛亮着。

Anya点亮一根蜡烛要一秒，每根蜡烛持续m秒

问她最少要几根蜡烛

## 思路

首先判断能不能成功。

显然当蜡烛的持续时间last小于最少要点亮的蜡烛数least时，不能成功。

然后就是模拟了。

我们不能浪费蜡烛，所以要从鬼来的前一秒开始点。

用队列表示现在点亮的蜡烛数。如果鬼来的时候蜡烛不够了，就push。

（为啥我看到蜡烛就想到了皮鞭。。）

## 代码
    
    
    12345678910111213141516171819202122232425262728293031

| 
    
    
    priority_queue<int, vector<int>, greater<int> >Q; int main(){    //ROP;    int n, last, least;    scanf("%d%d%d", &n, &last, &least);    if (last < least)    {        puts("-1");        return 0;    }    int fir, ans = 0;    for (int i = 0; i < n; i++)    {        int tme;        scanf("%d", &tme);        while (!Q.empty() && Q.top() < tme) Q.pop();        if (SZ(Q) < least)        {            int tmp = SZ(Q);            for (int j = tme - 1, cnt = 0; cnt < least - tmp; cnt++, j--)            {                Q.push(j + last);                ans++;            }        }    }    printf("%d\n", ans);    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - Codeforces](/tags/Online-Judge-Codeforces/)[Foundation - Simulate](/tags/Foundation-Simulate/)

---
categories: Posts
date: 2014-09-01 00:00:00
title: UVa 1418 - WonderTeam
tags: []
layout: post
---

#  [UVa 1418 - WonderTeam](/2014/09/UVa-1418/ "UVa 1418 - WonderTeam")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 14 2014 23:14

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 1418 - WonderTeam](http://www.bnuoj.com/v3/problem_show.php?pid=37035)

## 题意

有N个队比赛，每个队之间比两次，胜者3分，平一分，失败没分。如果一个队最多胜，最多赢球，最少输球就是梦之队，求最低排名。

## 思路

借鉴了他人的思路。

要求最低排名，就是要赢得越少越好，输得越多越好。

所以假设梦之队赢了两场，其他的队都赢一场，都赢在梦之队上。

队伍 | 胜场 | 负 | 平  
---|---|---|---  
梦之队 | 2 | n - 1 | n - 3  
两个队 | 1 | 1 | 2n - 4  
其他队 | 1 | 0 | 2n - 3  
  
梦之队总得分 n + 3

两个队（如果队伍总数>=3）得分2n

其他队 2n - 1。

然后就可以算出排名了。

## 代码
    
    
    1234567891011121314151617181920212223242526

| 
    
    
    #include<bits/stdc++.h>#define LL long long#define lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)const int MAXN = 1000 + 5;const int INF = 0x3f3f3f3f;using namespace std; typedef pair<int, int> pii;typedef vector<int> vei;typedef vector<pair<int, int> >veii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii;typedef priority_queue<pii, vector<pii>, greater<pii> >pquii; int main(){    int n, i, j;    while (scanf("%d", &n), n)    {        if (n <= 3) printf("1\n");        else if (n <= 4) printf("2\n");        else printf("%d\n", n);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Foundation - Greedy](/tags/Foundation-Greedy/)

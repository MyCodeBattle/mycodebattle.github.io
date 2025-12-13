---
categories: Posts
date: 2014-09-01 00:00:00
title: ZJU 3811 - Untrusted Patrol
tags: []
layout: post
---

#  [ZJU 3811 - Untrusted Patrol](/2014/09/ZOJ-3811/ "ZJU 3811 - Untrusted Patrol")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 8 2014 16:43

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

有N个仓库，K个传感器，给出传感器的提示顺序，问能不能遍历图

## 思路

从第一个传感器的提示地方开始遍历，直到碰到装传感器的地方，然后看第二个地方有没有被访问到。  
如果没有被访问到，说明第一个传感器和第二个传感器是不连通的，false。  
如果有，遍历第二个传感器，依次。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869

| 
    
    
    #include <cstdio>#include <cstring>#include <vector>#define LL long long#define lowbit(x) ((x) & (-x))const int MAXN = 1e5 + 5;const int INF = 0x3f3f3f3f;using namespace std; vector<int> mp[MAXN];int Next[MAXN], vis[MAXN], cenvis[MAXN]; void DFS(int cur){    for (vector<int>::iterator it = mp[cur].begin(); it != mp[cur].end(); it++)    {        if (vis[*it]) continue;        vis[*it] = 1;        if (!cenvis[*it]) DFS(*it);    }} int main(){    //freopen("input.txt", "r", stdin);    int T, i, j, nroom, nway, nloc, nnext;    scanf("%d", &T);    while (T--)    {        memset(vis, 0, sizeof vis);        memset(cenvis, 0, sizeof cenvis);        scanf("%d%d%d", &nroom, &nway, &nloc);        for (i = 0; i < nloc; i++)        {            int a;            scanf("%d", &a);            cenvis[a] = 1;        }        for (i = 0; i < nway; i++)        {            int a, b;            scanf("%d%d", &a, &b);            mp[a].push_back(b);            mp[b].push_back(a);        }        scanf("%d", &nnext);        bool flag = false;        if (nnext < nloc)            flag = true;        for (i = 0; i < nnext; i++)            scanf("%d", &Next[i]);        vis[Next[0]] = 1;        for (i = 0; i < nnext; i++)        {            if (!vis[Next[i]])            {                flag = true;                break;            }            DFS(Next[i]);        }        for (i = 1; i <= nroom; i++)            if (!vis[i]) flag = true;        printf("%s\n", flag == false ? "Yes" : "No");        for (i = 0; i <= nroom; i++)            mp[i].clear();    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Foundation - Search](/tags/Foundation-Search/)[Online Judge - ZJU](/tags/Online-Judge-ZJU/)

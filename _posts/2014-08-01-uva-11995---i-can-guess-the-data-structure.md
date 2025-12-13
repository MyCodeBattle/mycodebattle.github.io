---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 11995 - I Can Guess the Data Structure!
tags: []
layout: post
---

## 传送门

[UVa 11995 - I Can Guess the Data Structure!](http://vjudge.net/vjudge/problem/viewProblem.action?id=18700)

## 题意

给两个操作，一进一出（XD），判断是属于哪种数据结构。

## 思路

模拟。有STL真是太方便了。。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879808182838485868788899091

| ```c++
#include <bits/stdc++.h>using namespace std;#define LL long long#define MP(a, b) make_pair(a, b)const int MAXN = 1000 + 10;const int INF = 0x3f3f3f3f; queue<int> qu;priority_queue<int> pqu;stack<int> stk; struct COM{    int a, num;}cmd[MAXN]; int vis[4]; void Init(){    while (!qu.empty())        qu.pop();    while (!pqu.empty())        pqu.pop();    while (!stk.empty())        stk.pop();} int main(){    //freopen("input.txt", "r", stdin);    int n, i, j;    while (~scanf("%d", &n))    {        int ans = 0;        memset(vis, 0, sizeof vis);        Init();        for (i = 0; i < n; i++)            scanf("%d%d", &cmd[i].a, &cmd[i].num);        for (i = 0; i < n; i++)        {            if (cmd[i].a == 1)                qu.push(cmd[i].num);            else if (cmd[i].a == 2)                if (qu.empty() || qu.front() != cmd[i].num)                    break;                else                    qu.pop();        }        if (i == n)            vis[1] = 1, ans++;        for (i = 0; i < n; i++)        {            if (cmd[i].a == 1)                stk.push(cmd[i].num);            else if (cmd[i].a == 2)                if (stk.empty() || stk.top() != cmd[i].num)                    break;                else                    stk.pop();        }        if (i == n)            vis[2] = 1, ans++;        for (i = 0; i < n; i++)        {            if (cmd[i].a == 1)                pqu.push(cmd[i].num);            else if (cmd[i].a == 2)                if (pqu.empty() || pqu.top() != cmd[i].num)                    break;                else                    pqu.pop();        }        if (i == n)            vis[3] = 1, ans++;        if (ans == 0)            printf("impossible\n");        else if (ans > 1)            printf("not sure\n");        else        {            if (vis[1])                printf("queue\n");            else if (vis[2])                printf("stack\n");            else                printf("priority queue\n");        }    }    return 0;}
```
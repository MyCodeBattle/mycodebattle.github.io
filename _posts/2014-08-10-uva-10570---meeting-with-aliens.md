---
categories: Posts
date: 2014-08-10 00:00:00
title: UVa 10570 - Meeting with Aliens
tags: []
layout: post
---

## 传送门

[UVa 10570 - Meeting with Aliens](http://vjudge.net/problem/viewProblem.action?id=23446)

## 题意

n个外星人开会，一开始他们是乱坐的，现在要求把它们排有序，问最小交换次数。

## 思路

参考了别人的结论。

引用自**Wiking**

> 求最少交换次数，使得1~n排列有序。找出环的数目，答案就是n-环数。eg （13254）可分为（1）、（23）、（54）三个环。

查了一下，发现有个叫Cycle Sort的排序，应该和这个结论有关系。等下看看。

因为每个数都可能是起点，所以要扩展一下原来的数组，使之可以连起来，然后枚举每个起点。

因为可以顺时针数也可以逆时针数，所以要翻转一下原来的数组，用reverse这个STL函数。

忽然想起开学初C++老师布置的一个小作业，就是翻转一个数组。那时候要是知道这个函数。。。。。

## 代码


```c++
#include <bits/stdc++.h>
using namespace std;
#define LL long long
#pragma comment(linker, "/STACK:102400000,102400000")
const int MAXN = 500 + 10;
const int INF = 0x3f3f3f3f;
 
int num[MAXN * 2], n, vis[MAXN];
 
int GetV(int *pnum)
{
    memset(vis, 0, sizeof vis);
    int cnt = 0;
    for (int i = 1; i <= n; i++)
        if (!vis[i])
        {
            cnt++;
            for (int j = i; !vis[j]; j = pnum[j])
                vis[j] = 1;
        }
    return n - cnt;
}
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int i, j;
    while (scanf("%d", &n), n)
    {
        for (i = 1; i <= n; i++)
            scanf("%d", #[i]);
        int ans = INF;
        for (i = 0; i < 2; i++)
        {
            for (j = 1; j <= n; j++)
                num[j + n] = num[j];
            for (j = 1; j <= n; j++)
                ans = min(ans, GetV(num + j));
            reverse(num + 1, num + n + 1);
        }
        printf("%d\n", ans);
    }
    return 0;
}
```
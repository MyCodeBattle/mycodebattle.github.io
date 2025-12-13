---
categories: Posts
date: 2014-09-01 00:00:00
title: UVa 1335 - Beijing Guards
tags: []
layout: post
---

## 传送门

[UVa 1335 - Beijing Guards](http://vjudge.net/problem/viewProblem.action?id=36138)

## 题意

N个人围成一圈，相邻两个人不能有相同的礼物，求最少的礼物数

## 思路

大白上的例题，非常神奇的思路。

第一个人选1~n1的礼物，这部分当成左边，剩下的当成右边。然后以后奇数的人靠右边选，偶数的人靠左边选，这样可以保证最后一个奇数的人右边部分选的是最多的。  
最后判断最后一个人的左边部分是不是0.

如果是偶数，偶数人选1~ni，奇数人选从后选他需要的就行。

一开始我在二分的时候习惯地把left = 0了，WA了好几发。原来Check的时候没有检查礼物数是否合理。因为LRJ是直接把相邻之间的最大和当成left的。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768

| ```c++
#include <cstdio>#include <algorithm>#define LL long long#define lowbit(x) ((x) & (-x))const int MAXN = 1e5 + 5;const int INF = 0x3f3f3f3f;using namespace std; int num[MAXN], l[MAXN], r[MAXN], n; bool Check(int mid){    int x = num[1], y = mid - num[1];    l[1] = x, r[1] = 0;    for (int i = 2; i <= n; i++)    {        if (i & 1)        {            r[i] = min(num[i], y - r[i - 1]);            l[i] = num[i] - r[i];        }        else        {            l[i] = min(num[i], x - l[i - 1]);            r[i] = num[i] - l[i];        }    }    return l[n] == 0 ? true : false;} int main(){    //freopen("input.txt", "r", stdin);    int i, j;    while (scanf("%d", &n), n)    {        int nmax = -1, ans;        for (i = 1; i <= n; i++)            scanf("%d", #[i]);        for (i = 2; i <= n; i++)            nmax = max(nmax, num[i] + num[i - 1]);        nmax = max(nmax, num[1] + num[n]);        if (n == 1)        {            printf("%d\n", num[1]);            continue;        }        if (n & 1)        {            int left = nmax, right = MAXN * 3, mid;            while (left < right)            {                mid = left + ((right - left) >> 1);                if (Check(mid))                {                    ans = mid;                    right = mid;                }                else                    left = mid + 1;            }            printf("%d\n", ans);        }        else            printf("%d\n", nmax);    }    return 0;}
```
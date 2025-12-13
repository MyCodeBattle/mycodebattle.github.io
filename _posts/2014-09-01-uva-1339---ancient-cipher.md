---
categories: Posts
date: 2014-09-01 00:00:00
title: UVa 1339 - Ancient Cipher
tags: []
layout: post
---

## 传送门

[UVa 1339 - Ancient Cipher](http://vjudge.net/problem/viewProblem.action?id=36142)

## 题意

给出两个字符串，问上面能不能经过映射成为下面的字符串，下面的顺序是打乱的。

## 思路

看它们各个字母的出现个数是不是一样的，如果全一样就可以映射。

## 代码


```c++
#include <bits/stdc++.h>
#define LL long long
#define lowbit(x) ((x) & (-x))
const int MAXN = 26 + 5;
const int INF = 0x3f3f3f3f;
using namespace std;
 
int ori[MAXN], fn[MAXN];
vector<int> oAns, fAns;
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int i, j, n;
    char str[110];
    while (gets(str))
    {
        oAns.clear();
        fAns.clear();
        memset(ori, 0, sizeof ori);
        memset(fn, 0, sizeof fn);
        for (i = 0; str[i]; i++)
            ori[str[i] - 'A']++;
        gets(str);
        for (i = 0; str[i]; i++)
            fn[str[i] - 'A']++;
        for (i = 0; i < 27; i++)
        {
            if (ori[i]) oAns.push_back(ori[i]);
            if (fn[i]) fAns.push_back(fn[i]);
        }
        sort(oAns.begin(), oAns.end());
        sort(fAns.begin(), fAns.end());
        if (oAns.size() != fAns.size())
        {
            printf("NO\n");
            continue;
        }
        for (i = 0; i < oAns.size(); i++)
        {
            if (oAns[i] != fAns[i])
                break;
        }
        printf("%s\n", i == oAns.size() ? "YES" : "NO");
    }
    return 0;
}
```
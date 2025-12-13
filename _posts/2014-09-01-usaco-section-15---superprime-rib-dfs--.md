---
categories: Posts
date: 2014-09-01 00:00:00
title: USACO Section 1.5 - Superprime Rib (DFS + 枚举)
tags: []
layout: post
---

## 题意

找出n位，每次去掉最后一位都是素数的数字。

## 思路

首先有几个特殊的数字。

  1. 1 9不能作为第一位。

  2. 2只能作为第一位。


其余的数字都不行。

然后DFS即可。

一开始我是先枚举出数字再判断，T了。应该边枚举边判断

## 代码


```c++
/*
ID: mycodeb1
LANG: C++
TASK: sprime
*/
 
#include <cstdio>
#include <stack>
#include <set>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <functional>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <ctime>
#include <cstdlib>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <cmath>
#define LL long long
#define lowbit(x) ((x) & (-x))
#define MP(a, b) make_pair(a, b)
#define MS(arr, num) memset(arr, num, sizeof(arr))
#define PB push_back
#define F first
#define S second
#define ROP freopen("input.txt", "r", stdin);
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
using namespace std;
const int MAXN = 1000 + 5;
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
const int num[] = {1, 2, 3, 5, 7, 9};
int str[10], n;
 
bool Check(int nm)
{
    for (int i = 2; i <= (int)sqrt(nm + 0.5); i++)
        if (nm % i == 0) return false;
    return true;
}
 
void DFS(int curLen)
{
    int i, j;
    if (curLen == n)
    {
        int nm = 0;
        for (i = 0; i < n; i++) nm = nm * 10 + str[i];
        if (Check(nm)) printf("%d\n", nm);
        return;
    }
    for (i = 0; i < 6; i++)
    {
        if (curLen == 0)
            if (i == 0 || i == 5) continue;
        if (curLen != 0 && i == 1) continue;
        str[curLen] = num[i];
        int nm = 0;
        for (j = 0; j <= curLen; j++) nm = nm * 10 + str[j];
        if (!Check(nm)) continue;
        DFS(curLen + 1);
    }
}
 
int main()
{
    //ROP;
    freopen("sprime.out", "w", stdout);
    freopen("sprime.in", "r", stdin);
 
    MS(str, 0);
    int i, j;
    scanf("%d", &n);
    DFS(0);
    return 0;
}
```
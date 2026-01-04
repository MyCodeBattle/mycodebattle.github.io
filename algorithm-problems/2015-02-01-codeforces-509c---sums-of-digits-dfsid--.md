---
categories: Posts
date: 2015-02-01 00:00:00
title: Codeforces 509C - Sums of Digits (DFSID + 贪心)
tags: []
layout: post
---

## 题意

给出一个数字k，代表某个数的数字和。

现在给出n个k，输出递增的数字，且最后一个数字要求尽量小。

## 思路

看到是填数字的就想到迭代加深搜索了。搞了好久。

分了一些情况。

第一个数字单独处理。

之后的如果已经填上的数字比之前的大，后面可以填相等的。不然不能。  
再加上一些乱七八糟的剪枝。。

看了vfk总共二三十行的代码以后我都不好意思把自己的往外贴了。

## 代码


```c++
#include <stack>
#include <cstdio>
#include <list>
#include <set>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <functional>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <string>
#include <map>
#include <cmath>
using namespace std;
#define LL long long
#define ULL unsigned long long
#define SZ(x) (int)x.size()
#define Lowbit(x) ((x) & (-x))
#define MP(a, b) make_pair(a, b)
#define MS(arr, num) memset(arr, num, sizeof(arr))
#define PB push_back
#define X first
#define Y second
#define ROP freopen("input.txt", "r", stdin);
#define MID(a, b) (a + ((b - a) >> 1))
#define LC rt << 1, l, mid
#define RC rt << 1|1, mid + 1, r
#define LRT rt << 1
#define RRT rt << 1|1
#define BitCount(x) __builtin_popcount(x)
#define BitCountll(x) __builtin_popcountll(x)
#define LeftPos(x) 32 - __builtin_clz(x) - 1
#define LeftPosll(x) 64 - __builtin_clzll(x) - 1
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
const double eps = 1e-8;
const int MAXN = 500 + 10;
const int MOD = 29;
const int dir[][2] = { {1, 0}, {0, 1} };
int cases = 0;
typedef pair<int, int> pii;
 
int num[MAXN], tmp, curNum[MAXN], preDep, dep;
 
bool Check(int curDep)
{
    if (curDep > preDep) return true;
    if (curDep < preDep) puts("wocao");
    for (int i = 0; i < curDep; i++)
    {
        if (curNum[i] > num[i]) return true;
        if (curNum[i] <= num[i] && i == curDep-1) return false;
        if (curNum[i] < num[i]) return false;
    }
    return true;
}
 
bool DFSID(int curDep, int sum, bool flag)
{
    if (sum > tmp) return false;
    if (sum + (dep - curDep)*9 < tmp) return false;
    if (curDep == dep)
    {
        if (sum != tmp) return false;
        if (Check(curDep))
        {
            for (int i = 0; i < curDep; i++) printf("%d", curNum[i]);
            puts("");
            memcpy(num, curNum, sizeof curNum);
            preDep = curDep;
            return true;
        }
        return false;
    }
    if (dep == preDep)
    {
        for (int i = 0; i <= 9; i++)
        {
            if (i == 0 && curDep == 0) continue;
            if (!flag && i < num[curDep]) continue;
            curNum[curDep] = i;
            if (!flag)
            {
                if (i > num[curDep]) flag = true;
            }
            if (DFSID(curDep + 1, sum + i, flag)) return true;
 
        }
    }
    else
    {
        for (int i = 0; i <= 9; i++)
        {
            if (i == 0 && curDep == 0) continue;
            curNum[curDep] = i;
            if (DFSID(curDep + 1, sum + i, flag)) return true;
        }
    }
    return false;
}
 
void FirstHandle()
{
    int cur = tmp;
    int pos = 0;
    while (cur)
    {
        if (cur > 9) num[pos++] = 9, cur -= 9;
        else num[pos++] = cur, cur = 0;
    }
    reverse(num, num + pos);
    dep = preDep = pos;
    for (int i = 0; i < pos; i++) printf("%d", num[i]);
    puts("");
}
 
int main()
{
    //ROP;
    int n;
    scanf("%d", &n);
    dep = 1;
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &tmp);
        if (!i)
        {
            FirstHandle();
            continue;
        }
        while (!DFSID(0, 0, false))
        {
            dep++;
            while ((9*dep) < tmp) dep++;
        }
    }
    return 0;
}
```
---
categories: Posts
date: 2015-02-21 00:00:00
title: HDU 3816 - To Be NUMBER ONE (数学)
tags: []
layout: post
---

## 题意

输出符合要求的数。

## 思路

一个数可以这么拆。

$$\frac{1}{n} = \frac{1}{n+1} + \frac{1}{n(n+1)}$$

剩下来就好办了，一直分解数即可。

## 代码


```c++
​#include <stack>
#include <cstdio>
#include <list>
#include <cassert>
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
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
const double eps = 1e-8;
const int MAXN = 3e3 + 10;
const int MOD = 1e9 + 7;
const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };
int cases = 0;
typedef pair<int, int> pii;
  
int vis[MAXN];
  
int main()
{
    set<int> ans;
    ans.insert(2);
    vis[2] = 1;
    while (SZ(ans) != 18)
    {
        set<int>::iterator it = ans.begin();
        for (; it != ans.end(); it++)
        {
            int cur = *it;
            if (vis[*it])
                if (!vis[cur+1] && !vis[cur*(cur+1)]) break;
        }
        int cur = *it;
        if (SZ(ans) != 1)
        {
            ans.erase(*it);
            vis[*it] = 0;
        }
        ans.insert(cur+1); vis[cur+1] = 1;
        ans.insert(cur*(cur+1));  vis[cur*(cur+1)] = 1;
        for (it = ans.begin(); it != ans.end(); it++)
            if (it == ans.begin()) printf("%d", *it);
            else printf(" %d", *it);
        puts("");
    }
    return 0;
}
```
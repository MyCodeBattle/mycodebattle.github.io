---
categories: Posts
date: 2014-09-01 00:00:00
title: UVa 11039 - Building designing
tags: []
layout: post
---

## 传送门

[UVa 11039 - Building designing](http://www.bnuoj.com/v3/problem_show.php?pid=19457)

## 题意

有绝对值不一样的数字，现在把它们从小到大拍起来，相邻的正负必须不同，求最长长度。

## 思路

贪心。把数组排序一下，第一个必选。然后以后就能选就选。我是用set来判断是否为负数。是就跳过。

## 代码


```c++
#include <bits/stdc++.h>
#define LL long long
#define lowbit(x) ((x) & (-x))
const int MAXN = 5e5 + 5;
const int INF = 0x3f3f3f3f;
using namespace std;
 
set<int> mp;
int num[MAXN];
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int T, i, j, n, a;
    scanf("%d", &T);
    while (T--)
    {
        mp.clear();
        scanf("%d", &n);
        for (i = 0; i < n; i++)
        {
            scanf("%d", &a);
            if (a < 0)
            {
                mp.insert(-a);
                num[i] = -a;
            }
            else
                num[i] = a;
        }
        sort(num, num + n);
        int cnt = 1, last;
        last = mp.count(num[0]) ? -1 : 1;
        for (i = 1; i < n; i++)
        {
            if (last == 1)
            {
                if (mp.count(num[i]))
                    last = -1, cnt++;
            }
            else
                if (!mp.count(num[i]))
                    last = 1, cnt++;
        }
        printf("%d\n", cnt);
    }
    return 0;
}
```
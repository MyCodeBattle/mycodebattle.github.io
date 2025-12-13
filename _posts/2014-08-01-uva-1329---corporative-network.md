---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 1329 - Corporative Network
tags: []
layout: post
---

## 传送门

[UVa 1329 - Corporative Network](http://www.bnuoj.com/v3/problem_show.php?pid=36946)

## 题意

有两种命令，一种是把a合并到b的分支里，一种是询问a到根节点的距离。

## 思路

找到父节点，然后距离就是本身的距离加上父节点的距离，之后路径压缩

## 代码


```c++
#include <bits/stdc++.h>
#define LL long long
using namespace std;
const int MAXN = 2e4 + 5;
const int INF = 0x3f3f3f3f;
 
int dis[MAXN], p[MAXN];
 
int Find(int x)
{
    if (p[x] == x)
        return x;
    int root = Find(p[x]);
    dis[x] += dis[p[x]];
    return p[x] = root;
}
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int T, i, j, n, a, b;
    char ch[10];
    scanf("%d", &T);
    while (T--)
    {
        scanf("%d%*c", &n);
        for (i = 1; i <= n; i++)
        {
            p[i] = i;
            dis[i] = 0;
        }
        while (scanf("%s", ch) && ch[0] != 'O')
        {
            if (ch[0] == 'E')
            {
                scanf("%d", &a);
                Find(a);
                printf("%d\n", dis[a]);
            }
            else
            {
                scanf("%d%d", &a, &b);
                p[a] = b;
                dis[a] = abs(a - b) % 1000;
            }
        }
    }
    return 0;
}
```
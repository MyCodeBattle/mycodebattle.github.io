---
categories: Posts
date: 2014-07-09 00:00:00
title: UVa 10651 - Pebble Solitaire
tags: []
layout: post
---

## 传送门

[UVa 10651 - Pebble Solitaire](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1592)

## 题意

一行有十二个格子，每个格子上可能有棋子。按照规定的操作，问最后能剩下最少多少个？

## 思路

直接暴力过了，扫描每一种状态，如果可以跳生成新的状态继续DFS，返回的是跳过的棋子数，也就是消去的棋子数。然后用一开始的棋子数一减就可以了。不过感觉数据有点水，不然这样应该会TLE，感觉用哈希来保存每一种状态，然后记忆化搜索。

## 代码


```c++
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int MAXN = 12 + 1;
 
char chess[MAXN];
 
int ifJump(int i, int j, int k, const char *t)
{
    if (t[i] == '-' && t[j] == 'o' && t[k] == 'o')  //往左跳，类型1
        return 1;
    else if (t[i] == 'o' && t[j] == 'o' && t[k] == '-')
        return 2;
    return 0;
}
 
int DFS(char *t)
{
    int ans = 0, i, j;
    for (i = 1; i < 11; i++)
    {
        char temp[20];
        strcpy(temp, t);
        if (ifJump(i - 1, i, i + 1, t) == 1)
        {
            temp[i - 1] = 'o', temp[i] = '-', temp[i + 1] = '-';
            ans = max(ans, DFS(temp) + 1);
        }
        else if (ifJump(i - 1, i, i + 1, t) == 2)
        {
            temp[i - 1] = '-', temp[i] = '-', temp[i + 1] = 'o';
            ans = max(ans, DFS(temp) + 1);
        }
    }
    return ans;
}
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int T, i, j, cnt, ans;
    scanf("%d%*c", &T);
    while (T--)
    {
        cnt = 0;
        gets(chess);
        for (i = 0; i < 12; i++)
            if (chess[i] == 'o')
                cnt++;
        printf("%d\n", cnt - DFS(chess));
    }
    return 0;
}
```
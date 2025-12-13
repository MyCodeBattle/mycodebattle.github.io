---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 348 - Optimal Array Multiplication Sequence
tags: []
layout: post
---

## 传送门

[UVa 348 - Optimal Array Multiplication Sequence](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=114&page=show_problem&problem=284)

## 题意

给出N个矩阵，求它们的最小相乘次数。（差不多就是这个意思

## 思路

要使总的相乘次数最小，就是让它的每一个子区间相乘次数最小，然后就变成区间DP了。  
这题和那个切木棒差不多，但是我还是写不出来。  
输出方式是用递归输出，没想到。  
参考了[rising_fallmoon的解题报告](http://blog.csdn.net/rising_fallmoon/article/details/10474381)

## 代码


```c++
#include <cstdio>
#include <cstring>
using namespace std;
const int MAXN = 10 + 1;
const int INF = 2147483647;

struct RECTAN
{
    int row, colomn;
}rectan[MAXN];

int dp[MAXN][MAXN], next[MAXN][MAXN];

int DFS(int st, int ed)
{
    int i;
    int &ans = dp[st][ed];
    if (st == ed)
        return ans = 0;
    if (ans != -1)
        return ans;
    int temp;
    ans = INF;
    for (i = st; i < ed; i++)
    {
        temp = DFS(st, i) + DFS(i + 1, ed) + rectan[st].row * rectan[i].colomn * rectan[ed].colomn;
        if (temp < ans)
        {
            ans = temp;
            next[st][ed] = i;
        }
    }
    return ans;
}

void PrintAns(int st, int ed)
{
    if (st > ed)
        return;
    if (st == ed)
    {
        printf("A%d", st + 1);
        return;
    }
    printf("(");
    PrintAns(st, next[st][ed]);
    printf(" x ");
    PrintAns(next[st][ed] + 1, ed);
    printf(")");
}

int main()
{
    //freopen("input.txt", "r", stdin);
    int n, a, b, i, j, cases = 1;
    while (scanf("%d", &n), n)
    {
        memset(dp, -1, sizeof(dp));
        for (i = 0; i < n; i++)
            scanf("%d%d", &rectan[i].row, &rectan[i].colomn);
        int ans = DFS(0, n - 1);
        //printf("%d\n", ans);
        printf("Case %d: ", cases++);
        PrintAns(0, n - 1);
        printf("\n");
    }
    return 0;
}
```
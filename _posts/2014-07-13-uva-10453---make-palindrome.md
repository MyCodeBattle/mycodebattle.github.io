---
categories: Posts
date: 2014-07-13 00:00:00
title: UVa 10453 - Make Palindrome
tags: []
layout: post
---

## 传送门

[UVa 10453 - Make Palindrome](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=114&page=show_problem&problem=1394)

## 题意

给一串字符串，要求输出把它变成回文串的最小操作数和那串回文串。

## 思路

上面某一题的升级版。  
引用一下[Primo_的精彩解释](http://blog.csdn.net/primoblog/article/details/9363801)

> 对于 $dp[i][j]$:  
> 如果$str[i] == str[j]$ 则$dp(i,j) = dp(i+1,j-1)$  
> 如果$str[i]!=str[j]$，则从$dp(i+1,j)$和$dp(i,j-1)$选出一个变化次数最少的一个状态，然后添加一个与$str[i]$或$str[j]$相同的字符,使得  
> $str[j]+dp(i,j-1)+str[j]$(或者)$str[i]+dp(i+1,j)+str[i]$构成回文串。

这样一来问题就很清晰了。

对于递归输出，可以根据$dp[i][j]$的大小关系进行输出。

如果$dp[i][j] == dp[i + 1][j] + 1$，说明$str[j]$的右边加了个$str[i]$，所以要先输出$str[i]$，递归后再次输出$str[i]$。反之亦然。

## 代码


```c++
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int MAXN = 1000 + 100;
const int INF = 0x3f3f3f3f;

char str[MAXN];
int dp[MAXN][MAXN];

void PrintAns(int x, int y)
{
    if (x > y)
        return;
    if (x == y)
    {
        printf("%c", str[x]);
        return;
    }
    if (str[x] == str[y])
    {
        printf("%c", str[x]);
        PrintAns(x + 1, y - 1);
        printf("%c", str[y]);
    }
    else if (dp[x][y] == dp[x + 1][y] + 1)
    {
        printf("%c", str[x]);
        PrintAns(x + 1, y);
        printf("%c", str[x]);
    }
    else
    {
        printf("%c", str[y]);
        PrintAns(x , y - 1);
        printf("%c", str[y]);
    }
    return;
}

int DFS(int x, int y)
{
    int &ans = dp[x][y];
    if (x >= y)
        return ans = 0;
    if (ans != INF)
        return ans;
    if (str[x] == str[y])
        ans = DFS(x + 1, y - 1);
    else
        ans = min(DFS(x + 1, y), DFS(x, y - 1)) + 1;
    return ans;
}

int main()
{
    //freopen("input.txt", "r", stdin);
    int i, j, k, n, len;
    while (gets(str))
    {
        len = strlen(str);
        for (i = 0; i <= len; i++)
            for (j = 0; j <= len; j++)
                dp[i][j] = INF;
        DFS(0, len - 1);
        printf("%d ", dp[0][len - 1]);
        PrintAns(0, len - 1);
        putchar(10);
    }
    return 0;
}
```
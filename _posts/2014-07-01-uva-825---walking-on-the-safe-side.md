---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 825 - Walking on the Safe Side
tags: []
layout: post
---

## 传送门

[UVa 825 - Walking on the Safe Side](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=114&problem=766&mosmsg=Submission+received+with+ID+13850675)

## 题意

要从左上角走到左下角，有些地方不能走，求走的路线的数量。

## 思路

一开始我竟然一直从DFS上去想。。。见识短的原因。  
因为只能往右走，或者往下走，这样就是两条路，所以状态转移方程很容易列出来。  
后来输入也坑了我一下。  
我**以为** 一个数字后面肯定是一个空格，然后就用scanf去读取了，WA了好几发以为自己DP错了。后来用读取字符来处理，习惯写成str[i] - ‘0’。。又WA了好几发。行数列数可以超过10的。。教训。。

## 代码


```c++
#include <cstdio>
#include <cstring>
#include <cctype>
using namespace std;
const int MAXN = 200;
 
int mp[MAXN][MAXN], row, col, dp[MAXN][MAXN];
 
int main()
{
    //freopen("in.txt", "r", stdin);
    int T, i, j, tempRow, temp;
    scanf("%d", &T);
    while (T--)
    {
        memset(mp, 0, sizeof(mp));
        memset(dp, 0, sizeof(dp));
        scanf("%d%d", &row, &col);
        for (i = 0; i < row; i++)
        {
            scanf("%d", &tempRow);
            char str[1000];
            gets(str);
            for (j = 0, temp = 0; j <= strlen(str); j++)
            {
                if (isdigit(str[j]))
                    temp = temp * 10 + str[j] - '0';
                else
                    mp[tempRow][temp] = 1, temp = 0;
            }
        }
        dp[1][1] = mp[1][1] = 1;
        for (i = 1; i <= row; i++)
            for (j = 1; j <= col; j++)
                if (!mp[i][j])  //如果没障碍
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
        printf("%d\n", dp[row][col]);
        if (T)
            printf("\n");
    }
    return 0;
}
```
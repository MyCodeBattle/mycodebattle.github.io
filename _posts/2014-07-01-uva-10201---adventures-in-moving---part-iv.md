---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 10201 - Adventures in Moving - Part IV
tags: []
layout: post
---

## 传送门

[UVa 10201 - Adventures in Moving - Part IV](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=114&page=show_problem&problem=1142)

## 题意

我们要开车从A到B，途中有很多加油站，每个加油站的汽油价格都不一样。  
车的油箱最多只能装200L的油，一开始只有100L，公司要求到目的地的时候至少要有100，否则要罚钱！  
求到达目的地最少的油钱。

## 思路

这题从中午开始想，到刚才才想明白TAT

对于每个加油站，我们有两种状态：加油、不加油。再yy一下，所以我们可以用$dp[i][j]$，表示在加油站i时，剩余油量j所用的最少的钱。

假设现在停在一个加油站。如果不加油的话，那么所用的钱就是上个加油站用的钱。$dp[i][j] = dp[i - 1][j + dis]$，其中$dis$是上个加油站到这个加油站的距离。

如果要加油的话。如果要加油的话。如果要加油的话。  
我就是这里想不通想了一个下午（╯‵□′）╯ ┴─┴ 

如果要加油的话，设加的油量为$k$，车**要出发时（也就是已经加完油）** 的油量是j，所以车刚到这个加油站的油量是$j - k$，在上一个加油站的油量是$j - k + dis$。说起来很简单，可是下午的时候怎么也绕不过弯来（ ＴДＴ）

这样一来状态转移方程就好表示了。$$dp[i][j] = min(dp[i][j], dp[i - 1][j - k + dis] + k * oil[i].price)$$

如果到达不了目的地，就是最后一个加油站和目的地的距离大于100，或者状态转移不到最后的加油站。

感觉这个是一道挺好的题目。

## 代码


```c++
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int INF = 0x3f3f3f3f;
 
struct POINT
{
    int dis, price;
};
 
int dp[110][220];   //dp[i][j]表示在第i个加油站剩余油量为j时所用最少钱
POINT oil[110];
 
int main()
{
    //freopen("in.txt", "r", stdin);
    int T, i, j, n, distance, t;
    bool flag;
    char num[110];
    scanf("%d%*c", &T);
    while (T--)
    {
        flag = true;
        int k = 1;
        scanf("%d%*c", &distance);
        oil[0].dis = oil[0].price = 0;
        while (gets(num) && num[0] != 0)
        {
            sscanf(num, "%d%d", &oil[k].dis, &oil[k].price);
            k++;
            if (oil[k - 1].dis > distance)
                k--;
        }
        k--;
        for (i = 0; i <= k; i++)
            for (j = 0; j <= 200; j++)
                dp[i][j] = INF;
        dp[0][100] = 0;
        for (i = 1; i <= k; i++)
        {
            int dis = oil[i].dis - oil[i - 1].dis; 
            if (dis > 200)
            {
                flag = false;
                break;
            }
            for (j = 0; j <= 200; j++)
            {
                if (j + dis <= 200)
                    dp[i][j] = dp[i - 1][j + dis];
                for (t = 0; t <= j; t++)
                    if (j + dis - t <= 200 && dp[i - 1][j + dis - t] != INF)
                        dp[i][j] = min(dp[i - 1][j + dis - t] + t * oil[i].price, dp[i][j]);
            }
        }
        if (100 + distance - oil[k].dis > 200 || dp[k][100 + distance - oil[k].dis] == INF || flag == false)
            printf("Impossible\n");
        else
            printf("%d\n", dp[k][100 + distance - oil[k].dis]);
        if (T)
            printf("\n");
    }
    return 0;
}
```
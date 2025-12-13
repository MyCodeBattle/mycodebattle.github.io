---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 10313 - Pay the Price
tags: []
layout: post
---

## 传送门

[UVa 10313 - Pay the Price](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=114&page=show_problem&problem=1254)

## 题意

输入的第一个数字是需要换钱的数额。

如果只有第一个数，输出总共的方式。  
如果有第二个数，输出用不超过第二个数的硬币换钱的方式。  
如果有第三个数，输出用多于第二个不超过第三个的硬币换钱的方式。

## 思路

参考了Staginner和ACEndless的解题报告。  
引用一下他的说明

> 这个题目涉及到一个结论，用不超过j个硬币凑出面值i的方案种数，是和用面值不超过j的硬币凑出面值i的方案种数是相同的。说得再数学一点，就是整数i拆分成不超过j个整数的拆分数，是和整数i拆成若干个值不超过j的整数的拆分数是相同的。具体的证明用到了Ferrers图像的性质。
> 
> 这样的话我们就可以取一个二维数组$f[i][j]$表示用面值不超过j的硬币凑出面值i的方案的种数，那么如果我使用了面值j，对应方案种数就应该加上$f[i-j][j]$，如果我们不使用面值j，那么对应的方案种数就应该加上$f[i][j-1]$。也就是说状态转移方程为$f[i][j]= f[i-j][j]+ f[i][j-1]$。

## 代码


```c++
#include <bits/stdc++.h>
using namespace std;
const int MAXN = 301;
const int INF = 0x3f3f3f3f;
#define LL long long
 
LL dp[MAXN][MAXN];

int main()
{
   // freopen("input.txt", "r", stdin);
    int n, i, j, st, ed, temp， money;
    char str[20];
    dp[0][0] = 1;
    for (i = 0; i < MAXN; i++)
        for (j = 1; j < MAXN; j++)
        {
            if (j <= i)
                dp[i][j] = dp[i - j][j] + dp[i][j - 1];
            else
                dp[i][j] = dp[i][j - 1];
        }
    while (gets(str))
    {
        st = ed = -1;
        sscanf(str, "%d%d%d", &money, &st, &ed);
        st = min(st, 300), ed = min(ed, 300);
        if (st == -1)
            printf("%lld\n", dp[money][money]);
        else if (ed == -1)
            printf("%lld\n", dp[money][st]);
        else
        {
            if (st < 2)
                printf("%lld\n", dp[money][ed]);
            else
                printf("%lld\n", dp[money][ed] - dp[money][st - 1]);
        }
    }
    return 0;
}
```
---
categories: Posts
date: 2014-06-01 00:00:00
title: UVa 103 - Stacking Boxes
tags: []
layout: post
---

## 传送门

[UVa 103 - Stacking Boxes](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=39)

## 题意

给几个N维的盒子，如果A的所有维度都比对应的小就可以装进去，求可以装的最大个数，并从小到大输出。

## 思路

这题和矩形嵌套一样，只是从二维扩展到了多维。  
话是这么说，但是昨天写过一遍的矩阵嵌套今天又忘了。。又去看了一遍  
这里增加了输出路径，只要按照嵌套个数相差1的关系进行输出即可。

## 代码


```c++
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;
const int MAXN = 40;

struct BOX
{
    int dimen[20];
}box[MAXN];

int dimen, n, dp[MAXN];
bool first;

bool isNested(const BOX &a, const BOX &b)
{
    int i;
    for (i = 0; i < dimen; i++)
        if (a.dimen[i] >= b.dimen[i])
            return false;
    return true;
}

int DFS(int i, const vector<int> *mp)
{
    int &ans = dp[i], temp;
    if (ans != -1)
        return ans;
    ans = 1;
    for (int j = 0; j < mp[i].size(); j++)
    {
        temp = DFS(mp[i][j], mp) + 1;
        ans = max(temp, ans);
    }
    return ans;
}

void PrintAns(int i, const vector<int> *mp)
{
    if (first)
    {
        printf("%d", i + 1);
        first = false;
    }
    else
        printf(" %d", i + 1);
    for (int j = 0; j < mp[i].size(); j++)
    {
        if (dp[mp[i][j]] == dp[i] - 1)
        {
            PrintAns(mp[i][j], mp);
            break;
        }
    }
}

int main()
{
    //freopen("input.txt", "r", stdin);
    int i, j, ans, target;
    while (~scanf("%d%d", &n, &dimen))
    {
        first = true;
        ans = -1;
        memset(dp, -1, sizeof(dp));
        vector<int> mp[MAXN];
        for (i = 0; i < n; i++)
        {
            for (j = 0; j < dimen; j++)
                scanf("%d", &box[i].dimen[j]);
            sort(box[i].dimen, box[i].dimen + dimen);
        }
        for (i = 0; i < n - 1; i++)
            for (j = i + 1; j < n; j++)
            {
                if (isNested(box[i], box[j]))
                    mp[i].push_back(j);
                else if (isNested(box[j], box[i]))
                    mp[j].push_back(i);
            }
            for (i = 0; i < n; i++)
            {
                int temp = DFS(i, mp);
                if (temp > ans)
                {
                    ans = temp;
                    target = i;
                }
            }
            printf("%d\n", ans);
            PrintAns(target, mp);
            printf("\n");
    }
    return 0;
}
```
---
categories: Posts
date: 2014-09-28 00:00:00
title: HDU 5055 - Bob and math problem (贪心)
tags: []
layout: post
---

## 题意

在条件下组成最大的数字。

  1. 是奇数。

  2. 0不能放在前面。


## 思路

取出一个最小的奇数放在最后，然后从最大的开始放。

代码有点不优雅。。

## 代码


```c++
#include <cstdio>
#include <stack>
#include <set>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <functional>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <ctime>
#include <cstdlib>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <cmath>
#define LL long long
#define lowbit(x) ((x) & (-x))
#define MP(a, b) make_pair(a, b)
#define MS(arr, num) memset(arr, num, sizeof(arr))
#define PB push_back
#define F first
#define S second
#define ROP freopen("input.txt", "r", stdin);
#define BitCount(x) __builtin_popcount(x)
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
using namespace std;
const int MAXN = 1e4 + 100;
const int MAXN2 = 1e6 + 5;
const int MOD = 20071027;
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
int ans[MAXN], dic[] = {1,3,5,7,9}, num[10];
 
int main()
{
    //ROP;
    int n, i, j;
    while (~scanf("%d", &n))
    {
        int pos = 1, temp;
        MS(num, 0);
        MS(ans, 0);
        for (i = 0; i < n; i++)
        {
            scanf("%d", &temp);
            num[temp]++;
        }
        bool flag = false;
        for (i = 0; i < 5; i++)
        {
            if (num[dic[i]])
            {
                ans[n] = dic[i];
                flag = true;
                num[dic[i]]--;
                break;
            }
        }
        if (!flag)
        {
            printf("-1\n");
            continue;
        }
        else
        {
            for (i = 9; i >= 1; i--)
                for (j = 0; j < num[i]; j++) ans[pos++] = i;
            if (pos == 1 && n != 1)
            {
                printf("-1\n");
                continue;
            }
        }
        for (i = 1; i <= n; i++) printf("%d", ans[i]);
        puts("");
    }
    return 0;
}
```
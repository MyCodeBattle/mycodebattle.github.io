---
categories: Posts
date: 2015-01-18 00:00:00
title: UVa 11986 - Save from Radiation (推理)
tags: []
layout: post
---

## 题意

N + 1个瓶子里有一瓶毒药，老鼠喝了就会死，现在要求用最少的老鼠判断出哪瓶是毒药

## 思路

把瓶子从000 ~ N(2进制)编号，每个瓶子都有唯一的二进制表示。

问题转化为确定毒药的二进制编号。

比如说有9个瓶子(8 + 1)，编号为0000 ~ 1000，假设有毒的是1000，也就是第9个瓶子  
现在拿出第一位编号是0的瓶子，给第一只老鼠喝。  
拿出第二位编号是0的瓶子，给第二只老鼠。  
同上，一直到第四位。  
上面的过程是同时进行的。

显然前三只都不会死，最后一只不死。  
编号确定。

所以就是求N的二进制位数

## 代码


```c++
#include <cstdio>
#include <stack>
#include <list>
#include <set>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <functional>
#include <cstring>
#include <iomanip>
#include <algorithm>
#include <cctype>
#include <string>
#include <map>
#include <cmath>
using namespace std;
#define LL long long
#define ULL unsigned long long
#define SZ(x) (int)x.size()
#define Lowbit(x) ((x) & (-x))
#define MP(a, b) make_pair(a, b)
#define MS(arr, num) memset(arr, num, sizeof(arr))
#define PB push_back
#define X first
#define Y second
#define ROP freopen("input.txt", "r", stdin);
#define MID(a, b) (a + ((b - a) >> 1))
#define LC rt << 1, l, mid
#define RC rt << 1|1, mid + 1, r
#define LRT rt << 1
#define RRT rt << 1|1
#define BitCount(x) __builtin_popcount(x)
#define BitCountll(x) __builtin_popcountll(x)
#define LeftPos(x) 32 - __builtin_clz(x) - 1
#define LeftPosll(x) 64 - __builtin_clzll(x) - 1
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
const double eps = 1e-8;
const int MAXN = 1000 + 10;
const int MOD = 1000007;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
int cases = 0;
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;

int main()
{
    LL n, T;
    cin >> T;
    while (T--)
        while (cin >> n)
        {
            if (n != 0) printf("Case %d: %d\n", ++cases, LeftPosll(n) + 1);
            else printf("Case %d: 0\n", ++cases);
        }
    return 0;
}
```
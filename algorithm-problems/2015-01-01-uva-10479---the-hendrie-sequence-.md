---
categories: Posts
date: 2015-01-01 00:00:00
title: UVa 10479 - The Hendrie Sequence (规律)
tags: []
layout: post
---

## 题意

给出一个序列的定义，求第k个数

## 思路

看的帆神题解。无限仰慕帆神中。。。

引用一下。

> 思路：写出前几个序列为  
> 0 1 02 1003 02110004 1003020211100005…..  
> 发现规律，以1,2,4,8为长度分界，每个串由1个i-2串,2个i-3串,3个i-4串….最后末尾在加上i。有了这个规律便可以递归求解，n表示为当前还需要的长度，然后用2 _m去找到一个不小于n的数字，如果等于，说明正好找到了，如果大于，那么从后面往前考虑，先把0和1的情况考虑完。如果还不满足，继续往前考虑长度为2以上的串，如果找到一个小于的，说明就在这个情况里面，然后剩下的长度为2_ 长度 - n。递归求解。

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
#include <string>
#include <map>
#include <iomanip>
#include <cmath>
#define LL long long
#define ULL unsigned long long
#define SZ(x) (int)x.size()
#define Lowbit(x) ((x) & (-x))
#define MP(a, b) make_pair(a, b)
#define MS(arr, num) memset(arr, num, sizeof(arr))
#define PB push_back
#define F first
#define S second
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
using namespace std;
const double eps = 1e-8;
const int MAXN = 1100 + 10;
const int MOD = 1000007;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
ULL Solve(ULL n)
{
    ULL m = 0;
    while ((1ull << m) < n) m++;
    if ((1ull << m) == n) return m;
    n = (1ull << m) - n - 1;
    if (n < m - 1) return 0;
    n -= m - 1;
    if (n < m - 2) return 1;
    else n -= m - 2;
    for (ULL i = 1; ; i++)
    {
        ULL len = (1ull << i);
        for (int k = 0; k < m - i - 2; k++)
            if (n >= len) n -= len;
            else return Solve((len << 1) - n);
    }
}
 
int main()
{
    ULL n;
    while (cin >> n, n)
        cout << Solve(n) << endl;
    return 0;
}
```
---
categories: Posts
date: 2014-10-10 00:00:00
title: UVa 471 - Magic Numbers (暴力)
tags: []
layout: post
---

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
#include <cmath>
#define LL long long
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
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
using namespace std;
const LL MAXN = 9876543210;
const int MOD = 1e9 + 7;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
bool Judge(LL tmp)
{
    LL cnt = 0;
    while (tmp)
    {
        if (cnt & (1 << (tmp % 10))) return false;
        cnt |= (1 << (tmp % 10));
        tmp /= 10;
    }
    return true;
}
 
 
int main()
{
    //ROP;
    int T;
    LL n, i;
    cin >> T;
    while (T--)
    {
        cin >> n;
        for (i = 1; i <= MAXN; i++)
        {
            LL tmp = n * i;
            if (tmp > MAXN) break;
            if (Judge(tmp) && Judge(i)) cout << tmp << " / " << i << " = " << n << endl;
        }
        if (T) puts("");
    }
    return 0;
}
```
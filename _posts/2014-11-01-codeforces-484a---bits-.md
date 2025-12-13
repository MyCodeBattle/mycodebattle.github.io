---
categories: Posts
date: 2014-11-01 00:00:00
title: Codeforces 484A - Bits (贪心)
tags: []
layout: post
---

## 题意

输出[l, r]中二进制数字最多的数字。

## 思路

贪心，从r的最高位1开始和l比较，直到pos[r] = 1, pos[l] = 0,这时候就可以把r的当前位置置零，之前的位置全部变成1，这个值显然>= l。

然后还要判断一下，因为可能变了之后的数量还没有变之前多。

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
#define BitCountll(x) __builtin_popcountll(x)
#define LeftPos(x) 32 - __builtin_clz(x) - 1
#define LeftPosll(x) 64 - __builtin_clzll(x) - 1
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
using namespace std;
const int MAXN = 1000000 + 10;
const int MOD = 1e9 + 7;
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
int main()
{
    //ROP;
    int T, i, j;
    scanf("%d", &T);
    while (T--)
    {
        LL l, r;
        cin >> l >> r;
        int pos = LeftPosll(r);
        LL ans = 0;
        for (; pos >= 0; pos--)
        {
            LL tmp = (r & (1ll << pos));
            if (tmp && (l & (1ll << pos)) == 0)
            {
                pos--;
                while (pos >= 0)
                {
                    ans |= (1ll << pos);
                    pos--;
                }
            }
            else if (tmp) ans |= (1ll << pos);
        }
        if (BitCountll(ans) < BitCountll(r)) ans = r;
        cout << ans << endl;
    }
    return 0;
}
```
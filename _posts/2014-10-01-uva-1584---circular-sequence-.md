---
categories: Posts
date: 2014-10-01 00:00:00
title: UVa 1584 - Circular Sequence (枚举)
tags: []
layout: post
---

## 题意

找出字典序最小的序列。

## 思路

被难题虐死，来找点自信了TAT

无脑枚举每一位开始的序列

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
const int MAXN = 100 + 10;
const int MOD = 1e9 + 7;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
int main()
{
    //ROP;
    int T, i, j;
    cin >> T;
    string str;
    while (T--)
    {
        string ans = "ZZZZZZZZZZZZZZZZZZZZZZ";
        cin >> str;
        for (i = 0; i < SZ(str); i++)
        {
            string temp;
            int cnt = 0;
            for (j = i; cnt != SZ(str); j %= SZ(str))
            {
                temp += str[j];
                cnt++; j++;
            }
            ans = min(ans, temp);
        }
        cout << ans << endl;
    }
    return 0;
}
```
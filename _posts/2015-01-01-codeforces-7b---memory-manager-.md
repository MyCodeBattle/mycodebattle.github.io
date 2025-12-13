---
categories: Posts
date: 2015-01-01 00:00:00
title: Codeforces 7B - Memory Manager (模拟)
tags: []
layout: post
---

## 题意

三个操作，输出各自的信息。

## 思路

模拟题。hcbbt巨巨找的题目，一开始以为要用线段树区间合并，然后就怂了。后来hcbbt巨巨告诉我数据量小直接模拟。

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
const int MAXN = 100 + 10;
const int MOD = 1000007;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
int room[MAXN], n, cnt;
 
void Defragment()
{
    int i, j;
    while (1)
    {
        int ctn = 0;
        bool flag = false;
        for (i = 1; i < n; i++)
        {
            if (room[i] == 0) ctn++;
            if (room[i] == 0 && room[i + 1] != 0)
            {
                int tmp = room[i + 1];
                for (j = i + 1; room[j] == tmp; j++)
                    room[j - ctn] = tmp;
                j--;
                for (int k = 0; k < ctn; k++) room[j--] = 0;
                flag = true;
                break;
            }
        }
        if (!flag) return;
    }
}
 
void Erase()
{
    int num;
    cin >> num;
    if (num <= 0)
    {
        cout << "ILLEGAL_ERASE_ARGUMENT" << endl;
        return;
    }
    bool flag = false;
    for (int i = 1; i <= n; i++)
        if (room[i] == num)
        {
            room[i] = 0;
            flag = true;
        }
    if (!flag) cout << "ILLEGAL_ERASE_ARGUMENT" << endl;
}
 
void Alloc()
{
    int sz, i, j;
    cin >> sz;
    bool flag = false;
    for (i = 1; i <= n; i++)
    {
        if (flag) break;
        if (room[i] == 0)
        {
            for (j = i; j < i + sz && j <= n; j++)
                if (room[j] != 0) break;
            if (j == i + sz)
            {
                ++cnt;
                for (--j; j >= i; j--) room[j] = cnt;
                flag = true;
            }
        }
    }
    if (flag) cout << cnt << endl;
    else cout << "NULL" << endl;
}
 
int main()
{
    //ROP;
    int m, i, j;
    cin >> m >> n;
    while (m--)
    {
        string cmd;
        cin >> cmd;
        if (cmd == "alloc") Alloc();
        else if (cmd == "erase") Erase();
        else if (cmd == "defragment") Defragment();
    }
    return 0;
}
```
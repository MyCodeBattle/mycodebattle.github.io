---
categories: Posts
date: 2014-11-01 00:00:00
title: PKU 3450 - Corporate Identity (二分 + 暴力)
tags: []
layout: post
---

## 题意

找出各个字符串中共同的子串，最长。

## 思路

枚举第一个字符串的子串，然后在之后的字符串中找。

枚举子串的时候可以用二分减少复杂度。当找到某个长度的时候再在那个长度里找字典序最小的。

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
const int MAXN = 4000 + 10;
const int MOD = 1000007;
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
string str[MAXN], ans;
int n;
bool flag;
 
bool Check(int mid)
{
    string sub;
    int j = 0;
    for (int i = 0; i + mid <= SZ(str[0]); i++)
    {
        sub = str[0].substr(i, mid);
        for (j = 1; j < n; j++)
            if (str[j].find(sub) == string::npos) break;
        if (j == n)
        {
            flag = true;
            ans = sub;
            return true;
        }
    }
    return false;
}
 
void Output()
{
    string sub;
    int j;
    for (int i = 0; i + SZ(ans) <= SZ(str[0]); i++)
    {
        sub = str[0].substr(i, SZ(ans));
        for (j = 1; j < n; j++)
            if (str[j].find(sub) == string::npos) break;
        if (j == n) ans = min(ans, sub);
    }
    cout << ans << endl;
}
 
void Solve()
{
    int l = 1, r = 200, mid;
    flag = false;
    while (l <= r)
    {
        mid = MID(l, r);
        if (mid == 0) break;
        if (Check(mid)) l = mid + 1;
        else r = mid - 1;
    }
    if (flag) Output();
    else cout << "IDENTITY LOST" << endl;
}
 
int main()
{
    //ROP;
    ios::sync_with_stdio(0);
 
    int i, j;
    while (cin >> n, n)
    {
        for (i = 0; i < n; i++) cin >> str[i];
        Solve();
    }
    return 0;
}
```
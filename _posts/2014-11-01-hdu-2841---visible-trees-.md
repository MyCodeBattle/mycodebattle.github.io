---
categories: Posts
date: 2014-11-01 00:00:00
title: HDU 2841 - Visible Trees (容斥原理)
tags: []
layout: post
---

## 题意

输出在（0,0）点能看到的树的数目。

## 思路

可知如果斜率相同的话几棵树只能被看成一颗，也就是说求(x,y)互质的数目。

可以枚举一下X，这样就变成求（1，1~n）互质的数目 + （2,2~n）+…… + （m, 1 ~ n）的数目。

如何求(1, 1 ~ n)中互质的二元组数目呢？

最容易想到的是遍历一遍，求gcd为1的个数。但是这样总的时间复杂度为$O(nlogn + n^{2})$，超时。  
可以利用容斥原理。

求出n之内和curNum有一个因数相同的数目，减去两个因数相同的，加上三个。。。以此类推

一开始我想用curNum的倍数进行容斥的，但是这样会漏掉一些情况。参考了Titanium神的题解，利用一个数的因数进行容斥。

经过我的严密推(cai)理(ce)，这样的复杂度是$O(nlogn + nk*2^k), k <= 6$

具体的请参考<http://www.cnblogs.com/scau20110726/archive/2013/03/18/2966089.html，写得很好了。>

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
const int MAXN = 100000 + 10;
const int MOD = 1000007;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };  //0123£¬ÉÏÏÂ×óÓÒ
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
vector<int> pri[MAXN];
int vis[MAXN];
 
void GetPrime()
{
    for (int i = 2; i < MAXN; i++)
    {
        if (!vis[i])
        {
            pri[i].push_back(i);
            for (int j = i * 2; j < MAXN; j += i)
            {
                pri[j].PB(i);
                vis[j] = 1;
            }
        }
    }
}
 
int n, m;
 
int CountPrime(int cur)
{
    int ans = 0;
    for (int i = 1; i < (1 << SZ(pri[cur])); i++)
    {
        int pro = 1, num = 0;
        for (int s = 0; s < SZ(pri[cur]); s++)
            if (i & (1 << s)) pro *= pri[cur][s], num++;
        if (num & 1) ans += n / pro;
        else ans -= n / pro;
    }
    return n - ans;
}
     
int main()
{
    GetPrime();
    int T, i, j;
    cin >> T;
    while (T--)
    {
        cin >> m >> n;
        LL ans = n;
        for (i = 2; i <= m; i++) ans += CountPrime(i);
        cout << ans << endl;
    }
    return 0;
}
```
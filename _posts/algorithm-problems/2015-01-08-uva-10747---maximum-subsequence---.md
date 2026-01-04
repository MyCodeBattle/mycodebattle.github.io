---
categories: Posts
date: 2015-01-08 00:00:00
title: UVa 10747 - Maximum Subsequence (贪心 + 细节)
tags: []
layout: post
---

## 题意

从N个数中选出K个数，使得乘积最大，如果有相同的乘积，输出最大的和

## 思路

最基本的思路，很好想。先按照绝对值排一下序，从头开始选K个，如果有奇数个负数，要么换一个负数，要么换一个正数。

然后就是细节的处理。然后我就像挤牙膏一样写了三个小时（ ＴДＴ）（ ＴДＴ）

导致代码无比得丑

先让我缓一下。等下再来写细节

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
const double eps = 1e-8;
const int MAXN = 10000 + 10;
const int MOD = 1000007;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
struct NUMBER
{
    int val, sign;
    bool operator < (const NUMBER &a) const
    {
        if (val != a.val) return val > a.val;
        return sign > a.sign;
    }
}arr[MAXN];
 
int n, k;
 
bool Exclude(int ans)
{
    int i, minNeg = INF;
    for (i = 0; i < k; i++)
    {
        if (arr[i].sign < 0) minNeg = min(minNeg, arr[i].val * arr[i].sign);
        if (arr[i].sign > 0) return false;
    }
    if (i == k)
    {
        int rpls = -INF;
        for (int j = k; j < n; j++)
            if (arr[j].sign > 0) return false;
        int kans = 0;
        for (i = n - 1; i > n - 1 - k; i--) kans += arr[i].sign * arr[i].val;
        printf("%d\n", kans);
        return true;
    }
}
 
void Solve()
{
    sort(arr, arr + n);
    if (n == k)     //如果nk相等，只能全部选上
    {
        int ans = 0;
        for (int i = 0; i < n; i++) ans += arr[i].val * arr[i].sign;
        printf("%d\n", ans);
        return;
    }
    int cntNegative = 0, minPositiveNumber = INF, maxNegativeNumber = -INF, ans = 0;
    bool flag = false;
    for (int i = 0; i < k; i++)
    {
        ans += arr[i].val * arr[i].sign;
        if (arr[i].val == 0) flag = true;
        if (arr[i].val * arr[i].sign < 0)
        {
            cntNegative++;
            maxNegativeNumber = max(maxNegativeNumber, arr[i].val * arr[i].sign);
        }
        else if (arr[i].val > 0) minPositiveNumber = min(minPositiveNumber, arr[i].val);
    }
    int maxPosSel = -INF, minNegSel = INF;
    for (int i = k; i < n; i++)
    {
        if (arr[i].val * arr[i].sign >= 0) maxPosSel = max(maxPosSel, arr[i].val * arr[i].sign);
        if (arr[i].val * arr[i].sign < 0) minNegSel = min(minNegSel, arr[i].val * arr[i].sign);
    }
    if ((cntNegative & 1) || flag == true)
    {
        if (arr[k].val == 0)
        {
            int kans = 0, cnt = 0;
            for (int i = 0; i < k; i++)
                if (arr[i].sign > 0)
                {
                    cnt++;
                    kans += arr[i].val;
                }
            cnt = k - cnt;
            for (int i = n - 1; cnt; i--)
                if (arr[i].sign <= 0)
                    kans += -arr[i].val, cnt--;
            printf("%d\n", kans);
        }
        else if (Exclude(ans)) return;
        //这时候要选择换掉负数还是换掉正数
        //如果后面没正数可以顶掉换下的负数，只能换正数
        else if (maxPosSel == -INF)
            printf("%d\n", ans - minPositiveNumber + minNegSel);
        //没负数可以顶掉换下的正数，只能换负数
        else if (minNegSel == INF || minPositiveNumber == INF)
            printf("%d\n", ans - maxNegativeNumber + maxPosSel);
        else if (maxPosSel * minPositiveNumber < minNegSel * maxNegativeNumber)
            printf("%d\n", ans - minPositiveNumber + minNegSel);
        else if (maxPosSel * minPositiveNumber >= minNegSel * maxNegativeNumber)
            printf("%d\n", ans - maxNegativeNumber + maxPosSel);
    }
    else printf("%d\n", ans);
}
 
int main()
{
    //ROP;
   // freopen("myout.txt", "w", stdout);
    int i, j;
    while (scanf("%d%d", &n, &k), n + k)
    {
        for (i = 0; i < n; i++)
        {
            int tmp;
            scanf("%d", &tmp);
            if (tmp < 0)
            {
                arr[i].val = -tmp;
                arr[i].sign = -1;
            }
            else if (tmp > 0)
            {
                arr[i].val = tmp;
                arr[i].sign = 1;
            }
            else
            {
                arr[i].val = 0;
                arr[i].sign = 0;
            }
        }
        Solve();
    }
    return 0;
}
```
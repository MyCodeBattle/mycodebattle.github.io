---
categories: Posts
date: 2015-02-01 00:00:00
title: HDU 5179 - beautiful number (DFS)
tags: []
layout: post
---

## 题意

求美丽数的数量。

## 思路

我能说我看了十分钟第一个公式吗（ ＴДＴ），还以为是数学题。吓得我都飞起来了。

后来又想想数应该不是很多，搜索算了。

先获得left和right的位数，然后往上填数。因为数字不大，我就直接用int变量代替数组了。

我的有点类似DFSID，按照数字的位数搜。直接写DFS也可以。

## 代码


```c++
#include <stack>
#include <cstdio>
#include <list>
#include <cassert>
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
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
const double eps = 1e-8;
const int MAXN = 1e5 + 10;
const int MOD = 9901;
const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };
int cases = 0;
typedef pair<int, int> pii;
 
int arr[MAXN];
 
int DFS(int curDep, LL num, int bitLimit, int limit)
{
    int ans = 0;
    if (limit == 0) return 0;
    int tmp = num%10;   //前一位
    for (int i = 1; i <= 9; i++)
    {
        if (i <= tmp && tmp%i == 0 || curDep == 1)
        {
            num = num*10 + i;
            if (curDep < bitLimit) return DFS(curDep+1, num, bitLimit, limit);
            if (num > limit) continue;
            if (curDep == bitLimit) ans++;  //达到指定的位数
            num /= 10;  //回溯
        }
    }
    return ans;
}
 
int get_bit(int num)
{
    int tmp = num, cnt = 0;
    while (tmp)
    {
        tmp /= 10;
        cnt++;
    }
    return cnt;
}
 
int main()
{
    //ROP;
    int T;
    scanf("%d", &T);
    while (T--)
    {
        int aans1 = 0, aans2 = 0;
        int l, r;
        scanf("%d%d", &l, &r);
        int a = get_bit(l), b = get_bit(r);
        for (int i = 1; i <= b; i++)
            aans1 += DFS(1, 0, i, r);
        for (int i = 1; i <= a; i++)
            aans2 += DFS(1, 0, i, l-1);
        printf("%d\n", aans1-aans2);
    }
    return 0;
}
```
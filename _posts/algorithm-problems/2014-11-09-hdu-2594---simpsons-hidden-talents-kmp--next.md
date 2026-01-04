---
categories: Posts
date: 2014-11-09 00:00:00
title: HDU 2594 - Simpsons’ Hidden Talents (KMP & next数组性质)
tags: []
layout: post
---

## 题意

找出最长的是str1的前缀同时是str2的后缀。

## 思路

和PKU 2752几乎一样。

把两个字符串连在一起，就可以应用next数组的特性了。

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
const int MAXN = 50000 + 10;
const int MOD = 1000007;
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
char preStr[MAXN * 2], sufiStr[MAXN];
int next[MAXN * 2], preLen, sufiLen;
 
void GetFail()
{
    next[0] = next[1] = 0;
    int m = preLen + sufiLen;
    for (int i = 1; i < m; i++)
    {
        int j = next[i];
        while (j && preStr[j] != preStr[i]) j = next[j];
        next[i + 1] = (preStr[j] == preStr[i] ? j + 1 : 0);
    }
}
 
 
int main()
{
    //ROP;
    int i;
    while (~scanf("%s%s", preStr, sufiStr))
    {
        preLen = strlen(preStr), sufiLen = strlen(sufiStr);
        strcat(preStr, sufiStr);
        GetFail();
        for (i = preLen + sufiLen; next[i] > preLen || next[i] > sufiLen; i = next[i]);
        if (next[i] == 0) puts("0");
        else
        {
            for (int j = 0; j < next[i]; j++) putchar(preStr[j]);
            printf(" %d\n", next[i]);
        }
 
    }
    return 0;
}
```
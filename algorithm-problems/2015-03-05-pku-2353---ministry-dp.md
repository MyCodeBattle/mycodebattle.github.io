---
categories: Posts
date: 2015-03-05 00:00:00
title: PKU 2353 - Ministry (DP)
tags: []
layout: post
---

## 题意

找一条从首行到尾行的路，要求权最小。

## 思路

可以从上面或者左边或者右边走过来。

先从左到右DP，再从右到左DP。

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
const int MAXN = 100 + 10;
const int MOD = 9901;
const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };
int cases = 0;
typedef pair<int, int> pii;
 
//适用于正负数,(int,long long,float,double)
template <class T>
bool Read(T &ret)
{
    char c; int sgn; T bit=0.1;
    if(c=getchar(),c==EOF) return 0;
    while(c!='-'&&c!='.'&&(!isdigit(c))) c=getchar();
    sgn=(c=='-')?-1:1;
    ret=(c=='-')?0:(c-'0');
    while(c=getchar(),isdigit(c)) ret=ret*10+(c-'0');
    if(c==' '||c=='\n'){ ret*=sgn; return 1; }
    while(c=getchar(),isdigit(c)) ret+=(c-'0')*bit,bit/=10;
    ret*=sgn;
    return 1;
}
 
int dp[110][510], arr[110][510], path[110][510];
 
void Print(int n, int pos)
{
    if (n == 1) { printf("%d\n", pos); return; }
    if (path[n][pos] == 0) Print(n-1, pos);
    else if (path[n][pos] == 1) Print(n, pos-1);
    else Print(n, pos+1);
    printf("%d\n", pos);
}
 
int main()
{
    //ROP;
    int n, m;
    while (~scanf("%d%d", &n, &m))
    {
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++) Read(arr[i][j]);
        MS(dp, INF);
        for (int i = 1; i <= m; i++) dp[1][i] = arr[1][i];
        for (int i = 2; i <= n; i++)
        {
            for (int j = 1; j <= m; j++)
            {
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]);
                if (dp[i][j] == dp[i-1][j]) path[i][j] = 0;     //up = 0
                else if (dp[i][j] == dp[i][j-1]) path[i][j] = 1; //left = 1;
                dp[i][j] += arr[i][j];
            }
            for (int j = m; j >= 1; j--)
            {
                if (dp[i][j] > dp[i][j+1] + arr[i][j])
                {
                    dp[i][j] = dp[i][j+1] + arr[i][j];
                    path[i][j] = 2;
                }
            }
        }
        int ans = dp[n][1], pos = 1;
        for (int i = 1; i <= m; i++)
        {
            if (dp[n][i] < ans)
            {
                ans = dp[n][i];
                pos = i;
            }
        }
        Print(n, pos);
    }
    return 0;
}
```
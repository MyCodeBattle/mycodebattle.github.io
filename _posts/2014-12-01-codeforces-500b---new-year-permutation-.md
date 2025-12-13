---
categories: Posts
date: 2014-12-01 00:00:00
title: Codeforces 500B - New Year Permutation (思维)
tags: []
layout: post
---

#  [Codeforces 500B - New Year Permutation (思维)](/2014/12/codeforces-500b/ "Codeforces 500B - New Year Permutation \(思维\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Dec 31 2014 9:50

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

要得到尽量从小到大排列的序列，但是只有mp[i][j] = 1的时候才能交换两个位置。问能得到的最小序列。

## 思路

显然应该把小的尽量往前换，我是先对图跑一遍Floyd，然后对每个位置从小到大扫描一遍，能换就换。hcbbt巨巨用了并查集，时间比我少一半Orz。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <iomanip>#include <cmath>#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)#define BitCountll(x) __builtin_popcountll(x)#define LeftPos(x) 32 - __builtin_clz(x) - 1#define LeftPosll(x) 64 - __builtin_clzll(x) - 1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const double eps = 1e-8;const int MAXN = 300 + 10;const int MOD = 1000007;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int mp[MAXN][MAXN];int pos[MAXN], val[MAXN], n; void Floyd(){    for (int k = 1; k <= n; k++)        for (int i = 1; i <= n; i++)            for (int j = 1; j <= n; j++)                if (mp[i][j] == 0) mp[i][j] = mp[i][k] & mp[k][j];} int main(){    //ROP;    int i, j;    scanf("%d", &n);    for (i = 1; i <= n; i++)    {        int tmp;        scanf("%d%*c", &tmp);        pos[tmp] = i, val[i] = tmp;    }    for (i = 1; i <= n; i++)    {        for (j = 1; j <= n; j++)        {            char tmp;            scanf("%c", &tmp);            mp[i][j] = tmp - '0';        }        getchar();    }    Floyd();    int conti = 1;    for (i = 1; i <= n; i++)        for (j = conti; j <= n; j++)        {            if (mp[i][pos[j]])            {                int oriPos = pos[j];                val[oriPos] = val[i];                pos[val[i]] = oriPos;                val[i] = j;                pos[j] = i;             }        }    for (i = 1; i <= n; i++)    {        if (i == 1) printf("%d", val[i]);        else printf(" %d", val[i]);    }    puts("");    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - Codeforces](/tags/Online-Judge-Codeforces/)

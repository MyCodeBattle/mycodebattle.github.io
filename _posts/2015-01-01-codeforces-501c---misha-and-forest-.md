---
categories: Posts
date: 2015-01-01 00:00:00
title: Codeforces 501C - Misha and Forest (机智)
tags: []
layout: post
---

#  [Codeforces 501C - Misha and Forest (机智)](/2015/01/codeforces-501c/ "Codeforces 501C - Misha and Forest \(机智\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jan 12 2015 21:44

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

给出每个点的度数和和这个点连接的点的异或和，输出图的每条边。

## 思路

看了squee_spoon的题解。

这题的突破口在于叶子。因为叶子的sum就是点的编号。

所以在读取输入的时候把num为1的点都加入到队列，然后取出来，之后就能得到一条边。以此类推

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778

| 
    
    
    #include <cstdio>#include <stack>#include <list>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)#define BitCountll(x) __builtin_popcountll(x)#define LeftPos(x) 32 - __builtin_clz(x) - 1#define LeftPosll(x) 64 - __builtin_clzll(x) - 1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 100000 + 10;const int MOD = 1000007;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; struct POINT{    int num, sum;}arr[MAXN]; queue<int> Q; int main(){    //ROP;    int n, i, j;    scanf("%d", &n);    int ans = 0;    for (i = 0; i < n; i++)    {        scanf("%d%d", &arr[i].num, &arr[i].sum);        ans += arr[i].num;        if (arr[i].num == 1) Q.push(i);    }    printf("%d\n", (ans>>1));    while (!Q.empty())    {        int leaf = Q.front(); Q.pop();        if (arr[leaf].num == 0) continue;        arr[leaf].num--;        int u = arr[leaf].sum;        arr[u].num--;        arr[u].sum ^= leaf;        if (arr[u].num == 1) Q.push(u);        printf("%d %d\n", leaf, u);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - Codeforces](/tags/Online-Judge-Codeforces/)[Foundation - Jizhi](/tags/Foundation-Jizhi/)

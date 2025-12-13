---
categories: Posts
date: 2014-11-01 00:00:00
title: UVa 529 - Addition Chains (DFSID + 剪枝)
tags: []
layout: post
---

#  [UVa 529 - Addition Chains (DFSID + 剪枝)](/2014/11/UVa-529/ "UVa 529 - Addition Chains \(DFSID + 剪枝\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Nov 5 2014 20:22

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

给出一个m，问以1开头m结尾的最小长度数列。其中数列中的每个数都是两个数列中的数的和。

## 思路

一开始想过DFS，但是粗略地估计了一下是$O(n^2)$级的，就没往下想了。

没想到竟然可以用DFSID！而且还不超时。。是时候去了解一下递归复杂度计算了。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768697071727374

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>#define LL long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 10000 + 10;const int MOD = 1e9 + 7; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int target, ans[MAXN]; bool DFS(int curPos, int depth){    if (curPos > depth) return false;    if (ans[curPos - 1] << (depth - curPos + 1) < target || ans[curPos - 1] + ans[curPos - 2] > target) return false;    for (int i = 1; i < curPos; i++)    {        ans[curPos] = ans[curPos - 1] + ans[i];        if (curPos == depth && ans[curPos] == target) return true;        if (DFS(curPos + 1, depth)) return true;    }    return false;}  int main(){    int m, i, j;    while (scanf("%d", ⌖), target)    {        int depth;        ans[1] = 1;        if (target == 1)        {            puts("1");            continue;        }        for (depth = 2; !DFS(2, depth); depth++);        printf("%d", ans[1]);        for (i = 2; i <= depth; i++) printf(" %d", ans[i]);        puts("");    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Foundation - Search](/tags/Foundation-Search/)

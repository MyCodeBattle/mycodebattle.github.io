---
categories: Posts
date: 2014-12-01 00:00:00
title: UVa 11127 - Triple-Free Binary Strings (位运算 + DFS)
tags: []
layout: post
---

#  [UVa 11127 - Triple-Free Binary Strings (位运算 + DFS)](/2014/12/UVa-11127/ "UVa 11127 - Triple-Free Binary Strings \(位运算 + DFS\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Dec 14 2014 18:18

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

计算给定的字符串中有几个符合条件的字符串K，满足K的所有子串不包含三个相同的字符串连起来的字符串。

## 思路

一开始枚举1024种状态，放到set里，跑得慢不说还WA了。

还是看了帆神的题解，直接用位运算来判断。

其实我奇怪的是为什么30个*不会超时。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879808182838485868788899091

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <iomanip>#include <cmath>#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)#define BitCountll(x) __builtin_popcountll(x)#define LeftPos(x) 32 - __builtin_clz(x) - 1#define LeftPosll(x) 64 - __builtin_clzll(x) - 1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const double eps = 1e-8;const int MAXN = 10000 + 10;const int MOD = 1000007;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int len;char str[50]; bool Judge(int state, int len){    int pivot = (1 << len) - 1;    int a = (state & pivot);    state >>= len;    int b = (state & pivot);    state >>= len;    if (a == b && b == state) return true;    return false;} int DFS(int state, int pos){    int tmpS = state;    for (int i = 0; i <= pos - 3; i++)    {        if ((pos - i) % 3 == 0 && Judge(tmpS, (pos - i) / 3)) return 0;        tmpS >>= 1;    }    if (pos == len) return 1;    int ans = 0;    if (str[pos] == '0') ans += DFS(state, pos + 1);    else if (str[pos] == '1') ans += DFS(state | (1 << pos), pos + 1);    else    {        ans += DFS(state, pos + 1);        ans += DFS(state | (1 << pos), pos + 1);    }    return ans;} int main(){   // ROP;    int n, i, j, cases = 0;    while (scanf("%d", &n), n)    {        scanf("%s", str);        len = strlen(str);        printf("Case %d: %d\n", ++cases, DFS(0, 0));    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Foundation - Search](/tags/Foundation-Search/)

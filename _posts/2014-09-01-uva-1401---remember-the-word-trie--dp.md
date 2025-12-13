---
categories: Posts
date: 2014-09-01 00:00:00
title: UVa 1401 - Remember the Word (Trie + DP)
tags: []
layout: post
---

#  [UVa 1401 - Remember the Word (Trie + DP)](/2014/09/UVa-1401/ "UVa 1401 - Remember the Word \(Trie + DP\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 25 2014 19:29

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

给一个字符串，求几种方式组成，由给定的字典。

## 思路

$dp[i]$表示从第i个开始的字符串，$dp[i] = sum(i + len(x))$，x是这个字符串的前缀。

用以前的版本的字典树竟然无限TLE！姿势都一样。。看来以后只能用lrj版的字典树了。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <ctime>#include <cstdlib>#include <fstream>#include <string>#include <sstream>#include <map>#include <cmath>#define LL long long#define lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 400000 + 100;const int MOD = 20071027; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int dp[300000 + 10], len; struct TRIE{    int ch[MAXN][26];    int v[MAXN];    int sz;    void init()    {        sz = 1;        MS(ch[0], 0);    }    void insert(char *s)    {        int cur = 0, leng = strlen(s);        for (int i = 0; i < leng; i++)        {            int idx = s[i] - 'a';            if (!ch[cur][idx])            {                MS(ch[sz], 0);                v[sz] = 0;                ch[cur][idx] = sz++;            }            cur = ch[cur][idx];        }        v[cur] = 1;    }    void search(char *s, int x)    {        int cur = 0;        for (int i = x; i < len; i++)        {            int idx = s[i] - 'a';            if (!ch[cur][idx]) return;            cur = ch[cur][idx];            if (v[cur]) dp[x] = (dp[x] + dp[i + 1]) % MOD;        }    }}trie; char dic[110], str[300000 + 10]; int main(){    //ROP;    int n, i, j, cases = 0;    while (~scanf("%s", str))    {        len = strlen(str);        scanf("%d", &n);        trie.init();        for (i = 0; i < n; i++)        {            scanf("%s", dic);            trie.insert(dic);        }        dp[len] = 1;        for (i = len - 1; i >= 0; i--)        {            dp[i] = 0;            trie.search(str, i);        }        printf("Case %d: %d\n", ++cases, dp[0]);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Data Structure - Trie](/tags/Data-Structure-Trie/)

---
categories: Posts
date: 2014-10-01 00:00:00
title: UVa 11732 - strcmp() Anyone? (Trie + 邻接表)
tags: []
layout: post
---

#  [UVa 11732 - strcmp() Anyone? (Trie + 邻接表)](/2014/10/UVa-11732/ "UVa 11732 - strcmp\(\) Anyone? \(Trie + 邻接表\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Oct 3 2014 11:20

**Contents**

  1. 1. 思路
  2. 2. 代码

## 思路

为了节省空间，用了邻接表。

记录一下在每个节点是否有单词结束，

然后边插入边比较

参考了ShoutMoon的代码

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <ctime>#include <cstdlib>#include <fstream>#include <string>#include <sstream>#include <map>#include <cmath>#define LL long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 4000 * 1000 + 5;const int MOD = 20071027; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; char str[1010]; struct TRIE{    int head[MAXN], next[MAXN], ch[MAXN], val[MAXN];    int sz;    LL ans;     void init()    {        sz = 1; ans = 0; ch[0] = 0; head[0] = next[0] = val[0] = 0;    }     void insert(char *s)    {        int len = strlen(s), u = 0, p;        for (int i = 0; i <= len; i++)        {            for (p = head[u]; p; p = next[p])                if (ch[p] == s[i]) break;            if (!p)            {                p = sz++;                ch[p] = s[i];                next[p] = head[u];                head[u] = p;                head[p] = 0;                val[p] = 0;            }            ans += (val[u] - val[p]) * (2 * i + 1);            if (i == len)            {                ans += val[p] * (2 * (i + 1));                val[p]++;            }            val[u]++;            u = p;        }    } }trie; int main(){    //ROP;    int n, i, j, cases = 0;    while (scanf("%d%*c", &n), n)    {        trie.init();        while (n--)        {            scanf("%s", str);            trie.insert(str);        }        printf("Case %d: %lld\n", ++cases, trie.ans);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Data Structure - Trie](/tags/Data-Structure-Trie/)

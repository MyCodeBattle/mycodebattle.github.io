---
categories: Posts
date: 2014-09-01 00:00:00
title: PKU 2001 - Shortest Prefixes (Trie)
tags: []
layout: post
---

#  [PKU 2001 - Shortest Prefixes (Trie)](/2014/09/PKU-2001/ "PKU 2001 - Shortest Prefixes \(Trie\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 22 2014 11:20

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

找出每个单词唯一的前缀

## 思路

字典树入门题。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <ctime>#include <cstdlib>#include <fstream>#include <string>#include <sstream>#include <map>#include <cmath>#define LL long long#define lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define f first#define s second#define ROP freopen("input.txt", "r", stdin);const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 1000 + 5; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; struct TRIE{    int cnt;    TRIE *next[30];    TRIE() {cnt = 0; MS(next, 0);}}; char str[MAXN][25];TRIE *root = 0; void Insert(char *str){    TRIE *p = root;    int len = strlen(str);    for (int i = 0; i < len; i++)    {        int idx = str[i] - 'a';        if (p->next[idx] == 0)        {            TRIE *temp = new TRIE();            p->next[idx] = temp;        }        p = p->next[idx];        p->cnt++;    }} void Search(char *str){    TRIE *cur = root;    int len = strlen(str);    for (int i = 0; i < len; i++)    {        int idx = str[i] - 'a';        cur = cur->next[idx];        putchar(str[i]);        if (cur->cnt == 1) break;    }    puts("");} int main(){    //ROP;    int i, j, k = 0;    root = new TRIE();    while (gets(str[k]))        Insert(str[k++]);    for (i = 0; i < k; i++)    {        printf("%s ", str[i]);        Search(str[i]);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - PKU](/tags/Online-Judge-PKU/)[Data Structure - Trie](/tags/Data-Structure-Trie/)

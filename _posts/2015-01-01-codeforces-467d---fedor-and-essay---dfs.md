---
categories: Posts
date: 2015-01-01 00:00:00
title: Codeforces 467D - Fedor and Essay (反向建图 + DFS)
tags: []
layout: post
---

## 题意

给出原文的几个单词和几组替换词，要求最后包含的r最少，长度越短越好。

## 思路

因为替换的终点肯定可以确定（R最少的单词），所以可以反向建图，把所有单词按照r排序以后DFS一遍，把它们能走到的点的r和size都更新为自己的r、size。

然后直接统计文章中的单词的r和sz

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127128129130131132133134135

| ```c++
#include <stack>#include <cstdio>#include <list>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)#define BitCountll(x) __builtin_popcountll(x)#define LeftPos(x) 32 - __builtin_clz(x) - 1#define LeftPosll(x) 64 - __builtin_clzll(x) - 1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 2e5 + 10;const int MOD = 29;const int dir[][2] = { {1, 0}, {0, 1} };int cases = 0;typedef pair<int, int> pii; struct NODE{    int id, rNum, sz;    bool operator < (const NODE &a) const    {        if (rNum != a.rNum) return rNum < a.rNum;        return sz < a.sz;    }}; void ChangeToLower(string &str){    for (int i = 0; i < SZ(str); i++) str[i] = tolower(str[i]);} int CountR(const string &str){    int cnt = 0;    for (int i = 0; i < SZ(str); i++)        if (str[i] == 'r') cnt++;    return cnt;} map<string, int> oddId;map<int, int> newId;int cnt;vector<NODE> words; int GetNumber(string &tmp){    ChangeToLower(tmp);    if (oddId.count(tmp)) return oddId[tmp];    oddId[tmp] = cnt;    int r = CountR(tmp);    words.PB((NODE){cnt, r, SZ(tmp)});    cnt++;    return cnt - 1;} vector<int> G[MAXN], article;int vis[MAXN]; void DFS(int curId, int r, int sz){    vis[curId] = 1;    for (int i = 0; i < SZ(G[curId]); i++)    {        int tmpId = G[curId][i];        if (!vis[tmpId])        {            vis[tmpId] = 1;            words[newId[tmpId]].rNum = r;            words[newId[tmpId]].sz = sz;            DFS(tmpId, r, sz);        }    }} int main(){    //ROP;    int n;    cin >> n;    for (int i = 0; i < n; i++)    {        string tmp;        cin >> tmp;        int curNumber = GetNumber(tmp);        article.PB(curNumber);    }    int ncnv;    cin >> ncnv;    for (int i = 0; i < ncnv; i++)    {        string tmp;        cin >> tmp;        int u = GetNumber(tmp);        cin >> tmp;        int v = GetNumber(tmp);        G[v].PB(u);    }    sort(words.begin(), words.end());    for (int i = 0; i < SZ(words); i++) newId[words[i].id] = i;    for (int i = 0; i < SZ(words); i++)        if (!vis[words[i].id]) DFS(words[i].id, words[i].rNum, words[i].sz);    LL rAns = 0, szAns = 0;    for (int i = 0; i < SZ(article); i++)        rAns += words[newId[article[i]]].rNum, szAns += words[newId[article[i]]].sz;    cout << rAns << " " << szAns << endl;    return 0;}
```
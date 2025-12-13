---
categories: Posts
date: 2015-02-01 00:00:00
title: HDU 1973 - Prime Path (BFS)
tags: []
layout: post
---

## 题意

给定一个初始素数和终止素数，问能不能通过改变一个数位最后到达终点。

## 思路

BFS

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114

| ```c++
#include <stack>#include <cstdio>#include <list>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 10000 + 10;const int MOD = 29;const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };int cases = 0;typedef pair<int, int> pii; set<int> prime;int vis[MAXN], ed, arr[5], mp[MAXN];queue<pii> Q; void GetPrimeTable(){    int n = sqrt(MAXN + 0.5);    for (int i = 2; i < MAXN; i++) if (!vis[i])    {        prime.insert(i);        for (int j = i*i; j < MAXN; j += i) vis[j] = 1;    }} bool Solve(int style, int k, pii &ori){    int tmpNum = 0;    for (int i = 1; i <= 4; i++) tmpNum = ((style^i) ? tmpNum*10 + arr[i] : tmpNum*10 + k);    if (tmpNum <= 1000) return false;    if (!mp[tmpNum] && prime.count(tmpNum))    {        Q.push(MP(tmpNum, ori.Y + 1));        mp[tmpNum] = 1;    }    if (tmpNum == ed)    {        printf("%d\n", ori.Y + 1);        return true;    }    return false;} void Handle(int num){    for (int i = 4; i >= 1; i--)    {        arr[i] = num % 10;        num /= 10;    }} void BFS(){    while (!Q.empty())    {        pii tmp = Q.front(); Q.pop();        Handle(tmp.X);        for (int i = 1; i <= 4; i++)            for (int j = 0; j < 10; j++) if (Solve(i, j, tmp)) return;    }    puts("Impossible");} int main(){    //ROP;    GetPrimeTable();    int T;    scanf("%d", &T);    while (T--)    {        MS(mp, 0);        while (!Q.empty()) Q.pop();        int st;        scanf("%d%d", &st, &ed);        if (st == ed)        {            puts("0");            continue;        }        Q.push(MP(st, 0));        BFS();    }}
```
---
categories: Posts
date: 2015-03-01 00:00:00
title: Google Code Jam 2014 1A - Charging Chaos (思维)
tags: []
layout: post
---

## 题意

给出几个01组成的初始串，和相同个数的目标串。  
问能不能通过反转某一位使得初始串和目标串相同，如果能的话求最少。

## 思路

小数据可以状态压缩暴力，大的就不行了。

可以从目标串来考虑。  
我们可以得出每个初始串变成每个目标串所需的操作串，放到一个集合里。

比如初始串为101，目标串为001，操作串就是每一位的异或，100。

因为根据题意，如果有答案的话，存在一个操作串使得每一个初始串 ^ 它都能变成一个目标串。这个操作串必然在集合里。

然后检查一遍集合里的操作串的可行性，维护最小值即可。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768697071727374757677787980818283848586878889909192939495

| ```c++
#include <stack>#include <cstdio>#include <list>#include <cassert>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 200;const int MOD = 9901;const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };int cases = 0;typedef pair<int, int> pii; LL curTar[MAXN], pat[MAXN], tar[MAXN], sorted_target[MAXN];int n; bool Check(LL num){    for (int i = 0; i < n; i++) curTar[i] = pat[i]^num;    sort(curTar, curTar+n);    for (int i = 0; i < n; i++)        if (curTar[i] != sorted_target[i]) return false;    return true;} char tmp[50]; LL ReadBits(){    scanf("%s", tmp);    LL ret = 0;    for (int i = 0; i < strlen(tmp); i++)    {        ret <<= 1;        ret += tmp[i]-'0';    }    return ret;} set<LL> mp; int main(){    //ROP;    //freopen("out.txt", "w", stdout);    int T;    scanf("%d", &T);    while (T--)    {        mp.clear();        printf("Case #%d: ", ++cases);        int l;        scanf("%d%d", &n, &l);        for (int i = 0; i < n; i++) pat[i] = ReadBits();        for (int i = 0; i < n; i++) tar[i] = ReadBits(), sorted_target[i] = tar[i];        sort(sorted_target, sorted_target+n);        for (int i = 0; i < n; i++)            for (int j = 0; j < n; j++) mp.insert(pat[i]^tar[j]);        set<LL>::iterator it = mp.begin();        int ans = INF;        for (; it != mp.end(); it++)            if (Check(*it)) ans = min(ans, __builtin_popcountll(*it));        if (ans == INF) printf("NOT POSSIBLE\n");        else printf("%d\n", ans);    }    return 0;}
```
---
categories: Posts
date: 2015-02-01 00:00:00
title: Codeforces 514C - Watto and Mechanism (Trie + DFS)
tags: []
layout: post
---

## 题意

给一些模板串，再给出一些字符串，问能不能通过改变一个字符，使存在同样的模板串。

## 思路

建树，然后对于每个位置的字符，如果之前已经被改变过了，那么没有选择只能DFS下去。  
如果没被改变，可以不改变DFS下去，也可以改变字符DFS。

* * *

这题正确的姿势应该是hash，不过我用BKDRHash写了一下TLE了。估计是hash的方法有点问题。

然后很多人用Trie过了。我对这种方法的复杂度存在怀疑。

我觉(Y)得(Y)可以构造出数据，使得这种方法的复杂度为$O(n^2)$。

不过题目限定了字符的总长度。

反正我还是不会算。而且实际证明这种方法还是跑得很快的。只比hash(100+ms)慢一点点(240+ms)

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119

| ```c++
#include <stack>#include <cstdio>#include <list>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 6e5 + 10;const int MOD = 1e9 + 7;const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };const int hash_size = 4e5 + 10;int cases = 0;typedef pair<int, int> pii; char str[MAXN]; struct TRIE{    int ch[MAXN][3], v[MAXN], sz;     int get_idx(char c) { return c-'a'; }    void init()    {        sz = 1;        MS(ch[0], 0);    }     void insert(char *s)    {        int cur = 0, len = strlen(s);        for (int i = 0; i < len; i++)        {            int idx = s[i] - 'a';            if (!ch[cur][idx])            {                MS(ch[sz], 0);                v[sz] = 0;                ch[cur][idx] = sz++;            }            cur = ch[cur][idx];        }        v[cur] = 1;    }     bool find(int node, int len, int flag)    {        if (str[len] == 0)        {            if (flag && v[node] == 1)                return true;            return false;        }        if (flag)        {            if (ch[node][get_idx(str[len])] != 0 && find(ch[node][get_idx(str[len])], len+1, flag)) return true;            return false;        }        else        {            if (ch[node][get_idx(str[len])] != 0)                if (find(ch[node][get_idx(str[len])], len+1, flag))return true;            for (int i = 0; i < 3; i++)            {                if (i == get_idx(str[len])) continue;                if (ch[node][i] != 0)                    if (find(ch[node][i], len+1, flag+1)) return true;            }            return false;        }    } }trie; int main(){    //ROP;    int n, m;    scanf("%d%d", &n, &m);    trie.init();    for (int i = 0; i < n; i++)    {        scanf("%s", str);        trie.insert(str);    }    for (int i = 0; i < m; i++)    {        scanf("%s", str);        if (trie.find(0, 0, 0)) puts("YES");        else puts("NO");    }    return 0;}
```
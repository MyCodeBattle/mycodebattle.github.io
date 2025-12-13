---
categories: Posts
date: 2015-01-01 00:00:00
title: UVa 1449 - Dominating Patterns (AC自动机)
tags: []
layout: post
---

## 题意

在文本串里找出出现次数最多的模式串。

## 思路

AC自动机例题。

## 代码


```c++
#include <stack>
#include <cstdio>
#include <list>
#include <set>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <functional>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <string>
#include <map>
#include <cmath>
using namespace std;
#define LL long long
#define ULL unsigned long long
#define SZ(x) (int)x.size()
#define Lowbit(x) ((x) & (-x))
#define MP(a, b) make_pair(a, b)
#define MS(arr, num) memset(arr, num, sizeof(arr))
#define PB push_back
#define X first
#define Y second
#define ROP freopen("input.txt", "r", stdin);
#define MID(a, b) (a + ((b - a) >> 1))
#define LC rt << 1, l, mid
#define RC rt << 1|1, mid + 1, r
#define LRT rt << 1
#define RRT rt << 1|1
#define BitCount(x) __builtin_popcount(x)
#define BitCountll(x) __builtin_popcountll(x)
#define LeftPos(x) 32 - __builtin_clz(x) - 1
#define LeftPosll(x) 64 - __builtin_clzll(x) - 1
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
const double eps = 1e-8;
const int MAXN = 5e5 + 10;
const int MOD = 1000007;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
int cases = 0;
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
int ans;
 
const int MAXNODE = 150 * 70 + 10, SIGMA_SIZE = 26;
char str[MAXN * 2];
int ch[MAXNODE][SIGMA_SIZE];
int val[MAXNODE], cnt[200];
int last[MAXNODE];
int fail[MAXNODE];
map<string, int> mp;
 
struct AC
{
 
    int sz;
 
 
    void init()
    {
        sz = 1;
        MS(ch[0], 0); MS(cnt, 0);
        mp.clear();
    }
 
    int idx(char c) { return c - 'a'; }
 
    void insert(const char *s, int k)
    {
        int u = 0, len = strlen(s);
        for (int i = 0; i < len; i++)
        {
            int c = idx(s[i]);
            if (!ch[u][c])
            {
                MS(ch[sz], 0);
                val[sz] = 0;
                ch[u][c] = sz++;
            }
            u = ch[u][c];
        }
        val[u] = k;
        mp[s] = k;
    }
 
    //AC?Զ???????
 
    void get_fail()
    {
        queue<int> Q;
        fail[0] = 0;
        for (int c = 0; c < SIGMA_SIZE; c++)
        {
            int u = ch[0][c];
            if (u)
            {
                fail[u] = 0;
                Q.push(u);
                last[u] = 0;
            }
        }
        while (!Q.empty())
        {
            int r = Q.front(); Q.pop();
            for (int c = 0; c < SIGMA_SIZE; c++)
            {
                int u = ch[r][c];
                if (!u)
                {
                    ch[r][c] = ch[fail[r]][c];
                    continue;
                }
                Q.push(u);
                int v = fail[r];
                while (v && !ch[v][c]) v = fail[v];
                fail[u] = ch[v][c];
                last[u] = val[fail[u]] ? fail[u] : last[fail[u]];
            }
        }
    }
 
    void sum(int j)
    {
        if (j)
        {
            cnt[val[j]]++;
            sum(last[j]);
        }
    }
 
    void find(char *T)
    {
        int len = strlen(T);
        int j = 0;
        for (int i = 0; i < len; i++)
        {
            int c = idx(T[i]);
            j = ch[j][c];
            if (val[j]) sum(j);
            else if (last[j]) sum(last[j]);
        }
    }
};
 
vector<string> arr;
int n;
 
void Input(AC ∾)
{
    string tmp;
    for (int i = 1; i <= n; i++)
    {
        cin >> tmp;
        arr.PB(tmp);
        ac.insert(tmp.c_str(), i);
    }
}
 
int main()
{
    //ROP;
    AC ac;
    while (scanf("%d", &n), n)
    {
        ac.init();
        arr.clear();
        Input(ac);
        ac.get_fail();
        scanf("%s", str);
        ac.find(str);
        int maxCnt = -1;
        for (int i = 1; i <= n; i++)
            maxCnt = max(maxCnt, cnt[i]);
        cout << maxCnt << endl;
        for (int i = 0; i < SZ(arr); i++)
            if (cnt[mp[arr[i]]] == maxCnt) cout << arr[i] << endl;
    }
    return 0;
}
```
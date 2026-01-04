---
categories: Posts
date: 2015-01-19 00:00:00
title: HDU 2222 - Keywords Search (AC自动机)
tags: []
layout: post
---

## 思路

AC自动机模板题。

测了一下LRJ的模板。

## 代码


```c++
#include <cstdio>
#include <stack>
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
 
const int MAXNODE = 1e4 + 10, SIGMA_SIZE = 26;
char str[MAXN * 2];
int ch[MAXN][SIGMA_SIZE];   //Trie树结点
int val[MAXN];      //结点附加信息
int last[MAXN];     //后缀链接
int vis[MAXN];
int fail[MAXN];     //转移函数
 
struct AC
{
    //Trie部分
    int sz;
 
    void init()
    {
        sz = 1;
        MS(ch[0], 0);
    }
     
    int idx(char c) { return c - 'a'; }
 
    void insert(char *s)
    {
        int u = 0, n = strlen(s);
        for (int i = 0; i < n; i++)
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
        val[u]++;
    }
 
    //AC自动机部分
 
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
            if (vis[j]) return;
            vis[j] = 1;
            ans += val[j];
            sum(last[j]);
        }
    }
 
    void find(char *T)
    {
        int n = strlen(T);
        int j = 0;
        for (int i = 0; i < n; i++)
        {
            int c = idx(T[i]);
            j = ch[j][c];
            if (val[j]) sum(j);
            else if (last[j]) sum(last[j]);
        }
    }
};
 
int main()
{
    //ROP;
    int T;
    scanf("%d", &T);
    AC ac;
    char tmp[60];
    while (T--)
    {
        ac.init();
        MS(vis, 0);
        int n;
        ans = 0;
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
        {
            scanf("%s", tmp);
            ac.insert(tmp);
        }
        scanf("%s", str);
        ac.get_fail();
        ac.find(str);
        printf("%d\n", ans);
    }
    return 0;
}
```
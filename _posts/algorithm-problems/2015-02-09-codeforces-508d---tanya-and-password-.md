---
categories: Posts
date: 2015-02-09 00:00:00
title: Codeforces 508D - Tanya and Password (欧拉道路)
tags: []
layout: post
---

## 题意

一个句子被拆成三个三个的单词，问能不能拼起来。

## 思路

以前两个字母为起点，后两个字母为终点，连一条边。如果存在一条欧拉道路则可以拼起来。

如何判断存在欧拉道路？

  1. 有一个点出度大于入度和一个点入度大于出度
  2. 其他的点出度和入度必须是偶数


然后就是找欧拉道路的方法。

因为可能会自环，所以直接用结构体记录已经访问了几次。访问完一个点的相连的所有边，记录下这个点。

最后reverse一下。

看了**AOQNRMGYXLMV** 的题解。非常漂亮的代码。

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
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
const double eps = 1e-8;
const int MAXN = 62*62;
const int MOD = 2009;
const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };
int cases = 0;
typedef pair<int, int> pii;
 
const int RADIX = 62;
vector<int> G[MAXN];
 
struct POINT
{
    int in, out, cnt;
}p[MAXN];
 
int CharToNumber(char c)
{
    if (islower(c)) return c - 'a';
    if (isupper(c)) return 26 + c - 'A';
    if (isdigit(c)) return 52 + c - '0';
}
 
void GetVertexNumber(const string &str, int &u, int &v)
{
    u = CharToNumber(str[0]) * RADIX + CharToNumber(str[1]);
    v = CharToNumber(str[1]) * RADIX + CharToNumber(str[2]);
}
 
char NumberToChar(int num)
{
    if (num < 26) return num + 'a';
    if (num < 52) return num + 'A' - 26;
    return num + '0' - 52;
}
 
void DFS(int curNode, string &ans)
{
    while (p[curNode].cnt < SZ(G[curNode])) DFS(G[curNode][p[curNode].cnt++], ans);
    ans += NumberToChar(curNode % RADIX);
}
 
int main()
{
    ios::sync_with_stdio(0);
 
   // ROP;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        string str;
        cin >> str;
        int u, v;
        GetVertexNumber(str, u, v);
        G[u].PB(v);
        p[u].out++, p[v].in++;
    }
    int st = -1;
    for (int i = 0; i < MAXN; i++)
    {
        if (abs(p[i].in - p[i].out) > 1) { cout << "NO"; return 0; }
        if (p[i].in < p[i].out)
        {
            if (st != -1) { cout << "NO"; return 0; }
            st = i;
        }
    }
    if (st == -1)
        for (int i = 0; i < MAXN; i++)
            if (!G[i].empty())
            {
                st = i;
                break;
            }
    string ans;
    DFS(st, ans);
    ans += NumberToChar(st / RADIX);
    reverse(ans.begin(), ans.end());
    if (SZ(ans) != n + 2) { cout << "NO"; return 0; }
    else cout << "YES" << endl << ans << endl;
    return 0;
}
```
---
categories: Posts
date: 2015-02-03 00:00:00
title: Codeforces 510C - Fox And Names (拓扑排序)
tags: []
layout: post
---

## 题意

给出一串名字，代表着字典序从小到大，要求输出符合上述字符串排序的字典序。

## 思路

看了飞火扑蛾的题解。

学习了拓扑排序。

如果一个字符串是另一个字符串的前缀并且另一个字符串排在这个字符串之前，这样肯定是不行的。可以直接输出Impossible。

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
#include <unordered_set>
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
const int MAXN = 30 + 10;
const int MOD = 29;
const int dir[][2] = { { 1, 0 }, { 0, 1 } };
int cases = 0;
typedef pair<int, int> pii;
 
int mp[MAXN][MAXN], in[MAXN];
vector<char> ans;
const int sigma_size = 26;
 
void BFS()
{
    queue<int> Q;
    for (int i = 0; i < sigma_size; i++)
        if (in[i] == 0)
        {
            Q.push(i);
            ans.PB(i);
        }
    while (!Q.empty())
    {
        int cur = Q.front(); Q.pop();
        for (int i = 0; i < sigma_size; i++)
        {
            if (mp[cur][i])
            {
                in[i]--;
                if (in[i] == 0)
                {
                    Q.push(i);
                    ans.PB(i);
                }
            }
        }
    }
    if (SZ(ans) != sigma_size) cout << "Impossible" << endl;
    else
        for (auto &i: ans) cout << (char)(i+'a');
 
}
 
string str[110];
 
int idx(char c) { return c - 'a'; }
 
int main()
{
    //ROP;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) cin >> str[i];
    int i, j;
    for (i = 0; i < n-1; i++)
    {
        bool flag = false;
        for (j = 0; j < min(SZ(str[i]), SZ(str[i+1])); j++)
        {
            if (str[i][j] == str[i+1][j]) continue;
            flag = true;
            int a = idx(str[i][j]), b = idx(str[i+1][j]);
            if (!mp[a][b])
            {
                mp[a][b] = 1;
                in[b]++;
            }
            break;
        }
        if (!flag && SZ(str[i]) > SZ(str[i+1]))
        {
            cout <<"Impossible" << endl;
            return 0;
        }
    }
    BFS();
    return 0;
}
```
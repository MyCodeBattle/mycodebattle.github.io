---
categories: Posts
date: 2014-09-22 00:00:00
title: PKU 3630 - Phone List (Trie)
tags: []
layout: post
---

## 题意

查找是否有串是其他串的子串。

## 思路

一开始的思路是将串按长度排序，如果有串走完了以后那个位置已经被人走过，就是子串，用的是new的方式，MLE了。

后来释放了一下内存，TLE了。看了别人的题解，原来用静态的Trie才能过。

改了一下静态，过了。值得一提的是一开始的版本我在HDU上提交是500ms，静态版本提交是60ms，虽然算法有有一点变化，但是效率差34倍是有的。怪不得LRJ老师用的是静态版本。

## 代码


```c++
#include <cstdio>
#include <stack>
#include <set>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <functional>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <ctime>
#include <cstdlib>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <cmath>
#define LL long long
#define lowbit(x) ((x) & (-x))
#define MP(a, b) make_pair(a, b)
#define MS(arr, num) memset(arr, num, sizeof(arr))
#define PB push_back
#define F first
#define S second
#define ROP freopen("input.txt", "r", stdin);
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
using namespace std;
const int MAXN = 10000 + 5;
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
struct TRIE
{
    int ed, pass;
    int next[10];
}trie[MAXN * 10];
 
int cnt;
char str[15];
 
bool Insert(int root, char *str)
{
    int cur = root;
    for (int i = 0; str[i]; i++)
    {
        int idx = str[i] - '0';
        if (trie[cur].next[idx] == 0)
            trie[cur].next[idx] = ++cnt;
        cur = trie[cur].next[idx];
        trie[cur].pass++;
        if (trie[cur].ed) return false;
    }
    if (trie[cur].pass > 1) return false;
    trie[cur].ed = 1;
    return true;
}
 
int main()
{
    //ROP;
    int T, i, j, n;
    scanf("%d", &T);
    while(T--)
    {
        cnt = 0;
        MS(trie, 0);
        scanf("%d%*c", &n);
        bool flag = false;
        for (i = 0; i < n; i++)
        {
 
            gets(str);
            if (flag) continue;
            if (Insert(0, str) == false) flag = true;
        }
        printf("%s\n", flag ? "NO" : "YES");
    }
    return 0;
}
```
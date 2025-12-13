---
categories: Posts
date: 2014-09-01 00:00:00
title: The daily life about a frog.
tags: []
layout: post
---

## 题意

每个人可以选择first name 或者 last name 当自己的账号，现在给出最终的字典序排位，问能不能实现

## 思路

模拟一下。

lst用于记录上一个人选择的账号。

第一个人肯定要选择last name和first name里最小的，记为lst

第二个人，如果其中小的比lst大，那么就选择那个。如果比lst小，那么再次比较较大的和lst，如果还是比lst小，这个排序不能进行了。

以此类推。

## 代码

[CODE_BLOCK_0]| ```c++
#include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <ctime>#include <cstdlib>#include <fstream>#include <string>#include <sstream>#include <map>#include <cmath>#define LL long long#define lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 1e5 + 100;const int MOD = 20071027; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; struct NAME{    int id;    string fstr, sstr;}name[MAXN]; int main(){    //ROP;    ios::sync_with_stdio(0);         int n, i, j, tmp;    cin >> n;    for (i = 1; i <= n; i++) cin >> name[i].fstr >> name[i].sstr;    cin >> tmp;    string lst = min(name[tmp].fstr, name[tmp].sstr);    bool flag = true;    for (i = 0; i < n - 1; i++)    {        cin >> tmp;        if (!flag) continue;        string temp = min(name[tmp].fstr, name[tmp].sstr);        if (lst >= temp)        {            if (lst >= max(name[tmp].fstr, name[tmp].sstr))                flag = false;            else                lst = max(name[tmp].fstr, name[tmp].sstr);        }        else lst = temp;    }    printf("%s\n", flag ? "YES" : "NO");    return 0;}
```  
---|---
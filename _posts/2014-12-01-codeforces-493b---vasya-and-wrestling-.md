---
categories: Posts
date: 2014-12-01 00:00:00
title: Codeforces 493B - Vasya and Wrestling (模拟)
tags: []
layout: post
---

## 思路

乱搞了。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104

| ```c++
#include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <ctime>#include <string>#include <map>#include <iomanip>#include <cmath>#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)#define BitCountll(x) __builtin_popcountll(x)#define LeftPos(x) 32 - __builtin_clz(x) - 1#define LeftPosll(x) 64 - __builtin_clzll(x) - 1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const double eps = 1e-6;const int MAXN = 2e5 + 10;const int MOD = 1000007;const int dir[][2] = { {1, 0}, {-1, 0}, {0, -1}, {0, 1} }; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; char s[100];vector<int> num1, num2; int Cmp(){    for (int i = 0; i < min(SZ(num1), SZ(num2)); i++)    {        if (num1[i] > num2[i]) return 1;        else if (num1[i] < num2[i]) return -1;    }    if (SZ(num1) < SZ(num2)) return -1;    else if (SZ(num1) > SZ(num2)) return 1;    return 0;} int main(){    //ROP;    ios::sync_with_stdio(0);     int n, i, j, lst;    LL cnt1 = 0, cnt2 = 0;    LL sum1 = 0, sum2 = 0;    cin >> n;    bool flag;    for (int i = 0; i < n; i++)    {        int tmp;        cin >> tmp;        flag = false;        if (tmp < 0)        {            flag = true;            tmp = -tmp;        }        if (flag)        {            num2.PB(tmp);            sum2 += tmp;        }        else        {            num1.PB(tmp);            sum1 += tmp;        }    }    if (sum1 > sum2) cout << "first" << endl;    else if (sum1 < sum2) cout << "second" << endl;    else    {        if (Cmp() == 1) cout << "first" << endl;        else if (Cmp() == -1) cout << "second" << endl;        else if (!flag) cout << "first" << endl;        else cout << "second" << endl;    }    return 0;}
```
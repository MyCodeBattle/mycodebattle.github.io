---
categories: Posts
date: 2014-10-01 00:00:00
title: ZJU 3829 - Known Notation (贪心)
tags: []
layout: post
---

## 题意

输出最少的操作次数，使得成为逆波兰表达式

## 思路

显然只有缺少数字的时候才用到插入，不然就用交换。

交换的时候从最后面的数字开始交换。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768697071727374757677787980818283848586878889909192

| ```c++
#include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>#define LL long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 2000 + 10;const int MOD = 1e9 + 7;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };  typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii;  int fun[MAXN];char str[MAXN];  int main(){    //ROP;    ios::sync_with_stdio(0);      int T, i, j;    cin >> T;    while (T--)    {        string str;        cin >> str;        int num = 0, ope = 0, pos = 0;        for (i = SZ(str) - 1; i >= 0; i--)        {            if (str[i] != '*')            {                fun[pos++] = i;                num++;            }            else ope++;        }        if (num == SZ(str))        {            cout << "0" << endl;            continue;        }        int ans = max(0, ope + 1 - num);        int curNum = 0, curOp = 0;        curNum = ans;        pos = 0;        for (i = 0; i < SZ(str); i++)        {            if (str[i] != '*') curNum++;            else            {                if (curOp + 1 >= curNum)                {                    swap(str[i], str[fun[pos++]]);                    ans++;                    curNum++;                }                else curOp++;            }        }        if (str[SZ(str) - 1] != '*') ans++;        cout << ans << endl;    }    return 0;}
```
---
categories: Posts
date: 2014-09-01 00:00:00
title: PKU 2752 - Seek the Name, Seek the Fame (KMP)
tags: []
layout: post
---

## 题意

输出既是前缀也是后缀的子串的长度。

## 思路

失配函数的应用。引用一下**飘过的小牛** 的说明

> 1）当i = len时，next[len] = next[18] = 9，说明整个字符串前9个字符和后9个字符相同，所以9是满足要求的。
> 
> 2）next[9] = 4，说明在0-8中前4个字符和后4个字符相同。因为由1）得前9个字符和后9个字符相同，所以，S串的0-3等于5-8，而0-3又等于9-12,5-8又等于14-17，所以结果是0-3等于14-17，即4也是满足题意的。
> 
> 3）next[4]=2，同2，我们可以得到2也是满足题意的。
> 
> 4）next[2]=0，表明没有相同的前缀和后缀了，这时，就已经找到了这个S串的所有前缀和后缀。
> 
> 5）结果就是2,4,9,18.

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768697071

| ```c++
#include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <ctime>#include <cstdlib>#include <fstream>#include <string>#include <sstream>#include <map>#include <cmath>#define LL long long#define lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 4e5 + 5;const int MOD = 20071027; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; char str[MAXN];int len, f[MAXN]; vector<int> ans; void GetFail(){    f[0] = f[1] = 0;    for (int i = 1; i < len; i++)    {        int j = f[i];        while (j && str[j] != str[i]) j = f[j];        f[i + 1] = (str[j] == str[i] ? j + 1 : 0);    }} int main(){    //ROP;    int i, j;    while (~scanf("%s", str))    {        ans.clear();        len = strlen(str);        GetFail();        for (i = len; i; i = f[i]) ans.PB(i);        for (i = (int)ans.size() - 1; i >= 0; i--)        {            if (i) printf("%d ", ans[i]);            else printf("%d\n", ans[i]);        }    }    return 0;}
```
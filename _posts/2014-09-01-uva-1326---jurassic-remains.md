---
categories: Posts
date: 2014-09-01 00:00:00
title: UVa 1326 - Jurassic Remains
tags: []
layout: post
---

## 传送门

[UVa 1326 - Jurassic Remains](http://acm.hust.edu.cn/vjudge/problem/viewProblem.action?id=36129)

## 题意

找出尽量多的串，使每个字母都出现偶数次

## 思路

因为N<=24，考虑状态压缩。而对于每一个状态，可以用1表示出现奇数，0表示出现偶数，再对一个串中的字母进行状态压缩。

但是如果一直^到最后，复杂度为$O(2^n)$，TLE。考虑枚举一半的串的状态，然后在后一半中查找。因为只有两个相同的状态值异或才可以符合条件。

这样复杂度就变成$O(1.414^n)$

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768

| ```c++
#include<bits/stdc++.h>#define LL long long#define lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)const int MAXN = 30 + 5;const int INF = 0x3f3f3f3f;using namespace std; typedef pair<int, int> pii;typedef vector<int> vei;typedef vector<pair<int, int> >veii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii;typedef priority_queue<pii, vector<pii>, greater<pii> >pquii; char word[1000];int num[MAXN];map<int, int> mp; int BitCount(int x){    return x == 0 ? 0 : BitCount(x >> 1) + (x & 1);} int main(){    //freopen("input.txt", "r", stdin);    int n, i, j;    while (~scanf("%d", &n))    {        mp.clear();        for (i = 0; i < n; i++)        {            scanf("%s", word);            num[i] = 0;            for (j = 0; word[j]; j++)                num[i] ^= (1 << (word[j] - 'A'));        }        int n1 = n / 2, n2 = n - n1;        for (int state = 0; state < (1 << n1); state++)        {            int cur = 0;            for (i = 0; i < n; i++)                if ((1 << i) & state) cur ^= num[i];            if (!mp.count(cur) || BitCount(mp[cur]) < BitCount(state)) mp[cur] = state;        }        int ans = 0;        for (int state = 0; state < (1 << n2); state++)        {            int cur = 0;            for (int i = 0; i < n2; i++) if (state & (1 << i)) cur ^= num[n1 + i];            if (mp.count(cur) && BitCount(ans) < BitCount(mp[cur]) + BitCount(state))                ans = (state << n1) ^ mp[cur];        }         bool first = true;        printf("%d\n", BitCount(ans));        for (i = 0; i < n; i++)            if ((1 << i) & ans)            {                if (first)                    printf("%d", i + 1), first = false;                else printf(" %d", i + 1);            }        puts("");    }    return 0;}
```
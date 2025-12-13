---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 128 - Software CRC
tags: []
layout: post
---

## 传送门

[UVa 128 - Software CRC](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=115&page=show_problem&problem=64)

## 题意

给出一个256进制的数(0~255), char的范围，在它的后面填上两位，使得能够被34942整除。

## 思路

设原来的数为k

把这个数转化成十进制，同时取模，这样就得到$k \mod 34942$的值$t$.  
因为右移了两位，所以那时候余数是$t*256*256 \mod 34942$，可知只要加上$34942 - t \mod 34942$就是缺的数。

## 代码


```c++
#include <bits/stdc++.h>
using namespace std;
#define LL long long
const char con[] = "0123456789ABCDEF";
 
int main()
{
    //freopen("input.txt", "r", stdin);
    char str[1100], rec[5];
    LL t = 0, g = 34943, ans;
    while (gets(str), str[0] != '#')
    {
        t = 0, ans = 0;
        for (int i = 0; str[i]; i++)
            t = (t * 256 + str[i]) % g;
        ans = (g - t * 65536 % g) % g;
        //printf("%d\n", ans);
        for (int i = 0; i < 4; i++)
        {
            rec[i] = ans % 16;
            ans /= 16;
        }
        printf("%c%c %c%c\n", con[rec[3]], con[rec[2]], con[rec[1]], con[rec[0]]);
    }
    return 0;
}
```
---
categories: Posts
date: 2014-08-01 00:00:00
title: USACO Section 1.2 - Palindromic Squares
tags: []
layout: post
---

## 题意

给出一个进制，求1 ~ 300以内十进制转换成这个进制是不是回文串，是的话输出。

## 思路

直接转换，倒着输出。回文串随便输。

## 代码


```c++
/*
ID: mycodeb1
LANG: C++
TASK: palsquare
*/
 
#include <bits/stdc++.h>
using namespace std;
const int WMAXN = 5000;
const char cstr[] = "0123456789ABCDEFGHIJ";
 
string str;
int base;
 
string Convert(int num)
{
    str.clear();
    int k = 0;
    while (num)
    {
        str += cstr[num % base];
        num /= base;
    }
    return str;
}
 
bool isOK(string s)
{
    int len = s.length();
    for (int i = 0, j = len - 1; i < j; i++, j--)
        if (s[i] != s[j])
            return false;
    return true;
}
 
int main()
{
    freopen("palsquare.in", "r", stdin);
    freopen("palsquare.out", "w", stdout);
    ios::sync_with_stdio(false);
 
    int i, j;
    scanf("%d", &base);
    for (i = 1; i <= 300; i++)
        if (isOK(Convert(i * i)))
        {
            Convert(i);
            reverse(str.begin(), str.end());
            cout << str << " ";
            Convert(i * i);
            cout << str << endl;
        }
    return 0;
}
```
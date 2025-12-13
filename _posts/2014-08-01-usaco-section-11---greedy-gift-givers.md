---
categories: Posts
date: 2014-08-01 00:00:00
title: USACO Section 1.1 - Greedy Gift Givers
tags: []
layout: post
---

## 题意

每人都来分钱，每个人有自己的选择，钱必须平均分，剩下来的还给自己，问最后人都剩多少钱

## 思路

这题写了三十分钟。。没脸见人了。不过好像又回到了刚开始做UVa字符串专题，也就是刚开始接触ACM时候。时间好快╰（￣▽￣）╭

用map记录，然后输出。因为要按照输入的顺序输出，想不到其他的方法，就又开了一个数组。。。

## 代码


```c++
/*
ID: mycodeb1
LANG: C++
TASK: gift1
*/
 
#include <bits/stdc++.h>
using namespace std;
 
map<string, int> mp;
map<string, int>::iterator it;
string ss[11];
 
void Solve(int money, int num, string curName)
{
    string name;
    int t = money / num;
    int tt = money % num;
    for (int i = 0; i < num; i++)
    {
        cin >> name;
        it = mp.find(name);
        it->second += t;
    }
    it = mp.find(curName);
    it->second = it->second - money + tt;
}
 
int main()
{
    //freopen("in.txt", "r", stdin);
    freopen("gift1.in", "r", stdin);
    freopen("gift1.out", "w", stdout);
    ios::sync_with_stdio(false);
 
    int i, j, n, money, num;
    cin >> n;
    string str;
    for (i = 0; i < n; i++)
    {
        cin >> str;
        ss[i] = str;
        mp[str] = 0;
    }
    for (i = 0; i < n; i++)
    {
        cin >> str;     //current giver;
        cin >> money >> num;
        if (!num || !money)
            continue;
        Solve(money, num, str);
    }
    for (i = 0; i < n; i++)
    {
        cout << ss[i] << " ";
        it = mp.find(ss[i]);
        cout << it->second << endl;
    }
    return 0;
}
```
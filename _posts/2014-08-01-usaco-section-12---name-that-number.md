---
categories: Posts
date: 2014-08-01 00:00:00
title: USACO Section 1.2 - Name That Number
tags: []
layout: post
---

#  [USACO Section 1.2 - Name That Number](/2014/08/USACO-1_2-namenum/ "USACO Section 1.2 - Name That Number")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Aug 13 2014 22:19

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

给一个数字，找出字典中符合的单词。

## 思路

直接扫描字典，如果有相同的就输出。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243

| 
    
    
    /*ID: mycodeb1LANG: C++TASK: namenum*/ #include <bits/stdc++.h>using namespace std;const int WMAXN = 5000;const char cstr[] = "2223334445556667077888999"; vector<string> key, word; int main(){    //ifstream fin("input.txt");    ifstream fin("namenum.in");    ifstream fdicin("dict.txt");    ofstream fout("namenum.out");    //ios::sync_with_stdio(false);     int i, j;    string temp;    while (fdicin >> temp)    {        word.push_back(temp);        string t;        for (j = 0; j < temp.length(); j++)            t += cstr[temp[j] - 'A'];        key.push_back(t);    }    fin >> temp;    int flag = 0;    for (i = 0; i < key.size(); i++)        if (temp == key[i])        {            flag = 1;            fout << word[i] << endl;        }    if (flag == 0)        fout << "NONE" << endl;    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - USACO](/tags/Online-Judge-USACO/)[Foundation - Strings](/tags/Foundation-Strings/)

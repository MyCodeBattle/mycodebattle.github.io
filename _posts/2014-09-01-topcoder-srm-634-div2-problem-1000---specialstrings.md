---
categories: Posts
date: 2014-09-01 00:00:00
title: TopCoder SRM 634 Div2 Problem 1000 - SpecialStrings
tags: []
layout: post
---

## 题意

给一个字符串，求满足条件的下一个字典序的字符串。

条件：字符串首位和第i位的字符串的字典序比和i+1到末尾的字符串小

## 思路

从后面往前搜索。碰到第一个0，就把它变成1，然后检查之后的字符，看变为0能否符合条件。

第一个字符不能为1

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142

| ```c++
#include <cstdio>#include <cmath>#include <cstring>#include <ctime>#include <iostream>#include <algorithm>#include <set>#include <vector>#include <sstream>#include <typeinfo>#include <fstream> using namespace std; class SpecialStrings {    public:    bool Check(const string &str)    {        for (int i = 1; i < str.size(); i++)            if (str.substr(0, i) >= str.substr(i)) return false;        return true;    }     string findNext(string cur) {        int len = (int)cur.size();        if (len == 1 && cur[0] == '0') return "1";        int i, j;        for (i = len - 1; i >= 0; i--)        {            if (cur[i] == '1') continue;            if (i == 0) return "";            cur[i] = '1';            for (j = i + 1; j < len; j++)            {                cur[j] = '0';                if (!Check(cur)) cur[j] = '1';            }            return cur;        }        return "";    }};
```
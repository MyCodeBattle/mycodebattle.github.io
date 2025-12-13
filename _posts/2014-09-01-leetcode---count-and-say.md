---
categories: Posts
date: 2014-09-01 00:00:00
title: LeetCode - Count and Say
tags: []
layout: post
---

## 题意

给一个字符串，他的下一个序列是每个连续的数字的个数+当前数字。求第N个序列。

## 思路

直接用string了。

## 代码
    
    
    1234567891011121314151617181920212223

| ```c++
class Solution {public:    string countAndSay(int n)    {        string str = "1";        for (int cnt = 2; cnt <= n; cnt++)        {            string curStr;            for (string::iterator it = str.begin(); it != str.end(); )            {                string::iterator ed = it;                while (ed != str.end() && *ed == *it) ed++;                int pre = count(it, ed, *it);                stringstream sstr;                sstr << pre;                curStr += sstr.str() + *it;                it = ed;            }            str = curStr;        }        return str;    }};
```
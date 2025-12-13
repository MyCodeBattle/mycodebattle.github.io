---
categories: Posts
date: 2014-09-01 00:00:00
title: LeetCode - Reverse Words in a String
tags: []
layout: post
---

#  [LeetCode - Reverse Words in a String](/2014/09/leetcode-reverse-string/ "LeetCode - Reverse Words in a String")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 13 2014 13:48

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

要求逆序输出一个字符串中的单词。

## 思路

我用了stack来处理。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536

| 
    
    
    class Solution {    bool first;public:    void reverseWords(string &s) {        first = true;        int len = s.size();        string str;        for (int i = 0; i < len; i++)        {            if (!isspace(s[i])) str += s[i];            else if (!str.empty())            {                stk.push(str);                str.clear();            }        }        if (!str.empty()) stk.push(str);        s.clear();        while (!stk.empty())        {            if (first)            {                string tmp = stk.top(); stk.pop();                s += tmp;                first = false;            }            else            {                string tmp = stk.top(); stk.pop();                s += " " + tmp;            }        }    }private:    stack<string> stk;};  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - LeetCode](/tags/Online-Judge-LeetCode/)[Foundation - Strings](/tags/Foundation-Strings/)

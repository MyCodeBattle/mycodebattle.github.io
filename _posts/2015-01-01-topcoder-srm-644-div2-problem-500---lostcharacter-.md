---
categories: Posts
date: 2015-01-01 00:00:00
title: TopCoder SRM 644 Div2 Problem 500 - LostCharacter (贪心)
tags: []
layout: post
---

#  [TopCoder SRM 644 Div2 Problem 500 - LostCharacter (贪心)](/2015/01/topcoder-srm-644-div2-500/ "TopCoder SRM 644 Div2 Problem 500 - LostCharacter \(贪心\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jan 3 2015 15:04

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

给出一些字符串数组，可能包含有？。现在要求输出每个字符串在按字典序排序后的最靠前的位置。

## 思路

一开始看不懂题目，以为是要一起考虑的。原来是每个字符串分开考虑。

因为数据量很小，所以直接无脑暴力。

对于每个字符串，把它里面的？都改成a，然后把其他的字符串里的？都改成z，这样就能使位置尽量靠前。

顺便吐槽一下，连了一个上午加半个下午的TC，终于给连上了。

## 代码
    
    
    12345678910111213141516171819202122232425

| 
    
    
    class LostCharacter {    public:    vector<int> getmins(vector<string> str) {        vector<int> ans;        vector<string> tmp;        tmp = str;        if (str.empty()) return ans;        for (int i = 0; i < str.size(); i++)        {            string target = str[i];            for (int j = 0; j < target.size(); j++)                if (target[j] == '?') target[j] = str[i][j] = 'a';            for (int j = 0; j < str.size(); j++)            {                if (i == j) continue;                for (int k = 0; k < str[j].size(); k++)                    if (str[j][k] == '?') str[j][k] = 'z';            }            sort(str.begin(), str.end());            ans.push_back(lower_bound(str.begin(), str.end(), target) - str.begin());            str = tmp;        }        return ans;    }};  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - TopCoder](/tags/Online-Judge-TopCoder/)[Foundation - Greedy](/tags/Foundation-Greedy/)

---
categories: Posts
date: 2014-07-01 00:00:00
title: HDU 1113 - Word Amalgamation
tags: []
layout: post
---

#  [HDU 1113 - Word Amalgamation](/2014/07/HDU-1113/ "HDU 1113 - Word Amalgamation")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jul 30 2014 19:43

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[HDU 1113 - Word Amalgamation](http://acm.hdu.edu.cn/showproblem.php?pid=1113)

## 题意

先给出一个字典，然后给出几组词，如果词可以通过重新排列组成字典里面的词，输出字典里的词。

## 思路

一开始想麻烦了，开了两个map，一个用来记录sort后的词，把每个sort后相同的词都归为一组。

如果后来输入的词存在，输出那一组的字典词。

其实可以直接用string判断是否存在的，不用另外编号

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657

| 
    
    
    #include <cstdio>#include <map>#include <cstring>#include <iostream>#include <string>#include <cctype>#include <algorithm>using namespace std; map<string, int> mp;map<string, int> ans; string str; int main(){    //freopen("in.txt", "r", stdin);    int i, j, cnt = 1;    while (cin >> str)    {        if (str == "XXXXXX")            break;        string temp = str;        for (i = 0; i < str.size(); i++)            temp[i] = tolower(str[i]);        sort(temp.begin(), temp.end());        if (mp.count(temp))            ans.insert(make_pair(str, mp[temp]));        else        {            mp[temp] = cnt++;            ans.insert(make_pair(str, mp[temp]));        }    }    while (cin >> str)    {        if (str == "XXXXXX")            break;        string temp = str;        for (i = 0; i < str.size(); i++)            temp[i] = tolower(str[i]);        sort(temp.begin(), temp.end());        if (mp.count(temp))        {            for (map<string, int>::iterator it = ans.begin(); it != ans.end(); it++)                if (it->second == mp[temp])                    cout << it->first << endl;            printf("******\n");        }        else        {            printf("NOT A VALID WORD\n");            printf("******\n");        }    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Foundation - Strings](/tags/Foundation-Strings/)[Online Judge - HDU](/tags/Online-Judge-HDU/)

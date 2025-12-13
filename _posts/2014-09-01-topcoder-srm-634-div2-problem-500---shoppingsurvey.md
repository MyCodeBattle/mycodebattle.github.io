---
categories: Posts
date: 2014-09-01 00:00:00
title: TopCoder SRM 634 Div2 Problem 500 - ShoppingSurvey
tags: []
layout: post
---

#  [TopCoder SRM 634 Div2 Problem 500 - ShoppingSurvey](/2014/09/topcoder-srm-634-div2-500/ "TopCoder SRM 634 Div2 Problem 500 - ShoppingSurvey")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 27 2014 16:22

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

有N个人，现在知道每个商品被买了ki次，求最少的，买了全部商品的人数。

## 思路

要尽量不让一个人买完商品，也就是尽量把商品卖给不同的人。

我用num[i]，表示第i个人买的商品数，然后买就行。

比如说5个人，商品为3,3,4。

第一个商品卖给1,2,3

第二个卖给4,5,1

第三个卖给2,3,4,5。

这样就没人买到全部的商品了。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334

| 
    
    
    #include <cstdio>#include <cmath>#include <cstring>#include <ctime>#include <iostream>#include <algorithm>#include <set>#include <vector>#include <sstream>#include <typeinfo>#include <fstream> using namespace std; class ShoppingSurveyDiv2 {    int num[110];    public:    int minValue(int N, vector<int> s) {        int cnt = 0;        int len = s.size(), j = 1;        for (int i = 0; i < len; i++)        {            while (s[i]--)            {                num[j]++;                j++;                if (j > N) j = 1;            }        }        for (int i = 1; i <= N; i++)            if (num[i] >= len) cnt++;        return cnt;    }};  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - TopCoder](/tags/Online-Judge-TopCoder/)

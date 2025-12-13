---
categories: Posts
date: 2014-09-01 00:00:00
title: TopCoder SRM 634 Div2 Problem 500 - ShoppingSurvey
tags: []
layout: post
---

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


```c++
#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <sstream>
#include <typeinfo>
#include <fstream>
 
using namespace std;
 
class ShoppingSurveyDiv2 {
    int num[110];
    public:
    int minValue(int N, vector<int> s) {
        int cnt = 0;
        int len = s.size(), j = 1;
        for (int i = 0; i < len; i++)
        {
            while (s[i]--)
            {
                num[j]++;
                j++;
                if (j > N) j = 1;
            }
        }
        for (int i = 1; i <= N; i++)
            if (num[i] >= len) cnt++;
        return cnt;
    }
};
```
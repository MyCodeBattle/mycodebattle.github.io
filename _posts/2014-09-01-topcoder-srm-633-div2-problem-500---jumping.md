---
categories: Posts
date: 2014-09-01 00:00:00
title: TopCoder SRM 633 Div2 Problem 500 - Jumping
tags: []
layout: post
---

## 题意

有个青蛙，给出目标点和跳的距离，求能否到达。

## 思路

其实能否跳到和跳的顺序是无关的。

考虑不能跳到的情况

  1. 距离之和小于到终点的距离。  
不用说，就算一直跳直线也够不到。

  2. 最大一步的距离比前面的距离都要大。  
这样的话，就算一直朝反方向跳，最后一步也会跳出头。


其余情况都可以跳到。

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
#define LL long long
 
using namespace std;
 
class Jumping {
public:
    string ableToGet(int x, int y, vector<int> jumpLengths) {
        sort(jumpLengths.begin(), jumpLengths.end());
        if (jumpLengths.size() == 1)
        {
            int cur = jumpLengths[0];
            if (cur * cur != x * x + y * y) return "Not able";
            else return "Able";
        }
        else
        {
            LL dis = 0, judgeDis = 0;
            for (int i = 0; i < jumpLengths.size(); i++)
            {
                dis += jumpLengths[i];
                if (i == jumpLengths.size() - 2) judgeDis = dis;
            }
            int cur = jumpLengths.back();
            if (dis * dis >= x * x + y * y)
            {
                if (cur > judgeDis)
                {
                    if ((cur - judgeDis) * (cur - judgeDis) <= x * x + y * y)
                        return "Able";
                    else return "Not able";
                }
                return "Able";
            }
            else return "Not able";
        }
    }
};
 
// Powered by Greed 2.0-RC
```
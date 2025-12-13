---
categories: Posts
date: 2015-02-01 00:00:00
title: TopCoder SRM 649 Div2 Problem 1000 - XorSequenceEasy (思维)
tags: []
layout: post
---

## 题意

给一串序列，现在要求选一个B，让序列的每一个数都异或B。

现在要求输出新序列中最大的顺序对。

## 思路

观察两个数  
$7(0111)_2, 5(0101)_2$

能且只能异或第一位，使他们的大小改变。

所以我们就可以30位全部异或过去，如果能使顺序对增加的，B那个位就是1.  
然后统计。

因为数据量小，直接暴力统计顺序对了。

## 代码
    
    
    12345678910111213141516171819202122232425

| ```c++
class XorSequenceEasy {public:    int Check(const vector<int> &arr)    {        int cnt = 0;        for (int i = 0; i < SZ(arr); i++)            for (int j = i+1; j < SZ(arr); j++)                if (arr[i] < arr[j]) cnt++;        return cnt;    }     int getmax(vector<int> A, int N) {        int maxNum = 0, ori = Check(A), ans;        for (int i = 0; i < 30; i++)        {            int tmp = (1<<i);            //if ((ans|tmp) > N) break;            vector<int> B;            for (int j = 0; j < SZ(A); j++) B.PB(A[j]^tmp);            int comp = Check(B);            maxNum += max(0, comp - ori);        }        return maxNum + ori;    }};
```
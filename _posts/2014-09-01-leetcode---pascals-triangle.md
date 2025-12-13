---
categories: Posts
date: 2014-09-01 00:00:00
title: LeetCode - Pascal's Triangle
tags: []
layout: post
---

#  [LeetCode - Pascal's Triangle](/2014/09/leetcode-triangle/ "LeetCode - Pascal's Triangle")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 13 2014 16:46

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

输出杨辉三角

## 思路

照着输就行。

## 代码
    
    
    1234567891011121314151617181920212223

| 
    
    
    class Solution {    vector<vector<int> >vve;public:    vector<vector<int> > generate(int numRows) {        for (int i = 1; i <= numRows; i++)        {            vector<int> cur;            for (int j = 0; j < i; j++)            {                if (j == 0) cur.push_back(1);                else                {                    if (j != i - 1)                        cur.push_back(vve[i - 2][j] + vve[i - 2][j - 1]);                    else                        cur.push_back(1);                }            }            vve.push_back(cur);        }        return vve;    }};  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - LeetCode](/tags/Online-Judge-LeetCode/)[Foundation - Others](/tags/Foundation-Others/)

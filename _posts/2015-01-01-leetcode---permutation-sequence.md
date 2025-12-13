---
categories: Posts
date: 2015-01-01 00:00:00
title: LeetCode - Permutation Sequence
tags: []
layout: post
---

#  [LeetCode - Permutation Sequence](/2015/01/leetcode-permutation-sequence/ "LeetCode - Permutation Sequence")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jan 17 2015 23:50

**Contents**

  1. 1. 思路
  2. 2. 代码

## 思路

推导一下，先推出第一个，然后第二个，以此类推

## 代码
    
    
    123456789101112131415161718

| 
    
    
    class Solution {public:    string getPermutation(int n, int k) {        vector<int> num, fac;        for (int i = 0; i < n; i++) num.push_back(i + 1);        fac.push_back(1);        for (int i = 1; i < n; i++) fac.push_back(fac[i - 1] * i);        string ans;        for (int i = n - 1; i >= 0; i--)        {            int pos = (k - 1) / fac[i];            ans += (num[pos] + '0');            num.erase(num.begin() + pos);            k -= pos * fac[i];        }        return ans;    }};  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - LeetCode](/tags/Online-Judge-LeetCode/)

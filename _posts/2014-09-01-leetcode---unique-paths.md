---
categories: Posts
date: 2014-09-01 00:00:00
title: LeetCode - Unique Paths
tags: []
layout: post
---

#  [LeetCode - Unique Paths](/2014/09/leetcode-unique-path/ "LeetCode - Unique Paths")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 13 2014 21:38

**Contents**

  1. 1. 思路
  2. 2. 代码

## 思路

只能从上边或者左边走过来。

感觉LeetCode是偷懒的好地方。。

## 代码
    
    
    1234567891011121314

| 
    
    
    class Solution {    int dp[110][110];     public:    int uniquePaths(int m, int n) {        memset(dp, 0, sizeof dp);        for (int i = 1; i <= n; i++)            dp[1][i] = 1;        for (int i = 2; i <= m; i++)            for (int j = 1; j <= n; j++)                dp[i][j] = dp[i][j - 1] + dp[i - 1][j];        return dp[m][n];    }};  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - LeetCode](/tags/Online-Judge-LeetCode/)

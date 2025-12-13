---
categories: Posts
date: 2014-09-01 00:00:00
title: LeetCode - Remove Duplicates from Sorted Array
tags: []
layout: post
---

#  [LeetCode - Remove Duplicates from Sorted Array](/2014/09/leetcode-remove-duplicates-from-sorted-array/ "LeetCode - Remove Duplicates from Sorted Array")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 21 2014 18:20

**Contents**

  1. 1. 思路
  2. 2. 代码

## 思路

用两个数，一个表示当前的位置，另一个走完整个数组，如果数不同就替换掉

## 代码
    
    
    12345678910

| 
    
    
    class Solution {public:    int removeDuplicates(int a[], int n) {        if (n <= 1) return n;        int pivot = 0, j = 1;        for (j = 1; j < n; j++)            if (a[j] != a[pivot]) a[++pivot] = a[j];        return pivot + 1;    }};  
  
---|---  
  
来偷个懒呗
    
    
    123456

| 
    
    
    class Solution {public:	int removeDuplicates(int a[], int n) {		return unique(a, a + n) - a;	}};  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - LeetCode](/tags/Online-Judge-LeetCode/)

---
categories: Posts
date: 2014-09-01 00:00:00
title: LeetCode - Partition List
tags: []
layout: post
---

#  [LeetCode - Partition List](/2014/09/leetcode-partition-list/ "LeetCode - Partition List")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 16 2014 14:53

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

传入一个链表的头指针和一个数，把小于这个数的都放前面，大于的位置不变接着放后面。

## 思路

用了非常2的方法。

开两个队列，分别存放大于的和小于的，再开一个队列一个个存放指针，最后拿出来接上去。。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233

| 
    
    
    class Solution {    queue<int> qsml, qbig;    queue<ListNode *> p;public:    ListNode *partition(ListNode *head, int x) {        if (!head) return head;        do        {            p.push(head);            if (head->val >= x) qbig.push(head->val);            else qsml.push(head->val);            head = head->next;        }while (head);        while (!p.empty())        {            ListNode *cur = p.front(); p.pop();            if (!head)                head = cur;            if (!qsml.empty())            {                cur->val = qsml.front();                qsml.pop();            }            else            {                cur->val = qbig.front();                qbig.pop();            }            if (!p.empty()) cur->next = p.front();        }        return head;    }};  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - LeetCode](/tags/Online-Judge-LeetCode/)[Data Structure - Foundation](/tags/Data-Structure-Foundation/)

---
categories: Posts
date: 2014-09-16 00:00:00
title: LeetCode - Partition List
tags: []
layout: post
---

## 题意

传入一个链表的头指针和一个数，把小于这个数的都放前面，大于的位置不变接着放后面。

## 思路

用了非常2的方法。

开两个队列，分别存放大于的和小于的，再开一个队列一个个存放指针，最后拿出来接上去。。

## 代码


```c++
class Solution {
    queue<int> qsml, qbig;
    queue<ListNode *> p;
public:
    ListNode *partition(ListNode *head, int x) {
        if (!head) return head;
        do
        {
            p.push(head);
            if (head->val >= x) qbig.push(head->val);
            else qsml.push(head->val);
            head = head->next;
        }while (head);
        while (!p.empty())
        {
            ListNode *cur = p.front(); p.pop();
            if (!head)
                head = cur;
            if (!qsml.empty())
            {
                cur->val = qsml.front();
                qsml.pop();
            }
            else
            {
                cur->val = qbig.front();
                qbig.pop();
            }
            if (!p.empty()) cur->next = p.front();
        }
        return head;
    }
};
```
---
title: Redis 源码阅读 - 链表
layout: post
date: 2016-04-11
categories: Redis
---

一般通过一个 `adlist.h/list`来保存一个链表。

```
typedef struct list {
    listNode *head;
    listNode *tail;
    unsigned long len;

    //节点值复制函数
    void* (*dup) (void *ptr);

    //节点值释放函数
    void (*free) (void *ptr);

    //节点值对比函数
    void (*match) (void *ptr, void *key);
} list;
```

它的特性有：

- 双端
- 无环
- O(1) 访问表头和表尾
- O(1) 获取长度
- 多态。使用 `void*`来保存节点值。

没啦。。

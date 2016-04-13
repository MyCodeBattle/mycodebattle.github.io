---
title: Redis 源码阅读 - Dict
layout: post
date: 2016-04-13
categories: Redis
---

先来看下哈希表的结构。

```
typedef struct dictht {
    dictEntry **table;
    unsigned long size;
    unsigned long sizemask; //总等于size - 1
    unsigned long used;
} dictht;
```


```
typedef struct dictEntry {
    void *key;
    union {
        void *val;
        uint64_t u64;
        int64_t s64;
        double d;
    } v;
    struct dictEntry *next;
} dictEntry;
```

总的来说，一个字典保存着一个数组，里面的元素指向`dictEntry`。
value 可以是一个指针，或者64位的 uint, int 和 double。

## 字典

```
typedef struct dict {
    dictType *type;
    void *privdata;
    dictht ht[2];
    long rehashidx; /* rehashing not in progress if rehashidx == -1 */
    int iterators; /* number of iterators currently running */
} dict;
```

- type 属性是一个指向 dictType 的指针，每个 dictType 结构保存了一簇用于操作特定类型键值对的函数， Redis 会为用途不同的字典设置不同类型的特定函数。
- privdata 树形保存了需要传给那些特定函数的可选参数。
- ht 包括了两个哈希表，是用来在 rehash 的时候代替的。
- rehashidx 记录了当前哈希的进度，如果没有则是 -1。

```
typedef struct dictType {
    unsigned int (*hashFunction)(const void *key);
    void *(*keyDup)(void *privdata, const void *key);
    void *(*valDup)(void *privdata, const void *obj);
    int (*keyCompare)(void *privdata, const void *key1, const void *key2);
    void (*keyDestructor)(void *privdata, void *key);
    void (*valDestructor)(void *privdata, void *obj);
} dictType;
```

## 哈希算法

具体的和 Java 里的 HashMap 差不多，都是计算一下哈希值，然后逻辑与一下 sizeMask，然后拉链一下。
这里使用的是`MurmurHash2`。

## rehash

当超过负载时(默认为1)，进行 rehash。
过程就是把 ht[0] 的东西转移到 ht[1] 上，大小变成两倍。
如果是收缩的话，大小是最接近的 2 的幂次。

当所有键值都 rehash 完之后，把 ht[1] 变成 ht[0]。
rehash 是分步的，不是一次干完，用一个`rehashidx`来记录 rehash 到哪里了。

在 rehash 的时候，比如说原本查找的操作，需要在第一个表里找，如果找不到还要去第二个表里。以此类推。



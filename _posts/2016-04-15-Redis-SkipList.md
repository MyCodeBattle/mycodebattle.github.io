---
title: Redis 源码阅读 - 跳表
layout: post
date: 2016-04-15
categories: Redis
---

先来看看跳表结点的定义：

```
typedef struct zskiplistNode {
    robj *obj;
    double score;
    struct zskiplistNode *backward;
    struct zskiplistLevel {
        struct zskiplistNode *forward;
        unsigned int span;
    } level[];
} zskiplistNode;
```

- score，跳表按照 score 排序，从小到大。如果相同的按 obj 对应的 sds 字典序大小排序。
- backward，指向先前结点的指针。
- span，记录两个结点之间的距离，可以用来计算 rank。

再来看看跳表的定义：

```
typedef struct zskiplist {
    struct zskiplistNode *header, *tail;
    unsigned long length;
    int level;
} zskiplist;
```

剩下就没什么好说了。
跳表的复杂度计算有点神奇，看论文看不懂 Orz.

---

这书的作者也是挺扯蛋的，就把源代码里英文部分翻译一下，没注释的干脆不管了，一点都不负责。
这我也会啊！



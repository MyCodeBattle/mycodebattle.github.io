---
title: Redis 源码阅读 - 对象
layout: post
date: 2016-05-24
categories: Redis
---

<s>悲伤的话题。</s>

Redis 使用键值对来表示数据库中的键和值。当我们在 Redis 的数据库中新建一个键值对时，至少会创建两个对象。

Redis 中的每个对象都由一个 redisObject 结构表示。

```
typedef struct redisObject {
    unsigned type:4;
    unsigned encoding:4;
    unsigned lru:REDIS_LRU_BITS; /* lru time (relative to server.lruclock) */
    int refcount;
    void *ptr;
} robj;
```

## 类型

对象的 type 属性记录了对象的类型。

|类型常量|对象名称|
|---|---|
|REDIS\_STRING| 字符串对象|
|REDIS\_LIST|列表对象

以此类推，还有 HASH | SET | ZSET。

键总是一个字符串对象，而值不一定。

当输入 type 命令时，得到的是值对象的类型。

## 编码和底层实现

`ptr`指针指向对象的底层实现数据结构，这些数据结构由对象的`encoding`属性决定。

|编码常量|对应的数据结构|
|---|---|
|INT| long 类型的参数|
|EMBSTR| embstr 编码的简单动态字符串|
|RAW | 简单动态字符串|
|LINKEDLIST| 双端链表|
|ZIPLIST| 压缩列表|
|INTSET| 整数集合|
|SKIPLIST| 跳表和字典|

每种对象至少可以使用两种不同的编码，使用`object encoding`可以查看对象的编码。


# 字符串对象

如果一个字符串保存的是整数值，并且整数值可以用 long 类型来表示，那么 encoding 就是 int.

如果保存的是一个字符串，并且长度大于 32 字节，那么就使用 SDS，编码为 raw, 否则使用 embstr。

embstr 和 sds 的区别是 embstr 通过一次空间分配，使得一块区域里依次包含 redisObject 和 sdshdr，能充分利用缓存。 sds 需要分配两次空间，释放空间也要两次。

当字符串对象里存的是浮点数时，执行加某个数时，程序会先将字符串值换成浮点数，相加之后再变成字符串。

## 编码的转换

假设现在的编码是 int，append 了一个字母，这时候就被转换成了 raw。
另外，因为 embstr 没有响应的修改程序，所以它实际上是只读的，对它的修改都会变成对 sds 的修改。

----



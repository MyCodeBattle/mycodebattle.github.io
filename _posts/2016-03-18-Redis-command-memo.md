---
title: Redis 常用命令备忘
layout: post
date: 2016-03-18
categories: Memorandum
---

# SET

Time complexity: O(1)

`SET key value [EX seconds] [PX milliseconds] [NX|XX]`

## Options

Starting with Redis 2.6.12 SET supports a set of options that modify its behavior:
- EX seconds -- Set the specified expire time, in seconds.
- PX milliseconds -- Set the specified expire time, in milliseconds.
- NX -- Only set the key if it does not already exist.
- XX -- Only set the key if it already exist.

## Return value

如果正确执行返回`OK`，否则返回`NULL`。

# keys *

查找 key 的信息。

# flushadb

删除当前数据库的信息。

# flushall

删除全部数据库里的信息。

#select

默认 Redis 开了16个数据库。我们可以用 `select 2`来切换不同的数据库。



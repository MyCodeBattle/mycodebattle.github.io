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


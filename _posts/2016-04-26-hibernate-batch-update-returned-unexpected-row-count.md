---
title: Hibernate 一对一更新时出现 Batch update returned unexpected row count from ... 的解决办法
layout: post
date: 2016-04-26
categories: Hibernate
---

> Batch update returned unexpected row count from update [0]; actual row count: 0; expected: 1

这个错误的原因在于主键增长的方式的冲突。

比如说这次我的主键设置了'foreign'，然而我又在代码里 set 了一个值，所以就出现这个错误了。把那句 set 的语句去掉即可。





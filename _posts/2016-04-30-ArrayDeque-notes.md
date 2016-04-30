---
title: ArrayDeque 和 LinkedList
layout: post
date: 2016-04-30
categories: Java
---

昨天搜了一下很久之前就想的一个问题：为什么 Java 里的 Queue 使用 LinkedList 实现？

虽然链表这一结构适合队列的先进先出，不过大量 new 和 删除结点引发的 GC 代价也是很高的。

我粗略地测试了一下 1e7 左右的 push 和 poll，使用 ArrayDeque 是使用 LinkedList 的 1/10，虽然这样的测试不太科学，不过还是可以看出使用循环队列比链表的效率要高。



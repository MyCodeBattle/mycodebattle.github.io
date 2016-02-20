---
categories: Article
date: 2015-10-31 23:07:15
title: Python 'ascii' codec can't decode byte ... ordinal not in range(128)
tags: 
layout: post
---

Python内部的编码是Unicode，在读入中文的时候用的是utf-8，所以在写入的时候出了点问题。

在传入文本的时候写成`string.decode()`就行了。
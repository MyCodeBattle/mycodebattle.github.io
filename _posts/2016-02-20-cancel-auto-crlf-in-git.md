---
categories: Article
date: 2016-01-10 16:08:04
title: 取消Git对LF的自动替换 
tags: 
layout: post
---

在Windows环境下，如果使用LF，Git会自动替换成CRLF，那么用Vim打开时就有一个^M出现了。

这时候

`git config --global core.autocrlf false`

即可。

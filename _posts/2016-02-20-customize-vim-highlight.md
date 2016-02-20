---
categories: Article
date: 2016-01-28 20:36:33
title: 自定义Vim语法高亮
tags: Vim
layout: post
---

最近在写Java的时候，很多内置类和方法都亮不起来。
这种情况可以手动加一下关键字。

我们先找到`/syntax/java.vim`，在这个文件里定义关键字。

`syn keyword javaBuiltinClass Map Set`

这样我们就定义了个`javaBuiltinClass`种类的高亮，后面跟的是这个种类的关键词。

然后我们在自己的配色方案里`hi javaBuiltinClass #66D9EF`，这样就亮起来了。

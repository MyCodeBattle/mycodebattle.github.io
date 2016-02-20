---
categories: Article
date: 2015-12-09 16:27:35
title: IntelliJ IDEA的jsp中request等对象无法被解析的解决办法
tags: 
layout: post
---

用IDEA写jsp时，输入request然后点一下，不能弹出所有的方法。

是没有导入依赖包的缘故。

（Ctrl + Alt + Shift + S） → Libraries → 绿色的加号 → 到tomcat\lib目录下。

然而网上的人都说导入servlet-api.jar和jsp-api.jar，但是这样以后还是不能解析。
试了很久才发现，其实还要导入tomcat-api.jar。。。

问题解决╮(╯▽╰)╭
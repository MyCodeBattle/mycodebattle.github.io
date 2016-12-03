---
title: 一次使用 git bisect 查找项目中错误的经历
layout: post
date: 2016-12-03
categories: Git
---

今天在写双十二活动的时候，把系统发到了测试分支准备测试。

然后我无意间注册了个用户，发现日志竟然报错了！而且报的是一个非常蛋疼的错误

 > 2016-12-03 20:12:35,146 ERROR [c8c20c33f73d4595acdf4ea818b265b6][DubboServerHandler-120.26.100.234:33013-thread-5] c.m.s.c.BusinessEventHandler -  发放异常！
java.lang.ArrayIndexOutOfBoundsException: 0
	at com.miz.sinnis.core.BusinessEventHandler.isTypeMatched(BusinessEventHandler.java:83) [sinnis-project-service-logic-0.0.1-SNAPSHOT.jar:na]

要知道这个系统的开发是非常符合开闭原则的，每次只增加新的代码，完全不会去动老的代码。而且这个错误的地方是一个分发器，从这个系统建立之初就存在并且没变动过的东西。这就非常尴尬了（doge

然后我方了，赶紧跑到生产环境的分支测了一发，还好是正常的。那么原因就可以确定为我这个版本提交的代码出了问题。

但是这一个版本我有好几十个提交，怎么办呢。然后我就瞬间想到`git bisect`这个东西。没想到我有用上它的一天。

最初是在`Githug`上知道这个功能的。然后我百度了一下用法就开始搞了。

知道怎么搞就方便了。首先我定了当前版本为`bad`，去前面找了一个好的版本为`good`，几次之后就定位到了出错的版本！

最终的原因是因为这个版本里我加了事务，然后`Spring`自动实现了AOP，对分发器造成了影响。

最后的感想是多了解东西是非常有必要的，就算只是知道也可以，轮到用的时候去找资料就行了，不然比如这次我就没办法定位到底是哪个版本出了问题。到时候只能一个一个试过去，可怕。

以上。

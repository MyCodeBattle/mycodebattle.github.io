---
title: Ubuntu 下开启 MySQL 的远程连接
layout: post
date: 2017-01-30
categories: 
---

今天搞了一下服务器，发现服务器上的 MySQL 远程一直连接不上。查了一堆资料发现是配置的原因。

`/etc/my.cnf`下中，有个`bind-address`，默认是打开的，意思是只有下面地址才可以远程连接，注释掉就OK了。

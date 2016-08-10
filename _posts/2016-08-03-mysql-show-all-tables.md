---
title: MySQL 显示全部数据库的全部表的方法
layout: post
date: 2016-08-03
categories: MySQL
---

`select table_name from information_schema.tables`

如果要查看是哪个数据库里的话

`select table_schema from information_schema.tables where table_name = 'act_givebonus';`



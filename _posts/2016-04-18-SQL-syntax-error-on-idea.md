---
title: IntelliJ IDEA 中 MySQL 出现 [42000][1064] 错误的解决办法
layout: post
date: 2016-04-18
categories: 
---

在用 IDEA 自带的 Database 工具进行 SQL 语句查询的时候出现了这么一个错误：

```
[2016-04-18 12:07:46] [42000][1064] You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'OPTION SQL_SELECT_LIMIT=502' at line 1
[2016-04-18 12:07:46] [42000][1064] You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'OPTION SQL_SELECT_LIMIT=DEFAULT' at line 1
```

原因是 IDEA 自动下载的 JDBC 驱动太旧了，需要最新的驱动。
换成 5.1.38 的问题解决。



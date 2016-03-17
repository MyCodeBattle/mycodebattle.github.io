---
title: IDEA 部署 Tomcat 时提示 Error during artifact deployment 的解决办法
layout: post
date: 2016-03-13
categories: 
---

今天搭第一个 Struts 2 的时候发现不能部署，提示`Error during artifact deployment`。

这时候打开 Project Structure -> Artifacts
在右边的`output layout`下的`lib`包中导入 structs 包即可。
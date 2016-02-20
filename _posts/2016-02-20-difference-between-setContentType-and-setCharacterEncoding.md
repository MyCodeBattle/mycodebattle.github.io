---
categories: Article
date: 2015-12-15 18:50:13
title: response对象中setContentType和setCharacterEncoding方法的不同
tags: 
layout: post
---

在Servlet中用`response.setContType("html/text;charset=utf-8")`和`response.setCharacterEncoding("utf-8")`，后者乱码前者正常显示。

两者指定HTTP响应的编码，然而前者还指定了浏览器显示的编码。


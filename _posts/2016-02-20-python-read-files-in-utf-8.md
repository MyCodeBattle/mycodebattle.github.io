---
categories: Article
date: 2015-11-05 23:18:01
title: Python 2.7使用utf-8读入文件
tags: 
layout: post
---

```python
import codecs
f = codecs.open(filename, 'r', 'utf-8')
```
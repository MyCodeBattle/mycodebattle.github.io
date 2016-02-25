---
title: Java Concurrency In Practice 笔记
layout: post
date: 2016-02-22
categories: Java Notes
---

我就想看看我能写多久。

#Chapter2. Thread Safety

##线程安全

当变量都存在线程自身的栈的时候，这个对象是线程安全的，就像这样。

```
@ThreadSafe
public class statelesFactorizer implements Servlet {
    public void service(ServletRequest req, ServletResponse resp) {
        BigInteger i = extractFromRequest(req);
        BigInteger[] factors = factor(i);
        encodeIntoResponse(resp, factors);
    }
}
```
##原子性

很典型的自增操作，是非原子的。

##竞态条件

最常见的一种竞态条件是检查再运行(check-then-act)。

比如说你已经检查到X文件不存在，然后基于这个判断做出下一步动作。
然而在这期间可能状态已经被改变（有人创建了文件X），那么将会引发错误。




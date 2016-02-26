---
title: Java Concurrency In Practice 笔记
layout: post
date: 2016-02-22
categories: Java Notes
---

我就想看看我能写多久。


# Chapter2. Thread Safety

## 线程安全

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
## 原子性

很典型的自增操作，是非原子的。

### 竞态条件

最常见的一种竞态条件是检查再运行(check-then-act)。

比如说你已经检查到X文件不存在，然后基于这个判断做出下一步动作。
然而在这期间可能状态已经被改变（有人创建了文件X），那么将会引发错误。

### 复合操作

我们可以使用类似`AtomicLong`这种类，调用自增的方法，使之具有原子性。

## 锁


### 内部锁

我们可以使用`synchronized`将方法加锁，然而这样的效率十分低下。

### 重进入

内部所是可重进入的(reentrancy)，因此线程在请求自己占有的锁时会成功。

线程请求一个未被占用的锁时，JVM将记录锁的持有者，并将请求计数置为1。如果而同一线程再次请求这个锁，计数器加一。
当计数器为0时，锁释放。




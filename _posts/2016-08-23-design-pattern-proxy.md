---
title: 设计模式之代理模式
layout: post
date: 2016-08-23
categories: Design Pattern
---

应该是（看起来）比较简单的一个设计模式，中心思想就是让一个代理类来调用真实的接口，这样一来可以再代理中进行权限控制，一些与业务无关的代码的加入等。

# UML 类图

![proxy](http://images.cnitblog.com/blog/299855/201310/03085612-1e68bd5a753b44ce8349d046b52a29e7.png)

# 举个栗子

## Client

```
package designpattern.proxy;

/**
 * Created by Frog on 2016/8/23.
 */
public interface Subject {
    void write();
}
```

## Subject

```
package designpattern.proxy;

/**
 * Created by Frog on 2016/8/23.
 */
public interface Subject {
    void write();
}
```

## RealSubject

```
package designpattern.proxy;

/**
 * Created by Frog on 2016/8/23.
 */
public class Writer implements Subject {
    @Override
    public void write() {
        System.out.println("写了一本完美世界");
    }
}
```

## Proxy

```
package designpattern.proxy;

/**
 * Created by Frog on 2016/8/23.
 */
public class ProxyWriter implements Subject {
    private Subject realSubject;

    public ProxyWriter(Subject subject) {
        this.realSubject = subject;
    }

    @Override
    public void write() {
        System.out.println("呱呱代笔！");
        realSubject.write();
    }
}
```
## Result

```
呱呱代笔！
写了一本完美世界
```

## 应用

1. 虚拟代理。根据需要创建对象。
2. 远程代理。不懂
3. 安全代理。控制权限。
4. 智能指引，调用真实的对象时，代理处理另外一些事。其实感觉这个和第三点是一样的。

---
title: Java 中重写方法时的调用次序
layout: post
date: 2016-03-28
categories: Java
---

今天看到一个很有意思的东西。

先来看看下面一段代码

```
/**
 * Created by grizzly on 16-3-28.
 */
public class A {
    public void show(A obj) {
        System.out.println("A and A");
    }

    public static void main(String[] args) {
        A a2 = new B();
        a2.show(new B());
    }
}

class B extends A {
    @Override
    public void show(A obj) {
        System.out.println("B and A");
    }

    public void show(B obj) {
        System.out.println("B and B");
    }
}
```

一开始我以为肯定是输出`B and B`。
然而并不是，输出的是`B and A`。

这时候就是方法调用次序的问题了。

方法调用的优先级从高到低为 this.show(O)、super.show(O)、this.show((super)O)、super.show((super)O)。

所以先找 this.show(O)，A 类的方法里没这个方法，而且 A 也没有超类。
接下来就去找 `this.show((super)O)`，而且找到了。
然而这个方法绑定在了类 B 的方法上，所以调用的类 B 的方法。

真是神奇。

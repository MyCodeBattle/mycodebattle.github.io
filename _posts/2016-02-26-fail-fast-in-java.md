---
title: Java中的Fail-Fast机制
date: 2016-02-26
layout: post
categories: Java
---

# 什么是Fail-Fast机制

当多个线程同时对集合进行结构上的改变时，**有可能**引发Fail-Fast机制。
比如说两个Iterator，it1在遍历，it2删除了一个元素，那么就可能引发，程序就可能抛出`ConcurrentModificationException`异常。
但是这只是有可能抛出异常，所以不能编写一个依赖于此异常的程序。

# Fail-Fast机制的产生原因

先看看`ArrayList`中的源码。

```
private class Itr implements Iterator<E> {
    int cursor;
    int lastRet = -1;
    int expectedModCount = ArrayList.this.modCount;

    public boolean hasNext() {
        return (this.cursor != ArrayList.this.size);
    }

    public E next() {
        checkForComodification();
        /** 省略此处代码 */
    }

    public void remove() {
        if (this.lastRet < 0)
            throw new IllegalStateException();
        checkForComodification();
        /** 省略此处代码 */
    }

    final void checkForComodification() {
        if (ArrayList.this.modCount == this.expectedModCount)
            return;
        throw new ConcurrentModificationException();
    }
}
```
`Iterator`在调用`remove()`、`next()`的时候都会调用`checkForComodification()`，当`modCount != expectedModCount`的时候便会引发这个异常。

`modCount`一开始是0，每一个`add`操作和`remove`操作都会使他增加一。

当检测到`modCount`和期望的modCount不一致时，说明`ArrayList`已经在这个过程中被人修改。所以就抛出异常了。

# 解决办法

1. 给抛出异常的方法加锁
2. 使用`CopyOnWriteArray`。这个类每add一次就new一个新的数组，所以原来的不会变。然而这样就看不到新的修改了。根据情景使用吧。

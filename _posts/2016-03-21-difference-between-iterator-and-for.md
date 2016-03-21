---
title: Java 中使用 Iterator 和 索引的不同
layout: post
date: 2016-03-21
categories: Java
---

我们知道 Java 中可以使用 `for (Type ele : Object)` 的方法遍历容器，也可以用索引遍历。

使用前者实际上就是 new 了一个 Iterator，然后使用

```
 while (it.hasNext()) {
            it.next();
        }
```
来获取下一个值。

我们来看下在 ArrayList 中 it.next() 的源码。

```
public E next() {
    checkForComodification();
    int i = cursor;
    if (i >= size)
        throw new NoSuchElementException();
    Object[] elementData = ArrayList.this.elementData;
    if (i >= elementData.length)
        throw new ConcurrentModificationException();
    cursor = i + 1;
    return (E) elementData[lastRet = i];
}
```

O.get()的源码。

```
E elementData(int index) {
    return (E) elementData[index];
}

public E get(int index) {
    rangeCheck(index);

    return elementData(index);
}
```

所以如果可以 Random Access 的话，这两种方法严格上是没什么区别的，只是 Iterator 多判断了几次。

不过如果在 Sequential Access 的容器中，显然用 get(index) 的方法比直接用 Iterator 要慢很多。显然前者的时间复杂度是 $O(n^2)$的。



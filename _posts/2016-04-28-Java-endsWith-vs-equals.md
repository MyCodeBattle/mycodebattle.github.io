---
title: Java 中 endsWith 和 equals 的效率差异
layout: post
date: 2016-04-28
categories: Java
---

下午 51Nod 群里有人问了个问题：为什么用`endsWith`的效率比`equals`要低？

乍一看好像都差不多，上源码。

先看`endsWith`的：

```
public boolean endsWith(String suffix) {
    return startsWith(suffix, value.length - suffix.value.length);
}
```

```
public boolean startsWith(String prefix, int toffset) {
    char ta[] = value;
    int to = toffset;
    char pa[] = prefix.value;
    int po = 0;
    int pc = prefix.value.length;
    // Note: toffset might be near -1>>>1.
    if ((toffset < 0) || (toffset > value.length - pc)) {
        return false;
    }
    while (--pc >= 0) {
        if (ta[to++] != pa[po++]) {
            return false;
        }
    }
    return true;
}
```

这里可以看出`endsWith`相当于一个给了偏移量的`startsWith`，然后调用了`startsWith`方法。
这个方法先排除了长度大于被匹配的字符串和被匹配串不够匹配的情况，然后开始每一个位置的比较。

```
public boolean equals(Object anObject) {
    if (this == anObject) {
        return true;
    }
    if (anObject instanceof String) {
        String anotherString = (String)anObject;
        int n = value.length;
        if (n == anotherString.value.length) {
            char v1[] = value;
            char v2[] = anotherString.value;
            int i = 0;
            while (n-- != 0) {
                if (v1[i] != v2[i])
                    return false;
                i++;
            }
            return true;
        }
    }
    return false;
}
```

而`equals`首先判断了是不是同一个引用，然后判断了长度是否相等，接下来才开始一个一个遍历，所以在复杂度相同的情况下`equals`会比`endsWith`效率高。



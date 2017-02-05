---
title: String.substring 引起的内存泄露问题
layout: post
date: 2017-02-05
categories: Java
---

随便看的时候忽然看到`substring`竟然有内存泄露的问题。然后进去一看原来是 Java 6 时代的问题。

重现 bug 代码：

```
public class TestGC {
    private String largeString = new String(new byte[100000]);

    String getString() {
        return this.largeString.substring(0,2);
    }

    public static void main(String[] args) {
        java.util.ArrayList list = new java.util.ArrayList();
        for (int i = 0; i < 1000000; i++) {
            TestGC gc = new TestGC();
            list.add(gc.getString());
        }
    }
}
```
在 jdk 1.7 及以后，这里不会 OOM，否则会。

先看下这个问题是如何产生的：

JDK1.6 的`substring`代码：

```
public String substring(int beginIndex, int endIndex) {
	if (beginIndex < 0) {
	    throw new StringIndexOutOfBoundsException(beginIndex);
	}
	if (endIndex > count) {
	    throw new StringIndexOutOfBoundsException(endIndex);
	}
	if (beginIndex > endIndex) {
	    throw new StringIndexOutOfBoundsException(endIndex - beginIndex);
	}
	return ((beginIndex == 0) && (endIndex == count)) ? this :
	    new String(offset + beginIndex, endIndex - beginIndex, value);
    }

String(int offset, int count, char value[]) {
	this.value = value;
	this.offset = offset;
	this.count = count;
}
```

问题的根源就是在这个构造函数上。`substring`方法只是传了一个偏移量，然后直接把`value`引用传递给了新的 String。在上面那段程序中，仅仅需要两个字符，却引用了整个字符串，使得 GC 无法工作。

之后，构造函数被改成了这样：

```
public String(char value[], int offset, int count) {
    if (offset < 0) {
        throw new StringIndexOutOfBoundsException(offset);
    }
    if (count <= 0) {
        if (count < 0) {
            throw new StringIndexOutOfBoundsException(count);
        }
        if (offset <= value.length) {
            this.value = "".value;
            return;
        }
    }
    // Note: offset or count might be near -1>>>1.
    if (offset > value.length - count) {
        throw new StringIndexOutOfBoundsException(offset + count);
    }
    this.value = Arrays.copyOfRange(value, offset, offset+count);
}
```

可以发现，最后返回了一个新的引用。而且`offset`这个成员变量也被取消了。
以上。
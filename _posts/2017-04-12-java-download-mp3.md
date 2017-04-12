---
title: Java 下载歌曲时由于写入额外字节引发的错误
layout: post
date: 2017-04-12
categories: 
---

下午用 Java 下歌的时候发现下下来的歌听不了，但是直接用浏览器下载没问题。发现 MD5 不一样，可能是文件损坏了。

但是之前写下载图片也是这么写的，并没有出什么问题。于是就疯狂搜索，终于找到错误原因。

是由下面的代码引发的：

```java
try {
    byte[] buf = new byte[1024];
    int len = 0;
    while ((len = is.read(buf)) != -1) {
        out.write(buf);
    }
    out.flush();
    System.out.println("success");
} finally {
    out.close();
    is.close();
}
```

当最后一次写入不满 1024 时，它也把所有的 1024 字节写入了。导致写入了原本不应该有的字节。
太懒了 Orz。
改成这样就好了

```java
try {
    byte[] buf = new byte[1024];
    int len = 0;
    while ((len = is.read(buf)) != -1) {
        out.write(buf, 0, len);
    }
    out.flush();
    System.out.println("success");
} finally {
    out.close();
    is.close();
}
```

以上。
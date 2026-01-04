---
title: Java 中的 try-with-resources 语句
layout: post
date: 2016-06-06
categories: Java
---

晚上像以前一样写 `try-catch-finally`形打开数据库操作的时候发现 IDEA 上有这么一个提示:

> 'try' can use automatic resource management.

一看我就懵了，难道还有另外的写法。然后我就点了一下自动完成，代码就变成了这个样子。

```
try (Session session = sessionFactory.openSession()) {
    Transaction ts = session.beginTransaction();
        session.save(replyEntity);
        ts.commit();
        return true;
    } catch (Exception e) {
        System.out.println("保存帖子出错了");
        return false;
    }
}
```

按照提示查了一下，这个是 Java 7 里的新特性，叫`try-with-resources statement`。作用就是能自动关闭打开的资源文件。

那么它和手动 finally 有什么不一样呢？

考虑这么一种情况。

```
static String readFirstLineFromFileWithFinallyBlock(String path)
                                                     throws IOException {
    BufferedReader br = new BufferedReader(new FileReader(path));
    try {
        return br.readLine();
    } finally {
        if (br != null) br.close();
    }
}
```

假设我们 readLine 方法抛出了一个异常， close 又抛出了一个异常，那么 readLine 的异常就被**suppress**了，我们只能接收到 close 的异常。 
但是如果我们用 try-with-resources 语句的话，在这个语句中的异常将被 suppress，但是我们可以通过`Throwable.getSuppressed`来捕获被 suppress 的异常。


来看下面这个例子

```
public class TryWithResources {
 
    public static void main(String[] args) throws Exception {
 
        try ( OpenDoor door = new OpenDoor() ) {
            door.swing(); //this throws a SwingExecption
        }
        catch (Exception e) { 
            System.out.println("Is there a draft? " + e.getClass());
            int suppressedCount = e.getSuppressed().length;
            for (int i=0; i<suppressedCount; i++){
                System.out.println("Suppressed: " + e.getSuppressed()[i]);
            }
        }
        finally {
            System.out.println("I'm putting a sweater on, regardless. ");
        }
    }
}
 
class OpenException extends Exception {}
class SwingException extends Exception {}
class CloseException extends Exception {}
 
class OpenDoor implements AutoCloseable {
 
    public OpenDoor() throws Exception {
        System.out.println("The door is open.");
    }
    public void swing() throws Exception {
        System.out.println("The door is becoming unhinged.");
        throw new SwingException();
    }
 
    public void close() throws Exception {
        System.out.println("The door is closed.");
        throw new CloseException(); // throwing CloseException 
    }
}
```

try 块里的异常被捕获了， try-with-resources 语句里的异常通过方法被捕获。



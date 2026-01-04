---
title: try-catch-finally 中的 return
layout: post
date: 2016-07-05
categories: Java
---

前几天去面试，出了这么道笔试题

```
try {
    System.out.println("hello");
    System.exit(0);
} finally {
    System.out.println(" world");
}
```

我一看就方了：这 finally 还执行不？

答案是不执行的，因为虚拟机停了全部都停了。 
当然我选错了。

然后我又想起了很早之前做过的题

```
try {
    System.out.println("try");
    if (Math.random() < 0.5) throw new Exception();
    return 10;
} catch (Exception e) {
    System.out.println("catch");
    return 9;
} finally {
    return 20;
}
```

问最后的返回结果是多少。

可能大家都知道最后返回的是 20，那么一开始的 10 去哪里了呢？

反编译下。

```
{
  public Hello();
    descriptor: ()V
    flags: ACC_PUBLIC
    Code:
      stack=1, locals=1, args_size=1
         0: aload_0
         1: invokespecial #1                  // Method java/lang/Object."<init>":()V
         4: return
      LineNumberTable:
        line 18: 0

  public static void main(java.lang.String[]);
    descriptor: ([Ljava/lang/String;)V
    flags: ACC_PUBLIC, ACC_STATIC
    Code:
      stack=2, locals=1, args_size=1
         0: getstatic     #2                  // Field java/lang/System.out:Ljava/io/PrintStream;
         3: invokestatic  #3                  // Method test:()I
         6: invokevirtual #4                  // Method java/io/PrintStream.println:(I)V
         9: return
      LineNumberTable:
        line 20: 0
        line 21: 9

  public static int test();
    descriptor: ()I
    flags: ACC_PUBLIC, ACC_STATIC
    Code:
      stack=4, locals=3, args_size=0
         0: getstatic     #2                  // Field java/lang/System.out:Ljava/io/PrintStream;
         3: ldc           #5                  // String try
         5: invokevirtual #6                  // Method java/io/PrintStream.println:(Ljava/lang/String;)V
         8: invokestatic  #7                  // Method java/lang/Math.random:()D
        11: ldc2_w        #8                  // double 0.5d
        14: dcmpg
        15: ifge          26
        18: new           #10                 // class java/lang/Exception
        21: dup
        22: invokespecial #11                 // Method java/lang/Exception."<init>":()V
        25: athrow
        26: bipush        10
        28: istore_0
        29: bipush        20
        31: ireturn
        32: astore_0
        33: getstatic     #2                  // Field java/lang/System.out:Ljava/io/PrintStream;
        36: ldc           #12                 // String catch
        38: invokevirtual #6                  // Method java/io/PrintStream.println:(Ljava/lang/String;)V
        41: bipush        9
        43: istore_1
        44: bipush        20
        46: ireturn
        47: astore_2
        48: bipush        20
        50: ireturn
      Exception table:
         from    to  target type
             0    29    32   Class java/lang/Exception
             0    29    47   any
            32    44    47   any
      LineNumberTable:
        line 25: 0
        line 26: 8
        line 27: 26
        line 32: 29
        line 28: 32
        line 29: 33
        line 30: 41
        line 32: 44
      StackMapTable: number_of_entries = 3
        frame_type = 26 /* same */
        frame_type = 69 /* same_locals_1_stack_item */
          stack = [ class java/lang/Exception ]
        frame_type = 78 /* same_locals_1_stack_item */
          stack = [ class java/lang/Throwable ]
}
```

那么问题就来了，这里的反编译代码和 **Java Virtual Machine Specification** 上的不一样。 
查了一下，原来虚拟机说明上的是 50.0 以下的版本，而我的是 52。这就非常地尴尬了。

新版本的虚拟机已经取消了 jsr 这个指令，不知道是什么原理让执行 try 的时候不执行 ireturn. 不过这也不影响，我们能看出在 try 块 return 值的时候，这个值被 store 在了 local variable 里，然后跑去执行 finally 里的内容了。而在 finally 处，一个 bipush，紧接着就是 ireturn，这时候整个 frame 被销毁，因此刚才存的变量完全没用了。

如果 finally 里没有返回值，在 finally 处会 load\_0，然后 ireturn.

到此为止原理应该是清楚了，如果想要弄清是怎么跳转到 finally 处指令的大概要等到下一版 JVM Specification 了。

今天看了这么多才发现对 Java 里栈的理解完全错了。每个线程在启动的时候分配一个栈，然后 Operand Stack 和 local variable 都分配在 frame 上，这是调用每个方法时产生的！



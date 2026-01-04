---
title: StringBuilder 和 StringBuffer
layout: post
date: 2016-06-22
categories: Java
---

前几天用到了`StringBuilder`，顺便看了一下代码，记一下一些比较有意思的。

`StringBuilder`是非线程安全的，它和`StringBuffer`的代码绝大部分公用抽象类`AbstractStringBuilder`中的方法。


它的初始化大小是`16`，如果在构造函数中传入字符串，大小就会是`str.length() + 16`。

当它`append(null)`时，是真的会 append 「null」进数组的，类似的，append 一个`boolean`数值时，结果也是「true」或者「false」。

空间增长策略，每次扩充 `size*2 + 2`，不知道这个 + 2 是什么情况。

然后大部分的类似`insert`，`replace`的方法都调用了`System.arraycopy`来复制。

这里的`reverse()`会判断是不是`Unicode`字符，如果是的话在翻转一遍过后还会用某种方法再翻一下。

`StringBuffer`是线程安全的，其实就是在方法前都加了`synchronized`。

比较奇怪的是`StringBuffer`缓存了一个`toString()`对象，然后每次更新对象置`null`，不知道为什么`StringBuilder`不缓存一下。



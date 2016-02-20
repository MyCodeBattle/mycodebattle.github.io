---
categories: Memorandum
date: 2015-11-23 22:40:14
title: 一些零碎的C++知识点备忘
tags: 
layout: post
---

---

转载自http://blog.csdn.net/lwbkfc/article/details/8041893

size_t是unsigned类型，用于指明数组长度或下标，它必须是一个正数，std::size_t
ptrdiff_t是signed类型，用于存放同一数组中两个指针之间的差距，它可以使负数，std::ptrdiff_t.
size_type是unsigned类型,表示容器中元素长度或者下标，vector<int>::size_type i = 0;
difference_type是signed类型,表示迭代器差距，vector<int>:: difference_type = iter1-iter2.
前二者位于标准类库std内，后二者专为STL对象所拥有。
 
ptrdiff_t n=ip2-ip;
结果是4，这两个指针所指向的元素间隔为4个对象。两个指针减法操作的结果是标准库类型ptrdiff_t的数据。与size_t类型一样一，ptrdiff_t也是一种与机器相关的类型，在cstddef头文件中定义。size_t是unsigned类型，而ptrdiff_t是signed类型。这两种类型的差别体现了它们各自的用途：size_t类型用于指明数组长度，它必须是一个正数；ptrdiff_t类型则应保证足以存放同一数组中两个指针之间的差距，它有可能是负数。

---

operator new()：指对new的重载形式，它是一个函数，并不是运算符。对于operator new来说，分为全局重载和类重载，全局重载是void* ::operator new(size_t size)，在类中重载形式 void* A::operator new(size_t size)。还要注意的是这里的operator new()完成的操作一般只是分配内存，事实上系统默认的全局::operator new(size_t size)也只是调用malloc分配内存，并且返回一个void*指针。而构造函数的调用(如果需要)是在new运算符中完成的。
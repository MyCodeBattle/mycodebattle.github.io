---
title: ArrayDeque 和 LinkedList
layout: post
date: 2016-04-30
categories: Java
---

昨天搜了一下很久之前就想的一个问题：为什么 Java 里的 Queue 使用 LinkedList 实现？

虽然链表这一结构适合队列的先进先出，不过大量 new 和 删除结点引发的 GC 代价也是很高的。

随便插一点，ArrayDeque 里不允许 null。

我粗略地测试了一下 1e7 左右的 push 和 poll，使用 ArrayDeque 是使用 LinkedList 的 1/10，虽然这样的测试不太科学，不过还是可以看出使用循环队列比链表的效率要高。

在这里记录一些 ArrayDeque 的实现细节，省得以后老是像忘了 ArrayList 的默认初始化容量一样忘一些东西。

ArrayDeque 的最少分配空间是 8，默认分配 16，初始的 head 和 tail 都是 0。

它的每个 offer、poll 操作都是将这两个指针加一/减一再和（容量-1）相与。贴段代码。

```
public void addFirst(E e) {
    if (e == null)
        throw new NullPointerException();
    elements[head = (head - 1) & (elements.length - 1)] = e;
    if (head == tail)
        doubleCapacity();
}

public void addLast(E e) {
    if (e == null)
        throw new NullPointerException();
    elements[tail] = e;
    if ( (tail = (tail + 1) & (elements.length - 1)) == head)
        doubleCapacity();
}
```

这里巧妙地利用了容量是 2 的幂次的性质，位运算显然比取模要快多了。
当容量不够的时候，也就是 head 和 tail 相等的时候，就采取了 doubleCapacity 操作。

这个操作就是申请了一块二倍大的空间，然后把 head 至 length 复制到新数组里，然后把剩下的复制到新数组里。
然后调整一下 head 和 tail。

```
private void doubleCapacity() {
    assert head == tail;
    int p = head;
    int n = elements.length;
    int r = n - p; // number of elements to the right of p
    int newCapacity = n << 1;
    if (newCapacity < 0)
        throw new IllegalStateException("Sorry, deque too big");
    Object[] a = new Object[newCapacity];
    System.arraycopy(elements, p, a, 0, r);
    System.arraycopy(elements, 0, a, r, p);
    elements = a;
    head = 0;
    tail = n;
}
```

其他的就没什么意思了。






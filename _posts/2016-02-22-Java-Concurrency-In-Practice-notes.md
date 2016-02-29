---
title: Java Concurrency In Practice 笔记
layout: post
date: 2016-02-22
categories: Java Notes
---

我就想看看我能写多久。


# Chapter2. Thread Safety

## 线程安全

当变量都存在线程自身的栈的时候，这个对象是线程安全的，就像这样。

```
@ThreadSafe
public class statelesFactorizer implements Servlet {
    public void service(ServletRequest req, ServletResponse resp) {
        BigInteger i = extractFromRequest(req);
        BigInteger[] factors = factor(i);
        encodeIntoResponse(resp, factors);
    }
}
```
## 原子性

很典型的自增操作，是非原子的。

### 竞态条件

最常见的一种竞态条件是检查再运行(check-then-act)。

比如说你已经检查到X文件不存在，然后基于这个判断做出下一步动作。
然而在这期间可能状态已经被改变（有人创建了文件X），那么将会引发错误。

### 复合操作

我们可以使用类似`AtomicLong`这种类，调用自增的方法，使之具有原子性。

## 锁


### 内部锁

我们可以使用`synchronized`将方法加锁，然而这样的效率十分低下。

### 重进入

内部所是可重进入的(reentrancy)，因此线程在请求自己占有的锁时会成功。

线程请求一个未被占用的锁时，JVM将记录锁的持有者，并将请求计数置为1。如果而同一线程再次请求这个锁，计数器加一。
当计数器为0时，锁释放。


# Chapter5. Building Blocks
<s>中间的有机会再补</s>

## Synchronized Collections

### Problems with Synchronized Collections

虽然`Vector`和`Hashtable`是线程安全的，但这并不意味着我们可以随意使用，在某些复合操作下。

比如说两个方法`getLast`和`deleteLast`，如果他们同时获取了List的Length，那么deleteLast又先于getLast执行，就会抛出数组越界的异常，这样我们只能把这两个复合操作加上`client-side locking`。

如果使用普通的循环遍历容器，可能会抛出数组越界; 如果用`Iterator`来遍历，可能会抛出`ConcurrentModificationException`。这时候我们如果使用`client-side locking`就可能会造成死锁。
我们也可以使用copy一个数组来iterator的方法，不过这种方法要看情况使用。

### Hidden Iterators

有些隐式的Iterator可能会被调用。
比如说`System.out.println(set)`，隐式地调用了`set.toString()`，然后遍历了一遍迭代器。这个过程就和上面一样了。所以在使用之前也要加锁。
还有一些隐式iterator的方法，比如`hashcode`、`containsAll`、`removeAll`等。

## Concurrent Collections

Java 5.0中加入了`ConcurrentHashMap`和`CopyOnWriteArrayList`，后者适合读多写少。

### ConcurrentHashMap

`ConcurrentHashMap`使用了一种叫做`lock striping`的机制，允许读写一起进行。
该容器在迭代时并不会抛出`ConcurrentModificationException`。它的iterator是`weakly consistent`的，可能会反应出容器最新的修改。

它的`size`和`isEmpty`方法也做了权衡。
因为它们不一定总是能返回真实的情况，所以它们被允许返回一个大概的值。

它不提供为了特有的入口而锁住整个map，是为了以下的权衡：并行集合类应该被期望不间断地改变他们的内容。

除非程序需要锁住特别的入口，使用`ConcurrentHashMap`代替`Hashtable`是一个比较好的选择。

### CopyOnWriteArrayList

每修改一次就会new一个新的对象，适合如下的情景：
传送一个消息需要迭代监听列表，很多情况下监听列表不用修改很多次。

## Blocking Queues and the Producer-consumer Pattern

介绍了生产者-消费者模型。

`BlockingQueue`接口包括`LinkedBlockingQueue`和`ArrayBlockingQueue`等，它们的关系和`ArrayList`相似。还有`PriorityBlockingQueue`。
`SynchronousQueue`并不完全是一个队列，它直接将生产出来的数据给消费者。它没有消耗额外的存储空间，适合消费者很多的情况。
 
 ### Deques and Work Stealing
 
 `Deque`的应用可以在一个叫做`Work Stealing`的模式下。
 平时的时候消费者使用自己的Deque，万一自己的用完了，就可以从别人的队尾「偷」东西，减少了contention.
 
 ## Blocking and Interruptible Methods
 
 `Interruption`是一个合作的机制，线程A并不能强制要求线程B暂停。
 
 我们最好对`InterruptedException`做出处理。
 
 ## Synchronizers
 
 Synchronizer是那些根据自身状态协调控制流的**对象**。

### Latches

Latch可以延迟线程，直到满足所有条件线程才开始运行，就像门一样。
这有点像`Toposort`，一个活动要满足之前的条件才能举行。 

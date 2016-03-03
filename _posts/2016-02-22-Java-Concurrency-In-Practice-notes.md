---
title: Java Concurrency In Practice 笔记
layout: post
date: 2016-02-22
categories: Java Notes
---

我就想看看我能写多久。

* content
{:toc}


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



### FutureTask

`FutureTask`类实现了`Future`接口，它的计算通过`Callable`实现，相当于可以携带结果的`Runnable`。
`future.get`方法会返回计算结果，如果计算尚未完成就会阻塞直到完成。

### Semaphore

信号量。
它的构造函数中有个`boolean`变量`fair`，意思是一个刚释放锁的线程能不能又拿到锁。
通常情况下应该是true，否则可能会造成有的线程饿死。
`sem.acquire`获取一个信号量，否则一直阻塞。
`sem.release`释放。

### Barriers

Barriers可以等待一组线程，等他们全部到达的时候一起释放。可以实现Runnable接口，表示执行最后一个线程到达之后，全部释放之前的操作。
用的类是`CyclicBarriers`


# Task Execution

## Executing Tasks in Threads

### Executing Tasks Sequentially

线性执行任务会造成后面的线程等待，效率非常差。

### Explicitly Creating Threads for Tasks

利用多线程可以提高效率，但是无限地增加线程有很多缺陷。

### Disadvantages of Unbounded Thread Creation

- 当线程超过处理器的线程时，等待的线程会占用内存空间。
- 线程间的竞争会消耗资源。
- 能创建的线程有上限。

## The Executor Framework

`Executor`使用线程池来管理线程，可以重复利用已经创建出来的线程。我们并不用手动创建新的线程。

### Thread Pools

线程池可以重复利用线程，使得响应更迅速。
`newFixedThreadPool`是固定大小的线程池。
`newCachedThreadPool` 一个缓存的线程池，当线程池大小超过工作需求时可以方便地收割空闲进程。但是大小没上限。
`newSingleThreadExecutor` 创建单例线程，线序执行任务，提供足够的内在同步方法保证任何的修改对接下来的任务都可见。
`newScheduledThreadPool` 支持延迟和任务的周期执行。

### Executor Lifecycle

`ExecutorService`接口提供了控制生命周期的几个方法。
调用`shutdown`的时候，它不再接受新的任务，而会把当前执行的任务执行完，这时候的状态是`shutdown`。
在这之后状态变为`terminated`。

### Delayed and Periodic Tasks

`Timer`类可以让线程运行设定时间，然而有一些缺点，包括一旦抛出了一个 unchecked Exception，整个`TimerTasks`就 terminates 了。

文章中建议用`Delay?Queu`或者`BlockingQueue`代替。




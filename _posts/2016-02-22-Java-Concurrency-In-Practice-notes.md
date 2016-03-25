---
title: Java Concurrency In Practice 笔记
layout: post
date: 2016-02-22
categories: Java Notes
updated: 2016-03-04
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

文章中建议用`DelayQueue`或者`BlockingQueue`代替。


## Finding Exploitable Parallelism

我们要尽可能地找到任务中可以并行的部分。

### CompletionService

> "如果向Executor提交了一组计算任务，并且希望在计算完成后获得结果，那么可以保留与每个任务关联的Future，然后反复使用get方法，同时将参数timeout指定为0，从而通过轮询来判断任务是否完成。这种方法虽然可行，但却有些繁琐。幸运的是，还有一种更好的方法：完成服务CompletionService。"

这个接口和ExecutorService的区别主要在使用后者的时候我们要不断调用get判断工作是否完成，这个一旦take就是已经完成的任务。
还是有点搞不清楚。

### Summary

本章主要讲了如何使用`Executor`和相关的接口。以及如何开发出程序的并行性。

# Chapter 7. Cancellation and Shutdown

Java并不提供API强制终止线程。因为这样可能让共享的数据处于一个异常的状态。所以它提供了一个「合作机制」。
是否处理好 failure、shutdown、和 cancellation 是鉴别一个应用是否表现良好的重要方面。

## Task Cancellation

我们可以使用一个`boolean`变量`cancel`来标记是否有取消的请求。不过这样当线程被阻塞时便无法检查到这个变量，所以就会一直阻塞下去。

更好的办法是使用`interrupt`。

### Interruption

使用`interrupt`的时候，即使线程被阻塞也能收到消息。
`interrupted`方法返回了一个`boolean`，判断中断位是否被设置。如果被设置了，之后中断位会被清零，所以使用的时候要注意。


### Responding to Interruption

这章讲得好玄幻，基本看不懂。
大概就是讲当interrupt的时候，线程会抛出`InterruptedException`，这时候我们不能吞了它，要么做出处理，要么向上级 throw。


### Cancellation Via Future

当我们把 task 提交给 Executor 运行的时候，我们不知道 task 会被哪个线程执行，所以不能用 Thread.interrupt 方法。
这时候可以用`Future`的`cancel`方法。
该方法返回 false，如果 task 不能被取消（已经完成、已经取消）。
如果成功，尚未启动的任务永远不会启动。

如果任务已经启动，看传进去的参数，如果是`true`就会标记`interrupt`，否则失败。

如果一个任务没有处理中断异常，总是应该传入`false`。


# Chapter 13 - Explicit Locks

## Lock and ReentrantLock

`Lock`和`synchronized`的区别在于 Lock 更加灵活。
synchronized 的时候，线程一旦等待 synchronized 锁住的对象的时候便不能中断。
lock 还能用来锁一些结点，比如说 list 里的，这样我们能并发地访问每一个结点。（ConcurrentHashMap 的思想？）

## Polled and Timed Lock Acquisition

lock 可以设置等待获取锁的时间，一旦到达时间就放弃。方法是`lock.tryLock(time, NANOSECONDS)`.

## Interruptible Lock Acquisition

`lock.lockInterruptibly()`提供了能中断的 lock。

## Fairness

lock 分为 fair 和 unfair 两个，默认是 unfair。通常情况下 unfair 的 lock performance 要优于 fair lock。
考虑以下情形：
A 拿着锁，B 请求锁，然后进入队列。这时候 A 要释放锁，这时候 C 来了。如果是 fair lock，这时候会唤醒 B，让 B 先上。
但是可能发生这种情况：C 插队，等它运行完 B 才刚刚被唤醒，这样就是双赢了。
事实上 intrinsic lock 也是 unfair 的，虽然 JLS 没有规定。


## Choosing Between Synchronized and ReentrantLock

虽然 Lock 的效率通常比 intrinsic lock 要高，但是作者还是建议除非我们要用到 advanced features 的时候才考虑用 lock，通常的话还是使用 intrinsic lock 比较保险。因为 lock 要手动释放和获取。

## Read-write Locks

读写锁常用在读操作比写操作大得多的情况下。它能让多个读线程同时访问。
如果在其他情况下，性能是不如 lock 的 - 因为它就是用 lock 实现的。

插句无关的话：`ReadWriteMap`并没有实现`Map`接口，因为有些方法比如`entrySet`很难实现，一些简单的就够了。




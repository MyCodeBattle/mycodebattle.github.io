---
title: 设计模式之装饰模式
layout: post
date: 2016-08-21
categories: Design Pattern
---

装饰模式就是给一个对象加上更多的责任。

比如说我们要开发一个日志类，有个基本的功能记录日志。

但是我们在不同的时候需要不同类型的日志，比如错误日志，警告日志。

如果在平时的话，我们会考虑需要什么就把它们合在一个类中，如

```
public class LogExample {
    private ErrorLogger errorLogger;
    private WarnLogger warnLogger;
    
    public void write() {
        errorLogger.write();
        warnLogger.write();
    }
}
```

那么如果我们需要不同组合的话，就会产生非常多不同的子类。

这时候我们可以用装饰模式。

-----

上个类图

![decorator](http://pic002.cnblogs.com/images/2012/267603/2012010318015849.jpg)

- `Component`是需要规范的动作。
- `ConcreteComponent`是要被装饰的类。
- `Decorator` 持有一个`Component`实例。
- `ConcreteDecorator`负责装饰

举个栗子

`Component`

```
package designpattern.decorator;

/**
 * Created by Frog on 2016/8/21.
 */
public interface Log {
    void write();
}
```

`ConcreteComponent`

```
package designpattern.decorator;

/**
 * Created by Frog on 2016/8/21.
 */
public class Logger implements Log {
    @Override
    public void write() {
        System.out.println("普通的日志");
    }
}
```

`Decorator`
    
```
package designpattern.decorator;

/**
 * Created by Frog on 2016/8/21.
 */
public class LogDecorator implements Log {
    private Log log;

    public LogDecorator(Log log) {
        this.log = log;
    }

    @Override
    public void write() {
        log.write();
    }
}
```

`ConcreteDecorator`

```
package designpattern.decorator;

/**
 * Created by Frog on 2016/8/21.
 */
public class ErrorLogger extends LogDecorator {

    public ErrorLogger(Log log) {
        super(log);
    }

    @Override
    public void write() {
        super.write();
        System.out.println("记录错误日志");
    }
}
```

```
package designpattern.decorator;

/**
 * Created by Frog on 2016/8/21.
 */
public class WarnLogger extends LogDecorator {

    public WarnLogger(Log log) {
        super(log);
    }

    @Override
    public void write() {
        super.write();
        System.out.println("警告日志");
    }
}
```

----

```
package designpattern.decorator;

/**
 * Created by Frog on 2016/8/21.
 */
public class Solution {

    public static void main(String[] args) {
        Log log = new WarnLogger(new ErrorLogger(new Logger()));
        log.write();
    }
}
```

```
普通的日志
记录错误日志
警告日志
```


这样就达到了任意组合的效果。

其实感觉里面的精髓就是利用了一个 super 动作，然后递归调用上面全部的动作。
也就是每个类有一个指针，指向了另一个功能类。╮(╯▽╰)╭

以上。
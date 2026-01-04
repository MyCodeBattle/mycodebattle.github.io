---
title: 设计模式之策略模式
layout: post
date: 2016-08-10
categories: Design Pattern
---

## 场景

首先看这么一个场景：

> 假定现在需要实现一个简化的报价管理，实现如下的功能：

1. 对普通客户或者是新客户报全价.

2. 对老客户报的价格，统一折扣5%.

3. 对大客户报的价格，统一折扣10%

### 不用模式的解决方案

也就是现在的我的水平：

```
public double quote(double goodsPrice, String customerType) {
    if (customerType.equals("普通客户")) {
        return this.calcPriceForNormal(goodsPrice);
    }
    else if (customerType.equals("老客户")) {
        return this.calcPriceForOld(goodsPrice);
    }
    else if (customerType.equals("大客户")) {
        return this.calcPriceForLarge(goodsPrice);
    }
    return goodsPrice;
}
```
这样的问题在于，当添加一个新的方法时，就要去修改原来的代码，违反了开-闭原则。还有，考虑这么一种需求：当节日的时候，物品在原来的基础上有不同程度的打折。这个时候就得跑到实现函数里改代码。

### 策略模式解决

我们让这几个相似的方法形成一系列方法，然后定义一个公共的接口，这样在使用的时候替换一下就可以了。
当要维护某个算法的时候，只要修改对应的方法，不会对另外的方法造成影响。

为了让算法实现独立与客户，需要引入一个上下文对象，这个对象负责持有算法，但是不负责选择使用哪个算法，让客户选择算法。

之前我想了很久为什么还要一个上下文对象。让客户直接持有接口不行吗？后来想到这样有更好的扩展性。比如现在要在原来的基础上打9折，只要在对象调用接口的哪个方法里，结果算出来之后 * num 就行了，客户这边接口不用变。

### 模式结构

![结构](http://www.uml.org.cn/sjms/images/2010062321051411.jpg)

- Strategy: 策略接口。
- ConcreateStrategy: 具体实现策略。
- Context: 上下文，负责和策略类交互。

### 策略模式实现

#### Strategy 

```
public interface Strategy {
    void apply();
}
```

#### ConcreateStrategy 

```
public class ConcreateStrategyA implements Strategy {
    @Override
    public void apply() {
        System.out.println("算法A");
    }
}
```

```
public class ConcreateStrategyB implements Strategy {
    @Override
    public void apply() {
        System.out.println("算法B");
    }
}
```

```
public class ConcreateStrategyC implements Strategy {
    @Override
    public void apply() {
        System.out.println("算法C");
    }
}
```

#### Context

```
public class StrategyContext {
    private Strategy strategy;

    public StrategyContext(Strategy strategy) {
        this.strategy = strategy;
    }

    public void getResult() {
        strategy.apply();
    }
}
```

#### Client

```
public class Client {
    public static void main(String[] args) {
        Strategy strategy = new ConcreateStrategyA();
        StrategyContext context = new StrategyContext(strategy);
        context.getResult();
    }
}
```

那么问题来了：如何知道创建哪个对象呢。。应该是通过反射。


这里就是策略模式的大概内容了。明天再补上一些高级应用。

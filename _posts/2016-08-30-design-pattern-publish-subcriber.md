---
title: 设计模式之观察者模式
layout: post
date: 2016-08-30
categories: Design Pattern
---

## 情景

实验室里的学习三人组：吴某、谢某、卓某订阅了一个<b>色情</b>频道，他们希望能尽快收到推送。

考虑到解耦，我们把三人组抽象成订阅者。

## UML

![observer](http://images.cnitblog.com/blog/159936/201307/11113251-ae6b015242f84819951324627f73d6f1.png)

## 例子

`Observer`

```
package designpattern.observer;

/**
 * Created by Frog on 2016/8/30.
 */
public abstract class Subscriber {
    private String name;
    private YellowMessage yellowMessage;

    public abstract void updateTorrent();

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public YellowMessage getYellowMessage() {
        return yellowMessage;
    }

    public void setYellowMessage(YellowMessage yellowMessage) {
        this.yellowMessage = yellowMessage;
    }
}

```

```
package designpattern.observer;

/**
 * Created by Frog on 2016/8/30.
 */
public class WuSubscriber extends Subscriber {
    @Override
    public void updateTorrent() {
        System.out.println("吴某获得最新的种子地址啦！ " + getYellowMessage().getTorrent());
    }
}
```

```
package designpattern.observer;

/**
 * Created by Frog on 2016/8/30.
 */
public class XieSubscriber extends Subscriber {
    @Override
    public void updateTorrent() {
        System.out.println("谢某获得最新的种子地址啦！" + getYellowMessage().getTorrent());
    }
}
```

```
package designpattern.observer;

/**
 * Created by Frog on 2016/8/30.
 */
public class ZhuoSubscriber extends Subscriber {
    @Override
    public void updateTorrent() {
        System.out.println("卓某获得最新的种子地址啦！ " + getYellowMessage().getTorrent());
    }
}
```

`Subject`
```
package designpattern.observer;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by Frog on 2016/8/30.
 */
public abstract class  YellowMessage {
    private String torrent;
    private List<Subscriber> subscriberList = new ArrayList<>();

    public List<Subscriber> getSubscriberList() {
        return subscriberList;
    }

    public void setSubscriberList(List<Subscriber> subscriberList) {
        this.subscriberList = subscriberList;
    }

    public String getTorrent() {

        return torrent;
    }

    public void setTorrent(String torrent) {
        this.torrent = torrent;
    }

    public abstract void publish();
    public abstract void getLatestTorrent();
}

```

```
package designpattern.observer;

import java.util.List;

/**
 * Created by Frog on 2016/8/30.
 */
public class YiLingErSi extends YellowMessage {

    @Override
    public void publish() {
        getSubscriberList().forEach(Subscriber::updateTorrent);
    }

    @Override
    public void getLatestTorrent() {
        System.out.println(getTorrent());
    }
}
```

`output`

```
卓某获得最新的种子地址啦！ http://wtfgame.cc
吴某获得最新的种子地址啦！ http://wtfgame.cc
谢某获得最新的种子地址啦！http://wtfgame.cc
```
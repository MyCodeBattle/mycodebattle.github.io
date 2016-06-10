---
title: Spring MVC 中的 @InitBinder
layout: post
date: 2016-06-10
categories: Spring MVC
---

在写玩具的时候碰到这么一个问题：一个 form 表单里，对应处理的方法有两个对象，而且这两个对象有属性是一样的名字。 
这时候的自动绑定就有问题了。这时候会提示这个东西：

> The request sent by the client was syntactically incorrect.

实际上就是无法进行数据绑定了。

这时候需要用 @InitBinder 注释来手动告诉 Spring MVC 如何绑定。

```
@InitBinder("replyEntity")
public void bindReply(WebDataBinder webDataBinder) {
    webDataBinder.setFieldDefaultPrefix("reply.");
}

@InitBinder("tiebaEntity")
public void bindTieba(WebDataBinder webDataBinder) {
    webDataBinder.setFieldDefaultPrefix("tieba.");
}
```

然后在 form 上加入前缀即可。

在找`@InitBinder`资料的时候还发现，Spring MVC 默认的绑定对象不能超过 255 个，如果超过这个数的话也要用`@InitBinder`来设置。

`@InitBinder`还能对一些 Spring MVC 绑定有问题的类自己处理，比如日期。还没用到，先不写了。

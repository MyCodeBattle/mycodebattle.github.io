---
title: Struts2 中在 action 之间跳转保留 request 的方法
layout: post
date: 2016-05-22
categories: Java
---

如果一般的跳转，`request`里的值是会消失的。
所以在配置的时候应该这么搞：
`<result name="success" type="chain">getAllCourses</result>`

但是看了一个人的说法：
原则上是不能在 action 之间跳转的，因为每个 action 代表了处理一件事，他们不应该相互关联。

感觉他说的好有道理。看来是我设计上有问题。


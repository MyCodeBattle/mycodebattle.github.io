---
title: TCP/IP - 万维网和 HTTP 笔记
layout: post
date: 2016-04-24
categories: TCP/IP
---

# HTTP

使用一条 TCP 连接，没有独立的控制连接，使用 80 端口。
它和 SMTP 协议的不同点在于 SMTP 使用了存储转发，而 HTTP 是直接交付。

## HTTP 事物


### 请求报文

请求报文通常包括一个请求行，一个首部，有时还有一个主体。

#### 请求行

请求报文中第一行是请求行，该行有三个子段，分别称为方法，URL 和版本，以空格符分割。
方法子段定义了请求类型。

在 HTTP 1.1 中，定义了几种方法：

|方法|   动作   |
|---| ----|
|GET| 请求服务器文档 |
|HEAD| 请求关于文档的信息，而不是文档本身 |
|POST | 从客户向服务器发送一些信息 |
|PUT| 从服务器向客户发送文档 |
|TRACE| 把到达的请求回送|
|CONNECT| 保留|
|DELETE | 删除 Web 网页 |
|OPTINOs| 询问关于可用的选项 |

#### 请求报文的首部行

#### 请求首部

#### 请求报文实体

#### 状态行

第一个字段定义了 HTTP 的版本，状态码字段定义了请求的状态。

100 系列提供信息，200 系列指示成功的请求，300 系列重定向到另一个 URL，400 系列指示客户端差错，500 系列指示服务器差错。

#### 响应报文首部行

## 持续连接

HTTP 1.1 以前是非持续连接，也就是为每一个请求建立一次 TCP 连接。

1.1 中，持续连接变成了默认的连接。

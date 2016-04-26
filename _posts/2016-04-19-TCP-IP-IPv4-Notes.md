---
title: TCP/IP 协议族 - IPv4 笔记
layout: post
date: 2016-04-19
categories: TCP/IP
---

# 引言

IP 是一种不可靠的无连接数据协议，依靠更高层来解决数据损伤、丢失等问题。

# 数据报

网络层的分组称为**数据报**。

![ip](http://www.zzxueshihou.com/uploads/allimg/120305/1_120305175054_1.jpg)

- 首部长度,  定义了数据报首部的长度，单位是 4 字节。
- 总长度, 定义了数据报总长度。数据长度 = 总长度 - 首部长度。
为什么需要这个东西呢？如果数据报被填充了，就能根据这个得出真实的数据有多少。
- 标识， 用于分片.
- 标志，用于分片。
- 分片偏移，用于分片。
- 生存时间，控制数据报的最大跳数。如果变成0就丢弃数据报，可以用来限制数据报在一个局域网内。
- 协议，标识封装了哪个上层协议。

# 分片

## 最大传送单元 (MTU)

数据链路层限制了可封装在一个帧中的最大长度。所以有时候数据报要分片。

第一次分片是被运输层，它会把数据分成 IP 与源点使用的数据链路层可接纳的大小。
如果已经分片的数据报遇到更小的 MTU 网络，这些数据报还会分片。

数据报可以被任意路由器分片，但是重组只能在目的主机上进行。

分片的时候，必须改变三个字段的值：

- 标志
- 分片偏移
- 总长度

其余的各字段必须被复制。

## 与分片有关的字段

- 标识 (identification)，这个 16 位字段标志了从源主机发出的一个数据报。此标志与源 IP 地址的组合必须唯一地确定这个数据报，也就是说，
所有的分片都具有相同的 identification。
identification 是由一个计数器控制的，每产生一个数据报计数器加一。
- 标志 (flag)，这是 3 位的字段。第一位保留，第二位称为`不分片`位。如果这个值是1，机器就不能对数据报分片，如果无法通过任何可用的物理网络，
就丢弃数据报，并向源主机发送 ICMP 差错报文。第三位是`还有分片`位，如果是 1，说明不是最后一个。
- 分片偏移，这个 13 位字段表示的分片在整个数据报中的相对位置，偏移值以 **8字节** 为单位，因为他只有 13 位，要想跟上 16 位只能乘以 8 了。

# 选项

## 格式 

### 类型

共8位。


- 复制（1位），若是0，表示选项必须仅仅复制到第一个分片，否则表示选项必须复制到所有分片中。
- 类别（2位），定义了该选项的一般用途，若是00，表示选项用作数据报的控制。若是 10，表示用作排错和管理。

### 长度

定义了选项的总长度。


### 值

包含某些特定选项所需数据。

## 选项类型

### 无操作选项

是个 1 字节的选项，用作选项和选项之间的填充符。
00000001.

### 选项结束选项

只能用作最后一个选项。
00000000.

### 记录路由选项

00000111，用来记录经过的路由。

### 严格路由选项

10001001，如果数据报通过了某个未被列入的路由器，将丢弃并发送差错报文。

### 不严格路由选项

10000011，表中列出的路由器必须通过，但是可以通过其他的路由器。

### 时间戳

用来记录路由器处理数据报的时间。

---

上面六个选项中，不复制的选项开头是0，用于数据报控制的选项第 2、3 个位置是 00，否则是 10。

# 检验和

还没理解。

# 安全性

## 安全问题

### 分组窃取

入侵者可以窃取一个分组。

但是如果加密了的话窃取了也看不到内容。

### 分组篡改

这个可以通过**完整性机制**检测到。

### IP 伪装

可以通过**起源鉴别机制**检测 。

# IP 软件包

## 首部添加模块

接受来自高层协议的数据和目的 IP 地址。


```
Solution(data, des_address):
    把数据封装成为 IP 数据报
    计算检验和，插入到检验和字段
    把数据发送到相应的输入队列
    返回
```

## 处理模块

处理模块接收来自一个接口或者来自首部添加模块的数据报。

```
Solution(Datagram):
    从输入队列取出一个数据报
    if 目的地址和本地地址中的一个匹配:
        发送数据报到重装模块
        返回
    if 本机是路由器:
        TTL - 1
    if TTL <= 0:
        丢弃数据报
        发送 ICMP 差错报文
        返回
    把数据报发送到转发模块
    返回
```

## 队列

分为输入队列和输出队列。

## 路由表

## 转发模块

接受来自处理模块的 IP 分组。如果分组需要被转发，就发到这个模块。

转发模块找出下一站的 IP 地址以及发送该分组时应当经过的接口号，然后发送给分片模块。

## MTU 表

找出 MTU。

## 分片模块

分片模块咨询 MTU 表找出 MTU。如果数据报长度大于 MTU，就要进行分片。

```
Solution(Datagram):
    提取数据报长度
    if 长度 > MTU:
        if D 位被置 1:
            丢弃数据报
            发送 ICMP 差错报文
            返回
        else:
            计算最大长度
            把数据报划分为分片
            给每一个分片添加首部
            把每一个分片添加需要的选项
            发送分片
            返回
    else:
        发送数据报
```

## 重装表

还没看懂

## 重装模块

接受来自处理模块的，且已经到达最终目的地的数据报分片。
因为 IP 协议是无连接的，不能保证所有的分片按序到达。所以可能属于一个数据报的分片和另一个混在一起，所以使用了重装表。

```
Solution(Datagram):
    if 分片偏移是 0 且 M 位也是 0:
        把数据报发送到适当队列
        返回
    查找重装表中的相应表项
    if 未找到:
        创建一个新的项目
    在链表的适当地方插入分片
    if 所有分组已到达:
        重装分片
        交付数据报
        返回
    else:
        if 超时:
            丢弃所有的分片
            发送 ICMP 差错报文
    返回
```
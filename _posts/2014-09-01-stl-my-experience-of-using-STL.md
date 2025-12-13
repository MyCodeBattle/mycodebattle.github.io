---
categories: Posts
date: 2014-09-01 00:00:00
title: STL使用小记
tags: []
layout: post
---

今天突然想起前几个月刚接触STL容器的时候不知道从哪里下手，又找不到教程。现在就写一点自己使用STL容器的体会，希望给大家一些帮助。

以后会慢慢加上例题（如果我还能回想起我挖过这个坑的话

# vector

vector是一个可变长的数组。

## 用法：

```c++
vector<类型> 名字
```;  
例如  
```c++
vector<int> ve;
```  
```c++
vector<string> ve;
```

自己定义的结构体什么的也可以往里塞
    
    
    123456

| ```c++
struct POINT{	int x, y;};vector<POINT> ve;
```  

## 常用操作

```c++
ve.push_back(const value_type &val);
```  
作用是在数组后面增加一个元素。括号里填的是ve里装的东西的类型

```c++
ve.clear();
```清空ve里的所有元素。

```c++
ve.empty();
```判断ve是否为空，如果是返回true，否则false

```c++
ve.size();
```返回ve的长度。注意这里返回的类型是```c++
unsigned int
```,如果ve是空的```c++
ve.size() - 1
```就会爆掉。使用的时候一定要小心（做TC的时候被坑了一次）

```c++
ve.pop_back()
``` 删除数组里的最后一个元素。

vector支持随机访问，也可以使用迭代器访问。等下一起说

# queue

队列的容器。

## 用法

和vector一样。

```c++
queue<int> qu;
```  
```c++
queue<POINT> qu;
```

我一般都用它在BFS的时候存点。

## 常用操作

```c++
qu.push(const value_type &val);
``` 元素入队

```c++
qu.pop()
```元素出队

```c++
qu.front()
``` 获得队首元素

```c++
qu.empty()
``` 判断qu是否为空，是的话返回true

```c++
qu.size()
``` 获得qu的大小。

# priority_queue

## 用法

优先队列，默认从大到小排列。

```c++
priority_queue<int> pqu;
```

如果要装结构体的话，要重载结构体的小于号，或者自己写一个cmp函数。

cmp函数下面再讲。

一般在BFS的时候用的比较多，Dijkstra也有用到。

## 常用操作

```c++
pqu.push();
```

```c++
pqu.top();
``` 取出第一个元素

```c++
pqu.pop();
```

```c++
pqu.empty();
```

其实基本和queue差不多了。

## map
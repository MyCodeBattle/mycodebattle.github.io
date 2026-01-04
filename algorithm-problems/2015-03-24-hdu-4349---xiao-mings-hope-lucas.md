---
categories: Posts
date: 2015-03-24 00:00:00
title: HDU 4349 - Xiao Ming's Hope (Lucas定理)
tags: []
layout: post
---

## 题意

题目就是求$C_n^m \bmod 2 == 1$

由Lucas定理，转化到二进制下。

当n = 0时，m对应的位必须是0.当n=1时，随意。

所以最后的答案是$(1<<Number_of_Two(n))$

## 代码


```c++
int main()
{
    int n;
    while (~scanf("%d", &n))
        printf("%d\n", (1<<__builtin_popcount(n)));
    return 0;
}
```
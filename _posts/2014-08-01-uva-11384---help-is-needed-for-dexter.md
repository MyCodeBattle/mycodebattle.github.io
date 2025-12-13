---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 11384 - Help is needed for Dexter
tags: []
layout: post
---

## 传送门

[UVa 11384 - Help is needed for Dexter](http://www.bnuoj.com/v3/problem_show.php?pid=19802)

## 代码


```c++
#include <cstdio>
using namespace std;
 
int Fun(int n)
{
    if (n == 1)
        return 1;
    return Fun(n / 2) + 1;
}
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int n, i, j;
    while (~scanf("%d", &n))
        printf("%d\n", Fun(n));
    return 0;
}
```
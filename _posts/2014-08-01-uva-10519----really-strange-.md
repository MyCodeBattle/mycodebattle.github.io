---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 10519 - !! Really Strange !!
tags: []
layout: post
---

## 传送门

[UVa 10519 - !! Really Strange !!](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1460)

## 题意

n个圆圈做多能划分几个区域

## 思路

目测法

## 代码
    
    
    12345678910111213141516171819

| ```c++
import java.math.*;import java.io.*;import java.util.*; public class Main {         static public void main(String[] args) {        Scanner in = new Scanner(System.in);        while (in.hasNext()) {            BigInteger n = in.nextBigInteger();            if (n.compareTo(BigInteger.ZERO) == 0) {                System.out.println("1");                continue;            }            n = n.multiply(n.subtract(BigInteger.ONE)).add(BigInteger.valueOf(2));            System.out.println(n);        }    }}
```
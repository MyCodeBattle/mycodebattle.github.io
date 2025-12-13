---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 10344 - Ray Through Glasses
tags: []
layout: post
---

## 传送门

[UVa 10344 - Ray Through Glasses](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1275)

## 题意

计算第n次反射光线的条数。

## 思路

可以这么看。

第n次反射光线由两部分组成

  1. n - 1次的光线（当然要反射回来

  2. n - 2次从中间那条线反射回来的光线


所以$$dp[n] = dp[n - 1] + dp[n - 2]$$

Fibonacci

## 代码
    
    
    123456789101112131415161718

| ```c++
import java.math.*;import java.util.*;import java.io.*; public class Main {    public static void main(String[] args) {        Scanner in = new Scanner(System.in);        BigInteger[] dp = new BigInteger[1111];        dp[0] = BigInteger.valueOf(1);        dp[1] = BigInteger.valueOf(2);        for (int i = 2; i < 1111; i++)            dp[i] = dp[i - 1].add(dp[i - 2]);        while (in.hasNext()) {            int n = in.nextInt();            System.out.println(dp[n]);        }    }}
```
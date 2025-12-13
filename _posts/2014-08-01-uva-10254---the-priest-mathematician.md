---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 10254 - The Priest Mathematician
tags: []
layout: post
---

## 传送门

[UVa 10254 - The Priest Mathematician](http://vjudge.net/problem/viewProblem.action?id=21252)

## 题意

汉内塔问题，四个棒子

## 思路

参考了别人的题解，原来要先把小部分的答案打印出来再找规律（ ＴДＴ）

## 代码
    
    
    1234567891011121314151617181920212223242526

| ```c++
import java.math.*;import java.io.*;import java.util.*; public class Main {         static public void main(String[] args) {        Scanner in = new Scanner(System.in);        BigInteger[] dp = new BigInteger[10010];        dp[0] = BigInteger.ZERO;        int k = 1; int cnt = 0; BigInteger add = BigInteger.ONE;        for (int i = 1; i <= 10000; i++) {            dp[i] = dp[i - 1].add(add);            cnt++;            if (cnt == k) {                cnt = 0;                k++;                add = add.multiply(BigInteger.valueOf(2));            }        }        while (in.hasNext()) {            int n = in.nextInt();            System.out.println(dp[n]);        }    }}
```
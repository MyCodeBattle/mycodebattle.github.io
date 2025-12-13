---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 10183 - How Many Fibs?
tags: []
layout: post
---

## 传送门

[UVa 10183 - How Many Fibs?](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=115&problem=1124&mosmsg=Submission+received+with+ID+13976649)

## 思路

看到这么大的数字本来以为有别的办法的，看了题解才知道没有。

## 代码
    
    
    12345678910111213141516171819202122232425

| ```c++
import java.math.*;import java.io.*;import java.util.Scanner; public class Main {    public static void main(String[] args) {        Scanner cin = new Scanner(System.in);        BigInteger fibo[] = new BigInteger[500];        fibo[1] = BigInteger.ONE; fibo[2] = BigInteger.valueOf(2);        for (int i = 3; i < 500; i++)            fibo[i] = fibo[i - 1].add(fibo[i - 2]);        while (cin.hasNext()) {            BigInteger low = cin.nextBigInteger();            BigInteger high = cin.nextBigInteger();            if (low.compareTo(BigInteger.ZERO) == 0 && high.compareTo(BigInteger.ZERO) == 0)                break;            int cnt = 0;            for (int i = 1; i < 500; i++) {                if (fibo[i].compareTo(low) >= 0 && fibo[i].compareTo(high) <= 0)                    cnt++;            }            System.out.println(cnt);        }    }}
```
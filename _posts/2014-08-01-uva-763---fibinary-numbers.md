---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 763 - Fibinary Numbers
tags: []
layout: post
---

#  [UVa 763 - Fibinary Numbers](/2014/08/UVa-763/ "UVa 763 - Fibinary Numbers")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Aug 3 2014 21:55

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 763 - Fibinary Numbers](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=704)

## 题意

Fibonacci数给两个，求这两个数之和的Fibonacci数表示。

所谓Fibonacci数，和二进制差不多。最高位对应第n个Finonacci数，然后是1的就加起来。  
题目还要求要使和尽量大，这个没关系，从后面往前面减即可。

## 思路

把两个数转换为十进制数，再转换为Fibonacci数。

思路很简单，但是调试了快两个小时。原因在于输出的时候。  
一开始我是碰到一个就输出”1”，第一次跑了2989ms，吓cry了（ ＴДＴ）.  
接下来连续交了几次果断TLE.  
后来才知道这样的效率非常慢，正确的方法应该是string一个字符串，碰到1就加上，最后一起输出。  
不过这两个小时还是值得的（๑•̀ㅂ•́)و✧

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354

| 
    
    
    import java.math.*;import java.util.*;import java.io.*; public class Main {         static BigInteger[] dp = new BigInteger[111];         public static int find_start(BigInteger n) {        for (int i = 1; i < 105; i++)            if (dp[i].compareTo(n) > 0)                return i - 1;        return 0;    }         public static void main(String[] args) {        Scanner in = new Scanner(System.in);        boolean first = true;        dp[1] = BigInteger.valueOf(1);        dp[2] = BigInteger.valueOf(2);        for (int i = 3; i < 111; i++)            dp[i] = dp[i - 1].add(dp[i - 2]);        while (in.hasNext()) {            String fstr = in.next();            String sstr = in.next();            BigInteger sum = BigInteger.ZERO;            for (int i = 0; i < fstr.length(); i++)                if (fstr.charAt(i) == '1')                    sum = sum.add(dp[fstr.length() - i]);            for (int i = 0; i < sstr.length(); i++)                if (sstr.charAt(i) == '1')                    sum = sum.add(dp[sstr.length() - i]);            //System.out.println(sum);            if (!first)                System.out.printf("\n");            int ind = find_start (sum);            String ans = new String ("");            for (int i = ind; i >= 1; i--) {                if (dp[i].compareTo(sum) <= 0)                {                    ans += "1";                    sum = sum.subtract(dp[i]);                }                else ans += "0";            }            if (ind == 0)                ans += "0";            System.out.println(ans);            if (first) {                first = false;            }        }    }}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Java - BigInteger](/tags/Java-BigInteger/)

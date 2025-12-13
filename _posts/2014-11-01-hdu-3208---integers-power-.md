---
categories: Posts
date: 2014-11-01 00:00:00
title: HDU 3208 - Integer's Power (容斥原理)
tags: []
layout: post
---

#  [HDU 3208 - Integer's Power (容斥原理)](/2014/11/HDU-3208/ "HDU 3208 - Integer's Power \(容斥原理\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Nov 13 2014 18:00

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

一个数有一个power数，现在给出一个区间，求这个区间内的数的和。

## 思路

可以利用前缀和的思想，算出第一个数总共有的和，然后减去第二个数总共的和。

怎么算和呢？

因为pow(n, 1.0 / k)，得出的数是n之内有几个数能开k次方。  
那么我们可以对n开1次方、2次……直到开出的数<2

但是这里面有不合法的。比如$2^{2*3}$和$4^3$，显然64的值是6，能开3次方的数中4是无效的。  
如何除去这种数？  
算出每个被开方数i的倍数，如果该数有效（< 60)，dp[i] -= dp[j]。

pow精度被卡，学习了用Java二分。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354

| 
    
    
    import java.io.BufferedInputStream;import java.math.BigInteger;import java.util.Scanner;import java.math.*; public class Main {     static int MAXN = 60;     static long Pow(long num, int k) {         long l = 1, r = num + 1, mid, ans = 1;        while (l < r) {            mid = (l + r) / 2;            if (BigInteger.valueOf(mid).pow(k).compareTo(BigInteger.valueOf(num)) <= 0) {                //System.out.println(mid);                l = mid + 1;                ans = mid;            }            else r = mid;        }        return ans;    }     static long Sum(long k) {         long[] dp = new long[MAXN];        for (int i = 1; i < MAXN; i++) dp[i] = 0;        for (int i = 1; i < MAXN; i++) {            long n = Pow(k, i);            if (n < 2) break;            dp[i] = n - 1;            //System.out.println(n - 1);        }        for (int i = MAXN - 1; i > 0; i--) {            if (i * 2 >= MAXN) continue;            for (int j = i * 2; j < MAXN; j += i) dp[i] -= dp[j];        }        long ans = 0;        for (int i = 1; i < MAXN; i++) ans += i * dp[i];        //System.out.println(ans);        return ans;    }     public static void main(String[] args) {        Scanner in = new Scanner(new BufferedInputStream(System.in));        long a, b;        while (in.hasNext()) {            a = in.nextLong(); b = in.nextLong();            if (a + b == 0) break;            System.out.println(Sum(b) - Sum(a - 1));        }    }}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - HDU](/tags/Online-Judge-HDU/)[Math - Combinatorics](/tags/Math-Combinatorics/)[Java - BigInteger](/tags/Java-BigInteger/)

---
categories: Posts
date: 2014-11-01 00:00:00
title: URAL 1036 - Lucky Tickets (高精度 + 基本计数)
tags: []
layout: post
---

#  [URAL 1036 - Lucky Tickets (高精度 + 基本计数)](/2014/11/URAL-1036/ "URAL 1036 - Lucky Tickets \(高精度 + 基本计数\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Nov 21 2014 23:53

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

给出N，求有几种组合，使得前面N位数字的和和后面相等，并且相加为S。

## 思路

说好的容斥原理呢？（ ＴДＴ）人与人之间最基本的信任都没了。

题目可以转化为求S/2有几种表示方法。

用dp[i][j] = dp[i - 1][j - k]

dp[i][j]表示前i位和为j的方案数。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738

| 
    
    
    import java.io.BufferedInputStream;import java.math.BigInteger;import java.util.Scanner;import java.math.*;  public class Main {     static int MAXN = 1000 + 10;      public static void main(String[] args) {        Scanner in = new Scanner(new BufferedInputStream(System.in));        BigInteger[][] dp = new BigInteger[55][MAXN];        int S, i, j;        while (in.hasNextInt()) {            int n = in.nextInt();            S = in.nextInt();            if (S % 2 == 1) {                System.out.println("0");                continue;            }            S /= 2;            for (i = 0; i <= n; i++) {                for (j = 0; j <= S; j++) dp[i][j] = BigInteger.ZERO;            }            dp[0][0] = BigInteger.ONE;                          for (i = 1; i <= n; i++) {                for (j = 0; j <= S; j++) {                    for (int k = 0; k < 10; k++) {                        if (k > j) continue;                        dp[i][j] = dp[i][j].add(dp[i - 1][j - k]);                    }                }            }            System.out.println(dp[n][S].multiply(dp[n][S]));        }    }}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - URAL](/tags/Online-Judge-URAL/)[Java - BigInteger](/tags/Java-BigInteger/)[Math - Combinatorics](/tags/Math-Combinatorics/)

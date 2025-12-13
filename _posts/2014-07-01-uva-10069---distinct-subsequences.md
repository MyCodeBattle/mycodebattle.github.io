---
categories: Posts
date: 2014-07-01 00:00:00
title: UVa 10069 - Distinct Subsequences
tags: []
layout: post
---

#  [UVa 10069 - Distinct Subsequences](/2014/07/UVa-10069/ "UVa 10069 - Distinct Subsequences")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Jul 9 2014 10:10

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 10069 - Distinct Subsequences](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=114&problem=1010&mosmsg=Submission+received+with+ID+13853961)

## 题意

B是A的子序列，求A中有几个B。

## 思路

没思路，参考了[BearChild的解题报告](http://blog.csdn.net/keshuai19940722/article/details/11142089)  
用dp[i][j]表示a字符串的前j长度中包含b字符串前i字符的数量。  
状态转移方程

> a[j] = b[i], dp[i][j] = dp[i- 1][j - 1] + dp[i][j - 1]  
> a[j] != b[i], dp[i][j] = dp[i][j - 1]

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132

| 
    
    
    import java.math.*;import java.io.*;import java.text.*;import java.util.*;public class Main {     public static void main(String[] args) {        Scanner cin = new Scanner (new BufferedInputStream (System.in));        BigInteger dp[][] = new BigInteger[110][11000];        String a, b;        int T, i, j;        T = cin.nextInt();        while (T-- > 0) {            a = cin.next();            b = cin.next();            int alen = a.length();            int blen = b.length();            for (i = 0; i <= alen; i++) {                dp[0][i] = BigInteger.ONE;            }            for (i = 1; i <= blen; i++) {                dp[i][0] = BigInteger.ZERO;                for (j = 1; j <= alen; j++) {                    dp[i][j] = dp[i][j - 1];                    if (b.charAt(i - 1) == a.charAt(j - 1)) {                        dp[i][j] = dp[i][j].add(dp[i - 1][j - 1]);                    }                }            }            System.out.println(dp[blen][alen]);        }    }}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Dynamic Programming](/tags/Dynamic-Programming/)[Online Judge - UVa](/tags/Online-Judge-UVa/)[Must Be Done Again](/tags/Must-Be-Done-Again/)

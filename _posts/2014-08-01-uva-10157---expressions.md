---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 10157 - Expressions
tags: []
layout: post
---

## 传送门

[UVa 10157 - Expressions](http://vjudge.net/problem/viewProblem.action?id=21250)

## 思路

$$f(i, j) = \sum _{h=0}^{k=n - 1}f\left( k,d-1\right) \cdot f\left( n-k-1,d\right) $$

$f(i, j)$表示前i个里深度至多为j的个数。

答案为$f(i, j) - f(i, j - 1)$

## 代码


```c++
import java.math.*;
import java.io.*;
import java.util.*;
 
public class Main {
     
    static BigInteger[][] dp = new BigInteger[310][160];
    static public BigInteger DFS(int n, int d) {
        if (dp[n][d] != null)
            return dp[n][d];
        if (n == 0)
            return dp[n][d] = BigInteger.ONE;
        if (d == 0)
            return dp[n][d] = BigInteger.ZERO;
        dp[n][d] = BigInteger.ZERO;
        for (int i = 0; i < n; i++)
            dp[n][d] = dp[n][d].add(DFS(n - i - 1, d).multiply(DFS(i, d - 1)));
        return dp[n][d];
    }
         
    static public void main(String[] args) {
        Scanner in = new Scanner(new BufferedInputStream(System.in));
        while (in.hasNext()) {
            int n = in.nextInt();
            int d = in.nextInt();
            if ((n & 1) == 1) {
                System.out.println("0");
                continue;
            }
            n /= 2;
            if (d == 0)
                System.out.println("0");
            else
                System.out.println(DFS(n, d).subtract(DFS(n, d - 1)));
        }
    }  
}
```
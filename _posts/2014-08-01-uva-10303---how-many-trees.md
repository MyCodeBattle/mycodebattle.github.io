---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 10303 - How Many Trees?
tags: []
layout: post
---

## 传送门

[UVa 10303 - How Many Trees?](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=115&problem=1244&mosmsg=Submission+received+with+ID+13978433)

## 题意

有n个数字，求这n个数字可以组成的二叉搜索树的数目。

## 思路

引用一下Titanium的解释。

> 当空树即n=0时方案数为1，当n=1时方案数同样为1。当n>=2时，我们把n个数按升序排列，如果我们选ai作为数树根，那么a1……ai-1必定在右子树，ai+1……an必定在左子树，左子树有i-1个元素，同样是排序二叉树，相当于问这个i-1个元素又能组成多少个二叉排序树，右子树有n-i个元素，同时是二叉排序树，相当于问这n-i个元素能组成多少个二叉排序树，方案数为两者相乘。
> 
> 对于每个ai作为树根的计算方法如上，而所有的ai都能作为树根，所以不难总结出公式

$$h(n)= h(0) * h(n-1)+h(1) * h(n-2) + … + h(n-1)h(0) (n>=2)$$

实际上就是这个递推公式

$$h(n)=h(n-1) * (4*n-2)/(n+1)$$

## 代码


```c++
import java.math.*;
import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        BigInteger[] dp = new BigInteger[1100];
        dp[1] = BigInteger.ONE;
        for (int i = 2; i < 1100; i++)
            dp[i] = dp[i - 1].multiply(BigInteger.valueOf(4 * i - 2)).divide(BigInteger.valueOf(i + 1));
        while (in.hasNext()) {
            int n = in.nextInt();
            System.out.println(dp[n]);
        }
    }
}
```
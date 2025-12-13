---
categories: Posts
date: 2014-08-01 00:00:00
title: UVa 10862 - Connect the Cable Wires
tags: []
layout: post
---

#  [UVa 10862 - Connect the Cable Wires](/2014/08/UVa-10862/ "UVa 10862 - Connect the Cable Wires")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Aug 3 2014 16:01

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 10862 - Connect the Cable Wires](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1803)

## 题意

有一个供应站和几个仓库，每个仓库可以从供应站获得资源，也可以从相邻的仓库获得，求N个仓库的时候总共的方式。

## 思路

考虑第n个仓库的时候。

它可以连供应站，然后前面的仓库按照之前的方法连。这时候的方式是$dp[n - 1]$.

它也可以连左边的仓库。前面的仓库也是按照之前的方法连，这时候的方式是$dp[n - 1] + dp[n - 1]$。

然后想到这里就断掉了，因为我想破脑袋也只能想到这两种情况。

看了Staginner的题解才知道新增的这个仓库既连供应站又连前一个仓库。这样的话就可以看成一个整体了。这个整体可以和整体的前面那个仓库连，也可以不连。连的时候，又是一个整体。。。。。。

所以最后的公式是

$$dp[n] = 2 * dp[n - 1] + dp[n - 2] + … + dp[1]$$

$$dp[n - 1] = 2 * dp[n - 2] + dp[n - 3] + … + dp[1]$$

相减得

$$dp[n] = 3 * dp[n - 1] - dp[n - 2]$$

## 代码
    
    
    123456789101112131415161718192021

| 
    
    
    import java.math.*;import java.util.*;import java.io.*; public class Main {    public static void main(String[] args) {        Scanner in = new Scanner(System.in);        BigInteger[] dp = new BigInteger[2014];        dp[1] = BigInteger.valueOf(1);        dp[2] = BigInteger.valueOf(3);        for (int i = 3; i < 2014; i++)            dp[i] = dp[i - 1].multiply(BigInteger.valueOf(3)).subtract(dp[i - 2]);        while (true) {            int n = in.nextInt();            if (n == 0)                break;            System.out.println(dp[n]);        }     }}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Java - BigInteger](/tags/Java-BigInteger/)[Online Judge - UVa](/tags/Online-Judge-UVa/)

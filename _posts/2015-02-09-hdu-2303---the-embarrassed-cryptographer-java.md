---
categories: Posts
date: 2015-02-09 00:00:00
title: HDU 2303 - The Embarrassed Cryptographer (Java高精度)
tags: []
layout: post
---

## 题意

找出一个大数里有没有k以内的因子。

## 思路

Java水过

## 代码


```c++
import java.io.*;
import java.math.*;
import java.util.*;
 
public class Main {
    static int MAXN = (int)(1e6 + 10);
     
    static List<Integer> prime = new ArrayList<Integer>();
     
    static void GetPrimeTable() {
        int vis[] = new int[MAXN];
         
        int m = (int)Math.sqrt(MAXN + 0.5);
        for (int i = 2; i <= m; i++) if (vis[i] == 0) {
            for (int j = i*i; j < MAXN; j += i) {
                vis[j] = 1;
            }
        }
        for (int i = 2; i < MAXN; i++) {
            if (vis[i] == 0) {
                prime.add(i);
            }
        }
    }
         
    public static void main(String args[]) {
        GetPrimeTable();
        Scanner in = new Scanner(new BufferedInputStream(System.in));
        while (in.hasNextBigInteger()) {
            BigInteger a = in.nextBigInteger(), b = in.nextBigInteger();
            if (a.intValue() == 0 && b.intValue() == 0) break;
            int res = 0;
            for (int i = 0; prime.get(i) < b.intValue(); i++) {
                if (a.mod(new BigInteger(prime.get(i).toString())).intValue() == 0) {
                    res = prime.get(i);
                    break;
                }
            }
            if (res == 0) {
                System.out.println("GOOD");
            }
            else {
                System.out.println("BAD " + res);  
            }
        }
    }
}
```
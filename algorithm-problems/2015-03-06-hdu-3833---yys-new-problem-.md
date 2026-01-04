---
categories: Posts
date: 2015-03-06 00:00:00
title: HDU 3833 - YY's new problem (等差数列)
tags: []
layout: post
---

## 题意

判断1~N中有没有一个等差数列。

枚举公差，直接用数组判断。学过高等数学的我们知道这样的复杂度是$O(nlogn)$

## 代码


```c++
int arr[MAXN], n;
 
bool Solve()
{
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
        {
            if (i+(j<<1) > n) break;
            if (arr[i] < arr[i+j] && arr[i+j] < arr[i+j*2]) return true;
            if (arr[i] > arr[i+j] && arr[i+j] > arr[i+j*2]) return true;
        }
    return false;
}
int main()
{
    //ROP;
    int T;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
        {
            int tmp;
            scanf("%d", &tmp);
            arr[tmp] = i;
        }
        printf("%s\n", Solve() ? "Y" : "N");
    }
    return 0;
}
```
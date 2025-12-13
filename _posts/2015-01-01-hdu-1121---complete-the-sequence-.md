---
categories: Posts
date: 2015-01-01 00:00:00
title: HDU 1121 - Complete the Sequence (差分递推规律)
tags: []
layout: post
---

## 题意

找后面的k像，要求degree越小越好。

## 思路

完全没有思路。看了别人的题解才知道还有这么神奇的东西。

对给出的数组做n-1阶的差，最后得出一个常数。然后逆推就行了（作者原话）。  
然后我就对着逆推想了半天。果然是智商压制。

算是了解了一种新的题型吧。

## 代码


```c++
int dp[MAXN][MAXN];
 
int main()
{
    //ROP;
    int T;
    scanf("%d", &T);
    while (T--)
    {
        int n, k;
        scanf("%d%d", &n, &k);
        for (int i = 1; i <= n; i++) scanf("%d", &dp[0][i]);
        for (int i = 1; i < n; i++)
            for (int j = 1; i+j <= n; j++) dp[i][j] = dp[i-1][j+1] - dp[i-1][j];
        for (int i = 2; i <= k+1; i++) dp[n-1][i] = dp[n-1][1];
        for (int i = n-2; i >= 0; i--)
            for (int j = n-i; j <= n+k; j++) dp[i][j] = dp[i+1][j-1] + dp[i][j-1];
        for (int i = n+1; i < n+k; i++) printf("%d ", dp[0][i]);
        printf("%d\n", dp[0][n+k]);
    }
    return 0;
}
```
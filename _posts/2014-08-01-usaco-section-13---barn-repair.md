---
categories: Posts
date: 2014-08-01 00:00:00
title: USACO Section 1.3 - Barn Repair
tags: []
layout: post
---

## 题意

有一些牛仔牛棚里，现在要用M块木板拦住这些牛，求木板的最小长度。

## 思路

要让木板长度最小，就是要让浪费的最少，也就是空的地方要尽量少。

所以把空的长度排个序，减掉最长的N块即可。

要处理一下木板比牛多的情况。这时候一个牛一个木板

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243

| ```c++
/*ID: mycodeb1LANG: C++TASK: barn1*/ #include <bits/stdc++.h>using namespace std;const int MAXN = 200 + 10; int num[MAXN], itv[MAXN]; int cmp(const int i, const int j){    return i > j;} int main(){    //freopen("input.txt", "r", stdin);    freopen("barn1.in", "r", stdin);    freopen("barn1.out", "w", stdout);     int n, s, nb, i, j;    scanf("%d%d%d", &n, &s, &nb);    if (n >= nb)    {        printf("%d\n", nb);        return 0;    }    for (i = 0; i < nb; i++)        scanf("%d", #[i]);    sort(num, num + nb);    for (i = 1; i < nb; i++)        itv[i] = num[i] - num[i - 1];    sort(itv + 1, itv + nb, cmp);    int ans = num[nb - 1] - num[0] + 1;    for (i = 1; i < n; i++)        ans -= itv[i];    ans += n - 1;    printf("%d\n", ans);    return 0;}
```
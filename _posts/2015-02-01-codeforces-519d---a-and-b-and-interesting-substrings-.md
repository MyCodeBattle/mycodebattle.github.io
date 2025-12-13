---
categories: Posts
date: 2015-02-01 00:00:00
title: Codeforces 519D - A and B and Interesting Substrings (思维)
tags: []
layout: post
---

## 题意

要求找到子串的个数，使满足以下两个条件。

  1. i+1~j-1位置的字母的权之和为0.
  2. $str[i] = str[j]$


## 思路

一开始YY了半天，没思路。

后来想到第一个条件，可以通过前缀和$sum[j-1] = sum[i]$得出。又想到如果我把每个字母对应的前缀和都存起来，这样就可以快速得到答案了。

所以开一个26大的map数组，里面存的是对应的字符，所在位置的前缀和，和这个前缀和的出现次数。

遍历一遍字符。当查到到i这个位置时，判断```c++
map[str[i]]
```里是否有```c++
sum[i-1]
```，如果有的话就加上出现的次数。

然后更新一下```c++
map[str[i]][sum[i-1]]
```。

## 代码
    
    
    1234567891011121314151617181920212223

| ```c++
map<LL, int> G[30];char str[MAXN];int val[30];LL sum[MAXN]; int main(){    //ROP;    LL ans = 0;    for (int i = 0; i < 26; i++) scanf("%d", &val[i]);    scanf("%s", str+1);    int len = strlen(str+1);    for (int i = 1; i <= len; i++) sum[i] = sum[i-1] + val[str[i]-'a'];    for (int i = 1; i <= len; i++)    {        int idx = str[i]-'a';        if (G[idx].count(sum[i-1]))            ans += G[idx][sum[i-1]];        G[idx][sum[i]]++;    }    printf("%I64d\n", ans);    return 0;}
```
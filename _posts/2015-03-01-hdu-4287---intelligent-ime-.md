---
categories: Posts
date: 2015-03-01 00:00:00
title: HDU 4287 - Intelligent IME (思维)
tags: []
layout: post
---

## 题意

给出输入的字符，再给出按手机键盘的方式，问弹出几种已经输入的字符。

## 思路

直接映射。

这个专题的题目有点水。

## 代码


```c++
map<char, int> mp;
map<int, int> ans;
string word[] = {"abc","def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
int arr[MAXN];
char buf[20];
 
int main()
{
   // ROP;
    int T;
    scanf("%d", &T);
    for (int i = 0; i < 8; i++)
        for (int j = 0; j < SZ(word[i]); j++)
            mp[word[i][j]] = i+2;
    while (T--)
    {
        ans.clear();
        int n, k;
        scanf("%d%d", &n, &k);
        for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
        for (int i = 0; i < k; i++)
        {
            int tmp = 0;
            scanf("%s", buf);
            for (int j = 0; j < strlen(buf); j++) tmp = tmp*10 + mp[buf[j]];
            ans[tmp]++;
        }
        for (int i = 0; i < n; i++)
            printf("%d\n", ans[arr[i]]);
    }
    return 0;
}
```
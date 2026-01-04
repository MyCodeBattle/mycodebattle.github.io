---
categories: Posts
date: 2014-09-08 00:00:00
title: ZJU 3818 - Pretty Poem
tags: []
layout: post
---

## 传送门

[ZJU 3818 - Pretty Poem](http://acm.zju.edu.cn/onlinejudge/showProblem.do?problemCode=3818)

## 题意

问能不能构造出ABABA或者ABABCBA

## 思路

暴力枚举ABC

## 代码


```c++
#include <bits/stdc++.h>
#define LL long long
#define lowbit(x) ((x) & (-x))
const int MAXN = 50 + 5;
const int INF = 0x3f3f3f3f;
using namespace std;
 
char temp[MAXN];
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int T, i, j, n;
    scanf("%d%*c", &n);
    for (int ii = 0; ii < n; ii++)
    {
        string str;
        bool flag = false;
        char ch;
        scanf("%s", temp);
        for (i = 0; i < strlen(temp); i++)
            if (isalpha(temp[i])) str += temp[i];
        int len = str.size();
        for (i = 1; i * 2 < len; i++)
        {
            if (flag) break;
            for (j = 1; j * 2 + i * 3 <= len; j++)
            {
                string ab;
                int curLen = i * 3 + j * 2;
                string a = str.substr(0, i);
                string b = str.substr(i, j);
                if (a == b)
                    continue;
                if (curLen > len)
                    continue;
                else if (curLen == len)
                {
                    ab = a + b;
                    ab += ab;
                    string ans = ab + a;
                    if (ans == str)
                    {
                        flag = true;
                        break;
                    }
                }
                else
                {
                    ab = a + b;
                    ab += ab;
                    int k = 1;
                    while (k + ab.size() + a.size() + b.size() < len) k++;
                    string c = str.substr((i + j) * 2, k);
                    if (c == a || c == b)
                        continue;
                    string ans = ab + c + a + b;
                    if (ans == str)
                    {
                        flag = true;
                        break;
                    }
                }
            }
        }
        printf("%s\n", flag ? "Yes" : "No");
    }
    return 0;
}
```
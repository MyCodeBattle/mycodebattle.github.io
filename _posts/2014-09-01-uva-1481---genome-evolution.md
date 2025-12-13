---
categories: Posts
date: 2014-09-01 00:00:00
title: UVa 1481 - Genome Evolution
tags: []
layout: post
---

#  [UVa 1481 - Genome Evolution](/2014/09/UVa-1481/ "UVa 1481 - Genome Evolution")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 18 2014 17:24

**Contents**

  1. 1. 传送门
  2. 2. 题意
  3. 3. 思路
  4. 4. 代码

## 传送门

[UVa 1481 - Genome Evolution](http://www.bnuoj.com/v3/problem_show.php?pid=11934)

## 题意

统计两个集合中连续的，长度并且元素都相同的子序列的数量

## 思路

一开始想枚举A的子集，然后字典序排一下，存在MAP里。不过这样$O(n^3logn)$，明显超时了。

转换一下思路。记录A集合中的各个元素在B集合中的位置。对于一个长度为len的A的子集，如果他的元素在B中的最大位置-最小位置 + 1 等于len，说明这个序列的其他元素都在他们中间，也就是说这个序列也在中存在。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445

| 
    
    
    #include<bits/stdc++.h>#define LL long long#define lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)const int MAXN = 3000 + 5;const int INF = 0x3f3f3f3f;using namespace std; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int a[MAXN], b[MAXN], pos[MAXN]; int main(){    //freopen("input.txt", "r", stdin);    int n, i, j;    while (scanf("%d", &n), n)    {        for (i = 0; i < n; i++) scanf("%d", a + i);        for (i = 0; i < n; i++) scanf("%d", b + i);        for (i = 0; i < n; i++)            for (j = 0; j < n; j++)                if (a[i] == b[j])                {                    pos[a[i]] = j;                    break;                }        int ans = 0, maxPos, minPos;        for (i = 0; i < n - 1; i++)        {            maxPos = minPos = pos[a[i]];            for (j = i + 1; j < n; j++)            {                int len = j - i + 1;                maxPos = max(maxPos, pos[a[j]]);                minPos = min(minPos, pos[a[j]]);                if (maxPos - minPos + 1 == len) ans++;            }        }        printf("%d\n", ans);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)

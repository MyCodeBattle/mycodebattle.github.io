---
categories: Posts
date: 2014-08-01 00:00:00
title: Codeforces Round - 260 (Div. 2) A ~ C
tags: []
layout: post
---

#  [Codeforces Round - 260 (Div. 2) A ~ C](/2014/08/Codeforces-Round-260-Div2/ "Codeforces Round - 260 \(Div. 2\) A ~ C")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Aug 9 2014 11:22

**Contents**

  1. 1. A. Laptops
    1. 1.1. 传送门
    2. 1.2. 题意
    3. 1.3. 代码
  2. 2. B. Fedya and Maths
    1. 2.1. 传送门
    2. 2.2. 思路
    3. 2.3. 代码
  3. 3. C. Boredom
    1. 3.1. 传送门
    2. 3.2. 题意
    3. 3.3. 思路
    4. 3.4. 代码

## A. Laptops

### 传送门

[A. Laptops](http://codeforces.com/contest/456/problem/A)

### 题意

其实我现在还搞不懂题意。Alex说质量和价格成反比，我还以为全部电脑都要满足才是Happy Alex，到比赛结束都没做出来。

早上看了一下其他人的原来有一个电脑满足就行？（求解释）

/************************************************************/

经**Ted** 解惑，终于明白了。引用一下他说的话

> A题的题目里面Alex说有这样的两台笔记本(Alex thinks that there are two laptops, such that….)，然后题目最后说问在测试数据中是否存在如Alex所说的两台电脑(Determine whether two described above laptops exist.)。

感谢(ˉ▽￣～)

### 代码
    
    
    123456789101112131415161718192021

| 
    
    
    #include <bits/stdc++.h>using namespace std;#define LL long long#pragma comment(linker, "/STACK:102400000,102400000") int main(){    int a, b, i, n;    scanf("%d", &n);    for (i = 0; i < n; i++)    {        scanf("%d%d", &a, &b);        if (a != b)        {            printf("Happy Alex\n");            return 0;        }    }    printf("Poor Alex\n");    return 0;}  
  
---|---  
  
## B. Fedya and Maths

### 传送门

[B. Fedya and Maths](http://codeforces.com/contest/456/problem/B)

### 思路

它们的和mod5就是分别mod5的和mod5，而四个数分别mod5时，每个数都有循环节存在。

1就不用说了

2的话是1 2 4 3 1 2 4 3 1….

以此类推

然后把它们加起来可以发现，答案的循环节是0 0 0 4 0 0 0 4 0 0 0 4，所以如果能整除4就输出4，不然就输出0.

能整除4的话就是末尾两位能整除。

### 代码
    
    
    123456789101112131415161718

| 
    
    
    #include <bits/stdc++.h>using namespace std;#define LL long long#pragma comment(linker, "/STACK:102400000,102400000")const int MAXN = 1e5 + 10; char str[MAXN]; int main(){    int n, i, j;    gets(str);    int len = strlen(str);    char c = str[len - 1], d = str[len - 2];    int k = c - '0' + (d - '0') * 10;    printf("%d\n", k % 4 ? 0 : 4);    return 0;}  
  
---|---  
  
## C. Boredom

### 传送门

[C. Boredom](http://codeforces.com/contest/456/problem/C)

### 题意

小明在玩一个消消乐游戏，他可以选择一个数，然后就会消去这个数+1，-1的数，得到这个数的个数*这个数的分数，问他最多能得多少分。

### 思路

考虑DP。

对于每一个数，可以选择选不选。如果选的话，就加上前前个结果，不选的话，最大值就是上一个结果。

$$dp[i] = max(i * dp[i] + dp[i - 2], dp[i - 1])$$

### 代码
    
    
    1234567891011121314151617181920212223

| 
    
    
    #include <bits/stdc++.h>using namespace std;#define LL long long#pragma comment(linker, "/STACK:102400000,102400000")const int MAXN = 1e5 + 10; LL dp[MAXN]; int main(){    //freopen("input.txt", "r", stdin);    int n, i, j, a;    scanf("%d", &n);    for (i = 0; i < n; i++)    {        scanf("%d", &a);        dp[a]++;    }    for (i = 2; i < MAXN; i++)        dp[i] = max(i * dp[i] + dp[i - 2], dp[i - 1]);    printf("%I64d\n", dp[100000]);    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - Codeforces](/tags/Online-Judge-Codeforces/)

---
categories: Posts
date: 2014-08-01 00:00:00
title: Codeforces Round - 262 (Div. 2)
tags: []
layout: post
---

## A - Vasya and Socks

### 思路

小明一天早上用一双袜子，老妈每隔n天的那天晚上才给他一双，求什么时候用完

我是用暴力纯模拟的TAT

### 代码
    
    
    1234567891011121314151617181920212223

| ```c++
#include <bits/stdc++.h>using namespace std;#define LL long long#define MP(a, b) make_pair(a, b)const int MAXN = 1e5 + 10;const int INF = 0x3f3f3f3f; int main(){    //freopen("input.txt", "r", stdin);    int n, m, i, j, cnt = 0;    scanf("%d%d", &n, &m);    int res = n;    while (res > 0)    {        cnt++;        if (cnt % m == 0)            res++;        res--;    }    printf("%d\n", cnt);    return 0;}
```  

## B - Little Dima and Equation

枚举每个数显然是不现实的，所以要枚举s(x)，范围只有1 ~ 81，然后验证一下位数之和是不是s(x)  
昨天晚上脑子秀逗了，不知怎么就算成72

还要注意处理一下负数的情况

### 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435363738394041424344454647

| ```c++
#include <bits/stdc++.h>using namespace std;#define LL long long#define MP(a, b) make_pair(a, b)const int MAXN = 1e5 + 10;const int INF = 0x3f3f3f3f; vector<LL> ve; int Get(LL v){    if (v < 0 || v >= 1e9)        return -1;    int ans = 0;    while (v)    {        ans += v % 10;        v /= 10;    }    return ans;} int main(){    //freopen("input.txt", "r", stdin);    LL a, b, c;    LL i;    int ans = 0;    scanf("%I64d%I64d%I64d", &a, &b, &c);    for (i = 1; i <= 81; i++)    {        LL k = 1;        for (int l = 0; l < a; l++)            k *= i;        LL t = b * k + c;        if (Get(t) == i)        {            ans++;            ve.push_back(t);        }    }    sort(ve.begin(), ve.end());    printf("%d\n", ans);    for (i = 0; i < ve.size(); i++)        i != ve.size() - 1 ? printf("%I64d ", ve[i]) : printf("%I64d\n", ve[i]);    return 0;}
```  

## C - Present

### 题意

小明有一些花，每天可以给w范围的花增长1米，问m天过后最矮的花的最高值

### 思路

最小值最大化，二分。

在检查是否合理的时候，一开始我是用模拟的。。memcpy一个数组，然后一个个加过去，TLE了。

用一个变量add记录当前花已经增长的高度（被之前的影响了），用一个temp数组记录当前花增长的高度（用于确定当前对以后的影响）  
然后记录一下天数即可。

### 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061

| ```c++
#include <cstdio>#include <algorithm>#include <cstring>using namespace std;const int MAXN = 1e5 + 10;const int INF = 0x3f3f3f3f; int flw[MAXN], hmax = -1, hmin = INF, temp[MAXN], w, m, n; bool Check(int mid){    int cnt = 0, add = 0;    memset(temp, 0, sizeof temp);    for (int i = 0; i < n; i++)    {        if (i >= w)            add -= temp[i - w];        if (add + flw[i] < mid)        {            temp[i] = mid - (add + flw[i]);            add += temp[i];            cnt += temp[i];            if (cnt > m)                return false;        }    }    return true;} int Solve(){    int l = hmin, r = hmax, mid, ans;    while (l <= r)    {        mid = l + (r - l) / 2;        if (Check(mid))        {            ans = mid;            l = mid + 1;        }        else            r = mid - 1;    }    return ans;} int main(){    //freopen("input.txt", "r", stdin);    int i, j;    scanf("%d%d%d", &n, &m, &w);    for (i = 0; i < n; i++)    {        scanf("%d", &flw[i]);        hmax = max(hmax, flw[i]);        hmin = min(hmin, flw[i]);    }    hmax += m;    printf("%d\n", Solve());    return 0;}
```
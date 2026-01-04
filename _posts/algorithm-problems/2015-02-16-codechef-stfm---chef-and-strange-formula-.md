---
categories: Posts
date: 2015-02-16 00:00:00
title: CodeChef STFM - Chef and Strange Formula (康托展开)
tags: []
layout: post
---

## 思路

康托展开$X=a[n]*(n-1)!+a[n-1]*(n-2)!+...+a[i]*(i-1)!+...+a[1]*0!$

那么对照一下题目里的公式。

$F(x) = 1*1!+ 2*2!+ 3*3!+ ... + x*x! + (1+2+3..+x) * x$

后面的和大家都会算。

前面一时找不到规律，后来请教了hcbbt巨巨。他一眼就看出是康托展开！

前面就是序列  
x+1, x, x-1, …, 2, 1 的康托展开。

显然x+1个元素的排列为$(x+1)!$，因为是从0开始计算，所以上面这个排列的康托展开就是$(x+1)!-1$

所以$F(x) = (x+1)!- 1 + x* \frac {x+1}{2}$

之前算的时候不知道大阶乘的模怎么算。今天看别人代码才想到如果阶乘大于模那么值就是0。  
真的怀疑当时自己脑子抽了。

## 代码


```c++
#include <stack>
#include <cstdio>
#include <list>
#include <set>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <functional>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <string>
#include <map>
#include <cmath>
using namespace std;
#define LL long long
#define ULL unsigned long long
#define SZ(x) (int)x.size()
#define Lowbit(x) ((x) & (-x))
#define MP(a, b) make_pair(a, b)
#define MS(arr, num) memset(arr, num, sizeof(arr))
#define PB push_back
#define X first
#define Y second
#define ROP freopen("input.txt", "r", stdin);
#define MID(a, b) (a + ((b - a) >> 1))
#define LC rt << 1, l, mid
#define RC rt << 1|1, mid + 1, r
#define LRT rt << 1
#define RRT rt << 1|1
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
const double eps = 1e-8;
const int MAXN = 1e7 + 10;
const int MOD = 1e9 + 7;
const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };
const int hash_size = 4e5 + 10;
int cases = 0;
typedef pair<int, int> pii;
 
LL Fac[MAXN], m;
 
inline LL Mod(LL n)
{
    return n % m;
}
 
int main()
{
    //ROP;
    LL n;
    cin >> n >> m;
    Fac[0] = 1;
    for (int i = 1; i <= m; i++) Fac[i] = Mod(Fac[i-1] * i);
    LL ans = 0;
    for (int i = 0; i < n; i++)
    {
        //先计算sum
        LL tmp, tmpAns = 0;
        cin >> tmp;
        if (tmp & 1) tmpAns = Mod(Mod(tmp) * Mod(Mod(tmp) * Mod((tmp+1)/2)));
        else tmpAns = Mod(Mod(tmp) * Mod(Mod(tmp>>1) * (Mod(tmp+1))));
        //compute factorial
        LL fac;
        if (tmp >= m-1) fac = 0;
        else fac = Fac[tmp+1];
        tmpAns = Mod(tmpAns + fac - 1);
        ans = Mod(ans + tmpAns);
    }
    cout << ans << endl;
    return 0;
}
```
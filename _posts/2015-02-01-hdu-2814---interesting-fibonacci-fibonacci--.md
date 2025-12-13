---
categories: Posts
date: 2015-02-01 00:00:00
title: HDU 2814 - Interesting Fibonacci (Fibonacci性质 + 循环节)
tags: []
layout: post
---

#  [HDU 2814 - Interesting Fibonacci (Fibonacci性质 + 循环节)](/2015/02/HDU-2814/ "HDU 2814 - Interesting Fibonacci \(Fibonacci性质 + 循环节\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Feb 20 2015 18:22

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

$G(1) = F(a^b)$  
$G(n) = G(n-1)^{F(a^b)} (n>=2)$

求$G(n) \bmod c$

## 思路

求$a^b \bmod c$还有这么一个公式.

$$a^b \equiv (a \bmod c)^{b \bmod \phi(c) + \phi(c)} (\bmod c), b >= \phi(c)$$

所以这个题目就变成了求  
$$ans = F(a^b)^{ F(a^b)^{n-1} } \bmod c = (F(a^b) \bmod c)^{F(a^b) \bmod \phi(c) + \phi(c)} \bmod c$$

而Fibonacci数列有一个性质，它的n次方取模会出现一个循环节。假设循环节长度为$len$

$F(a^b) \bmod c = F(a^b \bmod len) \bmod c$

所以只要求出循环节的长度就行。

注意要特判$\phi(c) = 1$和$c = 1$的情况。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114

| 
    
    
    #include <stack>#include <cstdio>#include <list>#include <cassert>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 2e4 + 10;const int MOD = 1e9 + 7;const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };const int hash_size = 4e5 + 10;int cases = 0;typedef pair<int, int> pii; ULL F[3000]; int get_phi(int n){    int m = (int)sqrt(n+0.5);    int ans = n;    for (int i = 2; i <= m; i++) if (n%i == 0)    {        ans = ans / i * (i-1);        while (n % i == 0) n /= i;    }    if (n > 1) ans = ans / n * (n-1);    return ans;} ULL pow_mod(ULL a, ULL m, ULL n){    a %= n;    ULL ret = 1;    while (m)    {        if (m & 1) ret = ret*a%n;        a=a*a%n;        m >>= 1;    }    return ret;} int get_loop(int num){    F[0] = 0; F[1] = 1; F[2] = 1;    for (int i = 3; ; i++)    {        F[i] = (F[i-1]%num + F[i-2]%num) % num;        if (F[i] == 1 && F[i-1] == 0) return i-1;    }} int main(){    //ROP;    ios::sync_with_stdio(0);     int T;    cin >> T;    while (T--)    {        ULL a, b, n, c;        cin >> a >> b >> n >> c;        if (c == 1)        {            cout << "Case " << ++cases << ": 0" << endl;            continue;        }        ULL oula = get_phi(c);        int loop = get_loop(c);        ULL c1 = pow_mod(a, b, loop);        c1 = F[c1];        if (oula == 1)        {            cout << "Case " << ++cases << ": " << c1 << endl;            continue;        }        loop = get_loop(oula);        ULL t1 = pow_mod(a, b, loop);        t1 = F[t1];        ULL mi = pow_mod(t1, n-1, oula) + oula;        cout << "Case " << ++cases << ": " << pow_mod(c1, mi, c) << endl;    }     return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - HDU](/tags/Online-Judge-HDU/)[Math - Number Theory](/tags/Math-Number-Theory/)

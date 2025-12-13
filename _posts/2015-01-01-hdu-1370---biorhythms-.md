---
categories: Posts
date: 2015-01-01 00:00:00
title: HDU 1370 - Biorhythms (中国剩余定理)
tags: []
layout: post
---

## 思路

了解了一下中国剩余定理

$x \equiv B[0](\bmod W[1])$  
$x \equiv B[1](\bmod W[2])$  
…  
$x \equiv B[n](\bmod W[n])$

其中W、B已知，W[i] > 0 且W[i]与W[j]互质，求X

$a = (M_1 * M_{1}^{'} * B_1) + (M_2 * M_{2}^{'} * B_2) + ... + (M_k * M_{k}^{'} * B_k) \bmod LCM$

其中

$LCM = W_1 * W_2 * ... * W_k$, $M_{i}^{'} = m / W_i$ $M_{i}^{'}是M_{i}关于模W[i]的逆元$, $M_i * M_{i}^{'} \equiv 1 (\bmod W[i])$

根据欧几里得扩展求出$M_i * M_{i}^{'} + W_i * x = 1$

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839

| ```c++
void Extend_GCD(LL a, LL b, LL &d, LL &x, LL &y){    if (!b) d = a, x = 1, y = 0;    else { Extend_GCD(b, a%b, d, y, x); y -= x * (a/b); }} LL China(int n, int *a, int *m) //n个方程：x≡a[i](mod m[i]){    LL M = 1, d, y, x = 0;    for (int i = 0; i < n; i++) M *= m[i];    for (int i = 0; i < n; i++)    {        LL w = M / m[i];        Extend_GCD((LL)m[i], w, d, d, y);        x = (x + y*w*a[i]) % M;    }    if (x != 0) return (x+M) % M;    else return x+M;} int arr[10], m[10]; int main(){    //ROP;    int tmp;    cin >> tmp;    m[0] = 23; m[1] = 28, m[2] = 33;    int a, b, c, d, lcm = 23*28*33;    while (cin >> a >> b >> c >> d)    {        if (a + b + c + d == -4) break;        arr[0] = a, arr[1] = b, arr[2] = c;        int ans = (China(3, arr, m) - d + lcm)%lcm;        if (ans == 0) ans += lcm;        cout << "Case " << ++cases << ": the next triple peak occurs in " << ans << " days."<< endl;    }    return 0;}
```
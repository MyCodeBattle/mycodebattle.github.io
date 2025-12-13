---
categories: Posts
date: 2015-01-20 00:00:00
title: Project Euler
tags: []
layout: post
---

## Multiples of 3 and 5

字面意思


```c++
int main()
{
    int ans = 0;
    for (int i = 1; i < 1000; i++)
        if (i % 5 == 0 || i % 3 == 0) ans += i;
    printf("%d\n", ans);
}
```
 

## Even Fibonacci numbers

输出400W以内的Fibonacci数列中的偶数项的和


```c++
int main()
{
    const int MAX = 4e6;
    ULL ans = 0;
    int fir = 1, sec = 2, tmp = 3;
    while (1)
    {
        if (tmp > MAX) break;
        if (!(tmp&1)) ans += tmp;
        fir = sec + tmp;
        swap(fir, tmp);
        swap(fir, sec);
    }
    cout << ans + 2 << endl;
}
```
 

## Largest prime factor

输出给定的数的最大素数项


```c++
int main()
{
    LL num = 600851475143ll;
    set<int> st;
    for (LL i = 2; i <= (LL)sqrt(600851475143ll); i++)
    {
        while (num % i == 0)
        {
            st.insert(i);
            num /= i;
        }
    }
    cout << *st.rbegin() << endl;
    return 0;
}
```
 

## Largest palindrome product

输出三位数相乘最大的回文数


```c++
bool Check(int num)
{
    char str[10];
    MS(str, 0);
    sprintf(str, "%d", num);
    string s = str, comp = s;
    reverse(s.begin(), s.end());
    if (s == comp) return true;
    return false;
}
  
int main()
{
    int ans = 0;
    for (int i = 100; i < 1000; i++)
        for (int j = 100; j < 1000; j++)
            if (Check(i * j)) ans = max(ans, i * j);
    cout << ans << endl;
}
```
 

## Smallest multiple

输出1~20的最小公倍数


```c++
int main()
{
    int res = 1;
    for (int i = 2; i <= 20; i++)
        res = res / __gcd(res, i) * i;
    cout << res << endl;
    return 0;
}
```
 

## Sum square difference

$$5050^{2} - \frac{100(100 + 1)(2*100 + 1)}{6}$$
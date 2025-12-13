---
categories: Posts
date: 2015-01-01 00:00:00
title: HDU 1920 - Jackpot (LCM)
tags: []
layout: post
---

## 代码
    
    
    123456789101112131415161718192021222324252627

| ```c++
int main(){    int T;    const LL MAX = 1e9;    cin >> T;    while (T--)    {        LL tmp, ans = 1;        int n;        cin >> n;        bool flag = false;        while (n--)        {            cin >> tmp;            if (flag) continue;            ans = ans / __gcd(ans, tmp) * tmp;            if (ans >= MAX)            {                flag = true;                continue;            }        }        if (flag) cout << "More than a billion." << endl;        else cout << ans << endl;    }    return 0;}
```
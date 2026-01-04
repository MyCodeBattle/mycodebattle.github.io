---
categories: Posts
date: 2015-01-02 00:00:00
title: PKU 1061 - 青蛙的约会 (扩展欧几里得)
tags: []
layout: post
---



## 思路

了解了一下扩展欧几里得。。

设经过的时间为t。

$ (X + mt) - (Y + nt) = kL$，化简得$(n - m)t + Ly = X - Y$，符合$ax+by=c$的形式，可以用扩展欧几里得解出$ax+by=gcd(a, b)$的时候的一个解$x_0$。

两边同时乘以$\frac{c}{d}$，可得一个解x。

但是这时候的x可能是负数，因为通解为$x + k* \frac{b} {g}$，所以对$\frac{b}{g}$取余就行

## 代码

```
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
    #define LRT rt << 1#define RRT rt << 1|1
    #define BitCount(x) __builtin_popcount(x)
    #define BitCountll(x) __builtin_popcountll(x)
    #define LeftPos(x) 32 - __builtin_clz(x) - 1
    #define LeftPosll(x) 64 - __builtin_clzll(x) - 1const double PI = acos(-1.0);
    const int INF = 0x3f3f3f3f;
    const double eps = 1e-8;
    const int MAXN = 4e5 + 10;const int MOD = 1000007;
    const int dir[][2] = { {1, 0}, {0, 1} };int cases = 0;typedef pair<int, int> pii;
    typedef vector<int>::iterator viti;
    typedef vector<pii>::iterator vitii; 
    void gcd(LL a, LL b, LL &g, LL &x, LL &y){    
      if (!b) { g = a; x = 1; y = 0; }    else { gcd(b, a%b, g, y, x); y -= x * (a/b); }} int main(){    LL X, Y, m, n, L;    while (cin >> X >> Y >> m >> n >> L)    {        LL g, x, y;        LL b = L;        gcd(n-m, L, g, x, y);        cout << x << endl;        cout << y << endl;        if ((X-Y) % g != 0) cout << "Impossible" << endl;        else        {            LL p = b / g;            x = (X-Y) / g * x;            cout << (x % p + p) % p << endl;        }    }    return 0;}  ```

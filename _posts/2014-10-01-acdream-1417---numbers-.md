---
categories: Posts
date: 2014-10-01 00:00:00
title: ACDream 1417 - Numbers (枚举)
tags: []
layout: post
---

#  [ACDream 1417 - Numbers (枚举)](/2014/10/ACDream-1417/ "ACDream 1417 - Numbers \(枚举\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Oct 4 2014 22:08

**Contents**

  1. 1. 思路
  2. 2. 代码

## 思路

从1一直枚举到不超过n的10000…..，算出最接近1、10、等等的倍数，然后维护最小值

代码写得不优雅。。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <ctime>#include <cstdlib>#include <fstream>#include <string>#include <sstream>#include <map>#include <cmath>#define LL long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const LL MAXN = 1e18;const int MOD = 20071027; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int main(){    //ROP;    LL n, k;    int i, j;    while (cin >> n >> k, n + k)    {        char ans[] = "9999999999999999999999";        LL ori = 1;        if (k == 1)        {            cout << "1" << endl;            continue;        }        for (; ori > 0 && ori <= MAXN && ori <= n; ori *= 10)        {            if (ori % k == 0)            {                char str[20];                sprintf(ans, "%lld", ori);                break;            }            else            {                LL tmp = ori;                tmp += (k - tmp % k);                if (tmp > n) continue;                char str[20];                sprintf(str, "%lld", tmp);                if (strcmp(str, ans) < 0) strcpy(ans, str);            }        }        printf("%s\n", ans);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - ACDream](/tags/Online-Judge-ACDream/)[Foundation - Brute Force](/tags/Foundation-Brute-Force/)

---
categories: Posts
date: 2015-02-14 00:00:00
title: HDU 5175 - Misaki's Kiss again (数学)
tags: []
layout: post
---

## 思路

枚举一个数的全部因子，再由此枚举一个数的所有最大公约数。

然后可以通过异或得出另一个数，判断gcd是否等于当前的最大公约数

## 代码


```c++
#include <stack>
#include <cstdio>
#include <list>
#include <set>
#include <iostream>
#include <string>
#include <vector>
#include <climits>
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
const int MAXN = 100 + 10;
const int MOD = 1e9 + 7;
const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };
int cases = 0;
typedef pair<int, int> pii;
 
set<LL> mp, ans;
vector<LL> fac;
LL n;
 
void DFS(int pos, LL pro)
{
    if (pro >= n) return;
    LL tmp = (n^pro);   //最大公约数是pro，找出另一个异或的数，判断
    if (tmp < n && __gcd(n, tmp) == pro) ans.insert(tmp);
    for (int i = pos; i < SZ(fac); i++) DFS(i, pro*fac[i]);
}
 
int main()
{
    //ROP;
    for (int i = 0; i <= 60; i++) mp.insert((1ll<<i));  //2^n答案一定是0
    mp.insert(0);
    while (~scanf("%I64d", &n))
    {
        ans.clear(); fac.clear();
        printf("Case #%d:\n", ++cases);
        if (mp.count(n)) { puts("0"); puts(""); continue; }
        LL tmp = n;
        for (int i = 2; i <= (int)sqrt(n+0.5); i++) //枚举因子
        {
            if(tmp % i == 0)
            {
                fac.PB(i);
                while (tmp % i == 0) tmp /= i;
            }
        }
        if (tmp != 1 && tmp != n) fac.PB(tmp);
        DFS(0, 1);
        printf("%d\n", SZ(ans));
        for (set<LL>::iterator it = ans.begin(); it != ans.end(); it++)
            if (it != ans.begin()) printf(" %I64d", *it);
            else printf("%I64d", *it);
        puts("");
    }
    return 0;
}
```
---
categories: Posts
date: 2015-02-01 00:00:00
title: HDU 2351 - One is an Interesting Number (模拟)
tags: []
layout: post
---

#  [HDU 2351 - One is an Interesting Number (模拟)](/2015/02/HDU-2351/ "HDU 2351 - One is an Interesting Number \(模拟\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Feb 10 2015 13:51

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

给出一坨性质，问一个集合里满足性质最多的数

## 思路

在数论专题里的题目，明明是个模拟题= =坑

按照性质一条一条对照过去即可。

我先预处理了所有平方立方四次方的数。  
然后处理每个数的sum、multiple、square等

因为只有100个数，可以$O(n^2)$循环一遍。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127128129130131132133134135

| 
    
    
    #include <stack>#include <cstdio>#include <list>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 110;const int MOD = 1e9 + 7;const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };int cases = 0;typedef pair<int, int> pii; struct NUM{    int sum, multiple, num, square, cube, quad;}arr[MAXN]; void Handle(NUM #){    int tmp = num.num, curNum = num.num;    int sum = 0, multiple = 1;    while (tmp)    {        sum += tmp % 10;        multiple *= tmp % 10;        tmp /= 10;    }    num.sum = sum; num.multiple = multiple;    num.square = curNum <= 1000 ? curNum*curNum : -1;    num.quad = curNum <= 100 ? curNum*curNum*curNum*curNum : -1;    num.cube = curNum <= 100 ? curNum*curNum*curNum : -1;} set<int> cube, square, quad;int ansCnt; void Init() //处理平方、立方、四次方{    for (int i = 1; i <= 1000; i++)    {        square.insert(i*i);        if (i <= 100) cube.insert(i*i*i), quad.insert(i*i*i*i);    }} bool isPrime(int num){    if (num == 1) return false;    if (num == 2) return true;    for (int i = 2; i <= (int)sqrt(num+0.5); i++)        if (num % i == 0) return false;    return true;} int n, cnt[MAXN]; void Solve(const int &cur){    cnt[cur] = 0;    int curNum = arr[cur].num;    const NUM # = arr[cur];    for (int i = 0; i < n; i++)    {        if (i == cur) continue;        NUM &k = arr[i];        if (k.num % curNum == 0) cnt[cur]++;    //factor        if (curNum % k.num == 0) cnt[cur]++;    //multiple        if (k.square == curNum) cnt[cur]++;     //other-square        if (k.cube == curNum) cnt[cur]++;       //other-cube        if (k.quad == curNum) cnt[cur]++;       //other-quad        if (curNum % k.sum == 0) cnt[cur]++;        //other-sum        if (k.multiple != 0 && curNum % k.multiple == 0) cnt[cur]++;            //other-multiple    }    if (square.count(curNum)) cnt[cur]++;       //square    if (cube.count(curNum)) cnt[cur]++;         //cube    if (quad.count(curNum)) cnt[cur]++;         //quad    if (curNum % num.sum == 0) cnt[cur]++;      //sum-multiple    if (num.multiple != 0 && curNum % num.multiple == 0) cnt[cur]++;    //multiple-multiple    if (isPrime(curNum)) cnt[cur]++;    //prime    ansCnt = max(ansCnt, cnt[cur]);} int main(){    //ROP;    Init();    int T;    scanf("%d", &T);    while (T--)    {        ansCnt = -1;        scanf("%d", &n);        for (int i = 0; i < n; i++)        {            scanf("%d", &arr[i].num);            Handle(arr[i]);        }        for (int i = 0; i < n; i++) Solve(i);        vector<int> ans;        for (int i = 0; i < n; i++)            if (ansCnt == cnt[i]) ans.PB(arr[i].num);        sort(ans.begin(), ans.end());        printf("DATA SET #%d\n", ++cases);        for (int i = 0; i < SZ(ans); i++) printf("%d\n", ans[i]);    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - HDU](/tags/Online-Judge-HDU/)[Foundation - Simulate](/tags/Foundation-Simulate/)

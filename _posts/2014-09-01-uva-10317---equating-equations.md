---
categories: Posts
date: 2014-09-01 00:00:00
title: UVa 10317 - Equating Equations
tags: []
layout: post
---

#  [UVa 10317 - Equating Equations](/2014/09/UVa-10317/ "UVa 10317 - Equating Equations")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 21 2014 16:15

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

不改变符号顺序，问能不能交换数字的位置使等式成立。

## 思路

一开始看数据量这么小果断暴力枚举全排列然后检查，爽快地TLE了。后来想了一下，可以把左边的-号的数字都移到右边，这样两边都是正的数字，只要找出sum / 2的数字组成就行。

这里可以写DFS也可以写DP。

然后就是输出。

取出符号，如果在等号左边，而且符号是+，之后填上我们找到的数字，如果是-，就填上我们找到数字之外的数字（就是移到右边是正的数字）

等号右边相反。

但是需要考虑的情况有点多，主要是越界的问题。代码写得**很不优雅** ，大家参考思路就行。。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127128129130131132133134135136137138139140141142143144145146147148149150151152153154155156157158159160161162163164165166167

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <cctype>#include <algorithm>#include <cstdlib>#include <queue>#include <functional>#include <cstring>#include <string>#include <sstream>#include <map>#include <cmath>#define LL long long#define lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define ROP freopen("input.txt", "r", stdin);const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 30 + 5; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int vis[MAXN], succeed, sum, ans[MAXN], cnt;vector<int> num, sym, rnum;char str[10000];bool lpos, rpos; void DFS(int curSum, int cur, int curCnt){    for (int i = cur; i < num.size(); i++)    {        if (succeed) return;        if (curSum + num[i] > sum) return;        if (curSum + num[i] == sum && curCnt + 1 == cnt)        {            ans[curCnt] = i;            succeed = 1;            return;        }        ans[curCnt] = i;        DFS(curSum + num[i], i + 1, curCnt + 1);    }} void OutPut(){    if (!succeed) printf("no solution");    else    {        for (int i = 0; i < cnt; i++) vis[ans[i]] = 1;        for (int i = 0; i < num.size(); i++)            if (!vis[i]) rnum.push_back(num[i]);        int i = 0, j = 0, k = 0;        char ch;        if (lpos)        {            ch = sym[j++];            printf("%c", ch);            if (ch == '+') printf("%d", num[ans[i++]]);            if (ch == '-') printf("%d", rnum[k++]);        }        else printf("%d", num[ans[i++]]);        ch = sym[j++];        while (ch != '=')        {            printf(" %c ", ch);            if (ch == '-') printf("%d", rnum[k++]);            if (ch == '+') printf("%d", num[ans[i++]]);            ch = sym[j++];        }        printf(" = ");        if (rpos)        {            ch = sym[j++];            printf("%c", ch);            if (ch == '-') printf("%d", num[ans[i++]]);            if (ch == '+') printf("%d", rnum[k++]);            if (j == sym.size()) return;        }        else printf("%d", rnum[k++]);        if (j == sym.size()) return;        ch = sym[j++];        while (1)        {            printf(" %c ", ch);            if (ch == '-') printf("%d", num[ans[i++]]);            if (ch == '+') printf("%d", rnum[k++]);            if (j == sym.size()) return;            ch = sym[j++];        }             }} int main(){    //ROP;    int i, j;    char ch;    while (gets(str))    {        MS(vis, 0);        succeed = sum = cnt = 0;        num.clear();        rnum.clear();        sym.clear();        lpos = rpos = false;        int a = 0;        char last = 0;         for (i = 0; str[i] != '='; i++)        {            if (isdigit(str[i]))            {                if (last == '+' || last == 0) cnt++;                a = atoi(&str[i]);                num.push_back(a); sum += a;                while (isdigit(str[i])) i++;            }            if (str[i] == '+' || str[i] == '-')            {                if (num.empty()) lpos = true;                last = str[i];                sym.push_back(last);            }        }        sym.push_back(str[i]);        int temp = num.size();  //用于标记当前的数量        last = 0;        for(; i < strlen(str); i++)        {            if (isdigit(str[i]))            {                if (last == '-') cnt++;                a = atoi(&str[i]);                num.push_back(a); sum += a;                while (isdigit(str[i])) i++;            }            if (str[i] == '+' || str[i] == '-')            {                if (num.size() == temp) rpos = true;                last = str[i];                sym.push_back(last);            }        }        if (sum & 1)        {            printf("no solution\n");            continue;        }        sum /= 2;        sort(num.begin(), num.end());        DFS(0, 0, 0);        OutPut();        puts("");    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Foundation - Search](/tags/Foundation-Search/)

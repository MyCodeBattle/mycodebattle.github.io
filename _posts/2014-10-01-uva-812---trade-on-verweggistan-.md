---
categories: Posts
date: 2014-10-01 00:00:00
title: UVa 812 - Trade on Verweggistan (贪心)
tags: []
layout: post
---

#  [UVa 812 - Trade on Verweggistan (贪心)](/2014/10/UVa-812/ "UVa 812 - Trade on Verweggistan \(贪心\)")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Oct 2 2014 12:02

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

## 题意

有N个作坊，每个作坊都有一叠酒（我就当成酒了）

如果要买第i个的话，必须买下上面的所有酒。

酒的出售价是10元。

现在有个商人要买酒，求最大利润和达到最大利润的时候买的酒的数量。如果有多解，每个都输出。如果大于10，输出前十个。

## 思路

看网上都说是DP？我怎么觉得是贪心。

有点类似于有依赖关系的背包。

  1. 如何得到最大利润？

分别计算出每个作坊所能达到的最大利润，然后把所有正的利润加起来就行。

  1. 如何计算达到最大利润时候的数量？

在求出每个作坊的最大利润的时候，扫描一遍数组，如果当前利润i和最大利润一样，就把i存到一个数组里。最后汇总即可。

总体的思路就是这样，还有一些小的东西。

在汇总数量的时候，一开始我不知道怎么办。

比如说，第一个在达到最大利润的时候，数量可以是2 3  
第二个，3 4

那么总的数量就是 5 6 7. 然后这个结果还要作为中间结果，和下面的进行累加。然后我就不知道这个结果要存在哪里。。

后来YY了一下，开了两个数组，先存到数组A，然后存到数组B。。。轮流存╮(╯▽╰)╭

因为可能有重复的，用了unique。

还有当最大利润为0的时候，要加入0.因为可以不选。

就是这样。代码感觉不太优雅，因为有很多重复的地方。仅供参考

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117

| 
    
    
    #include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <ctime>#include <cstdlib>#include <fstream>#include <string>#include <sstream>#include <map>#include <cmath>#define LL long long#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 2e4 + 5;const int MOD = 20071027; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int purl[55][25], pro[55];vector<int> ans, num[55], ans2; int main(){    //ROP;    int w, i, j, n, cases = 0;    bool first = true;    while (scanf("%d", &w), w)    {        ans.clear();        ans2.clear();        for (i = 1; i <= w; i++) num[i].clear();        for (i = 1; i <= w; i++)        {            scanf("%d", &n);            int tmp, vmax = -1;            for (j = 1; j <= n; j++)            {                scanf("%d", &tmp);                purl[i][j] = purl[i][j - 1] + 10 - tmp;                vmax = max(purl[i][j], vmax);            }            if (vmax >= 0)            {                for (j = 1; j <= n; j++)                    if (purl[i][j] == vmax) num[i].PB(j);   //num[i]，第i个作坊达到最大利润的时候的可以选择的个数                if (vmax == 0) num[i].PB(0);    //如果是0的话可以不选            }            pro[i] = vmax;  //profit[i]        }        int sum = 0;        for (i = 1; i <= w; i++)        {            if (pro[i] >= 0)            {                sum += pro[i];                if (ans.empty() && ans2.empty())                    for (j = 0; j < num[i].size(); j++) ans.PB(num[i][j]);                else if (ans.empty())                {                    for (j = 0; j < ans2.size(); j++)                        for (int k = 0; k < num[i].size(); k++) ans.PB(ans2[j] + num[i][k]);                    ans2.clear();                }                else                {                    for (j = 0; j < ans.size(); j++)                        for (int k = 0; k < num[i].size(); k++) ans2.PB(ans[j] + num[i][k]);                    ans.clear();                }            }        }        if (ans.empty()) sort(ans2.begin(), ans2.end());        else sort(ans.begin(), ans.end());        if (!first) puts("");        first = false;        printf("Workyards %d\n", ++cases);        printf("Maximum profit is %d.\n", sum);        printf("Number of pruls to buy:");        if (ans.empty() && ans2.empty()) printf(" 0");        else if (ans2.empty())        {            int real = unique(ans.begin(), ans.end()) - ans.begin();            for (i = 0; i < min(real, 10); i++) printf(" %d", ans[i]);        }        else        {            int real = unique(ans2.begin(), ans2.end()) - ans2.begin();            for (i = 0; i < min(real, 10); i++) printf(" %d", ans2[i]);        }        puts("");    }    return 0;}  
  
---|---  
  
[Solving Reports](/categories/Solving-Reports/)

[Online Judge - UVa](/tags/Online-Judge-UVa/)[Foundation - Greedy](/tags/Foundation-Greedy/)

---
categories: Posts
date: 2014-10-01 00:00:00
title: PKU 2528 - Mayor's posters (线段树 + 区间修改)
tags: []
layout: post
---

## 思路

线段树学习第三发

引用一下NotOnlySuccess大大的思路。

> 离散化简单的来说就是只取我们需要的值来用,比如说区间[1000,2000],[1990,2012] 我们用不到[-∞,999][1001,1989][1991,1999][2001,2011][2013,+∞]这些值,所以我只需要1000,1990,2000,2012就够了,将其分别映射到0,1,2,3,在于复杂度就大大的降下来了  
> 所以离散化要保存所有需要用到的值,排序后,分别映射到1~n,这样复杂度就会小很多很多  
> 而这题的难点在于每个数字其实表示的是一个单位长度(并非一个点),这样普通的离散化会造成许多错误(包括我以前的代码,poj这题数据奇弱)  
> 给出下面两个简单的例子应该能体现普通离散化的缺陷:  
> 例子一:1-10 1-4 5-10  
> 例子二:1-10 1-4 6-10  
> 普通离散化后都变成了[1,4][1,2][3,4]  
> 线段2覆盖了[1,2],线段3覆盖了[3,4],那么线段1是否被完全覆盖掉了呢?  
> 例子一是完全被覆盖掉了,而例子二没有被覆盖  
> 为了解决这种缺陷,我们可以在排序后的数组上加些处理,比如说[1,2,6,10]  
> 如果相邻数字间距大于1的话,在其中加上任意一个数字,比如加成[1,2,3,6,7,10],然后再做线段树就好了.  
> 线段树功能:update:成段替换 query:简单hash

因为可能有2W个点，每个点又都可能插入一个数据，所以要开到4W * 4W个结点。

当你看到其他解题报告是8W个结点的时候，那他一定是错的。

(为了探究这8W和16W整页VJ都被我刷满了╮(╯▽╰)╭)

## 代码


```c++
#include <cstdio>
#include <stack>
#include <set>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <functional>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <ctime>
#include <cstdlib>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <cmath>
#define LL long long
#define Lowbit(x) ((x) & (-x))
#define MP(a, b) make_pair(a, b)
#define MS(arr, num) memset(arr, num, sizeof(arr))
#define PB push_back
#define F first
#define S second
#define ROP freopen("input.txt", "r", stdin);
#define MID(a, b) (a + ((b - a) >> 1))
#define LC rt << 1, l, mid
#define RC rt << 1|1, mid + 1, r
#define LRT rt << 1
#define RRT rt << 1|1
#define BitCount(x) __builtin_popcount(x)
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
using namespace std;
const int MAXN = 2e4 + 5;
const int MOD = 20071027;
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
struct POINT
{
    int l, r;
}pit[10005];
 
int ans, col[20000 << 3];
set<int> mp;
vector<int> ve;
 
void PushDown(int rt)
{
    if (col[rt] != -1)
    {
        col[LRT] = col[RRT] = col[rt];
        col[rt] = -1;
    }
}
 
void Query(int rt, int l, int r)
{
    if (col[rt] != -1)
    {
        if (!mp.count(col[rt]))
            ans++;
        mp.insert(col[rt]);
        return;
    }
    if (l == r) return;
    int mid = MID(l, r);
    Query(LC);
    Query(RC);
}
 
void Update(int rt, int l, int r, int L, int R, int val)
{
    if (L <= l && r <= R)
    {
        col[rt] = val;
        return;
    }
    PushDown(rt);
    int mid = MID(l, r);
    if (L <= mid) Update(LC, L, R, val);
    if (R > mid) Update(RC, L, R, val);
}
 
int main()
{
    //ROP;
    int T, i, j, n;
    scanf("%d", &T);
    while (T--)
    {
        ve.clear();
        mp.clear();
        ans = 0;
        scanf("%d", &n);
        for (i = 0; i < n; i++)
        {
            scanf("%d%d", &pit[i].l, &pit[i].r);
            ve.PB(pit[i].l); ve.PB(pit[i].r);
        }
        sort(ve.begin(), ve.end());
        int num = unique(ve.begin(), ve.end()) - ve.begin();
        ve.resize(num);
        int cnt = 0;
        for (i = 0; i < num - 1; i++)
            if (ve[i] + 1 != ve[i + 1]) ve.PB(ve[i] + 1);
        sort(ve.begin(), ve.end());
        MS(col, -1);
        for (i = 0; i < n; i++)
        {
            int l = lower_bound(ve.begin(), ve.end(), pit[i].l) - ve.begin();
            int r = lower_bound(ve.begin(), ve.end(), pit[i].r) - ve.begin();
            Update(1, 0, ve.size() - 1, l, r, i);
        }
        Query(1, 0, ve.size() - 1);
        printf("%d\n", ans);
    }
    return 0;
}
```
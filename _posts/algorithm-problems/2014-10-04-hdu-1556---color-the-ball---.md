---
categories: Posts
date: 2014-10-04 00:00:00
title: HDU 1556 - Color the ball (树状数组 | 线段树)
tags: []
layout: post
---

## 思路

都忘了树状数组长什么样了。。模板题，趁机回忆了一下。

## 代码（树状数组）


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
#define SZ(x) (int)x.size()
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
const LL MAXN = 1e5 + 10;
const int MOD = 20071027;
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
int C[MAXN], n;
 
int GetValue(int x)
{
    int sum = 0;
    while (x > 0)
    {
        sum += C[x];
        x -= Lowbit(x);
    }
    return sum;
}
 
void Update(int x, int v)
{
    while (x <= n)
    {
        C[x] += v;
        x += Lowbit(x);
    }
}
 
int main()
{
    //ROP;
    int i, j;
    while (scanf("%d", &n), n)
    {
        fill(C, C + n + 1, 0);
        int a, b;
        for (i = 0; i < n; i++)
        {
            scanf("%d%d", &a, &b);
            Update(a, 1);
            Update(b + 1, -1);
        }
        for (i = 1; i <= n; i++)
        {
            if (i == n) printf("%d\n", GetValue(i));
            else printf("%d ", GetValue(i));
        }
    }
    return 0;
}
```
 

### 线段树


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
#define SZ(x) (int)x.size()
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
const LL MAXN = 1e5 + 10;
const int MOD = 20071027;
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
int cnt[MAXN << 2];
 
struct SEGTREE
{
    void init()
    {
        MS(cnt, 0);
    }

    void PushDown(int rt)
    {
        if (cnt[rt])
        {
            cnt[LRT] += cnt[rt];
            cnt[RRT] += cnt[rt];
            cnt[rt] = 0;
        }
    }

    int search(int rt, int l, int r, int val)
    {
        if (l == r) return cnt[rt];
        PushDown(rt);
        int mid = MID(l, r);
        if (val <= mid) return search(LC, val);
        else return search(RC, val);
    }

    void update(int rt, int l, int r, int L, int R)
    {
        if (L <= l && r <= R)
        {
            cnt[rt]++;
            return;
        }
        PushDown(rt);
        int mid = MID(l, r);
        if (L <= mid) update(LC, L, R);
        if (R > mid) update(RC, L, R);
        //PushUp(rt);
    }

}segtree;
 
int main()
{
    //ROP;
    int n, i, j;
    while (scanf("%d", &n), n)
    {
        int a, b;
        segtree.init();
        for (i = 0; i < n; i++)
        {
            scanf("%d%d", &a, &b);
            segtree.update(1, 1, n, a, b);
        }
        for (i = 1; i <= n; i++)
            if (i != n) printf("%d ", segtree.search(1, 1, n, i));
            else printf("%d\n", segtree.search(1, 1, n, i));
    }
    return 0;
}
```
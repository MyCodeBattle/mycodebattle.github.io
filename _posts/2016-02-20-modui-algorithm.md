---
categories: Solving-Reports
date: 2015-09-30 12:36:38
title: BZ 2038 - 小Z的袜子 (莫队)
tags: [Online Judge - BZ, Algorithm - MoDui]
layout: post
---

 ## 题意 ## 

区间询问l, r里拿出一样的数的概率。


 ## 思路 ## 

莫队算法。

分块，每个块大小$\sqrt{query}$

对于区间询问问题，如果我们可以在短时间内求出`l+-1, r`, `l, r+-1`，那么我们就可以用莫队算法。

块不同的时候，按l排序，不然按r排序。


 ## 代码 ## 

```
#include <stack>
#include <cstdio>
#include <list>
#include <cassert>
#include <set>
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <functional>
#include <cstring>
#include <algorithm>
#include <cctype>
#pragma comment(linker, "/STACK:102400000,102400000")
#include <string>
#include <map>
#include <cmath>
//#include <ext/pb_ds/assoc_container.hpp>
//#include <ext/pb_ds/hash_policy.hpp>
using namespace std;
//using namespace __gnu_pbds;
#define LL long long
#define ULL unsigned long long
#define SZ(x) (int)x.size()
#define Lowbit(x) ((x) & (-x))
#define MP(a, b) make_pair(a, b)
#define MS(p, num) memset(p, num, sizeof(p))
#define PB push_back
#define X first
#define Y second
#define ROP freopen("input.txt", "r", stdin);
#define MID(a, b) (a + ((b - a) >> 1))
#define LC rt << 1, l, mid
#define RC rt << 1|1, mid+1, r
#define LRT rt << 1
#define RRT rt << 1|1
#define FOR(i, a, b) for (int i=(a); (i) < (b); (i)++)
#define FOOR(i, a, b) for (int i = (a); (i)<=(b); (i)++)
#define TRAVERSAL(u, i) for (int i = head[u]; i != -1; i = edge[i].nxt)
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
const double eps = 1e-8;
const int MAXN = 5e4+10;
const int MOD = 1e9+7;
const int dir[][2] = { {0, 1}, {1, 0} };
const int seed = 131;
int cases = 0;
typedef pair<int, int> pii;
 
int pos[MAXN];
 
struct POINT
{
    int l, r, id;
    bool operator < (const POINT &a) const
    {
        if (pos[l] != pos[a.l]) return l < a.l;
        return r < a.r;
    }
}p[MAXN];
 
struct ANS
{
    LL x, y;
}ans[MAXN];
 
int n, m, arr[MAXN];
LL num[MAXN], cur_ans;
 
void update(int pos, int val)
{
    cur_ans -= num[arr[pos]]*num[arr[pos]];
    num[arr[pos]] += val;
    cur_ans += num[arr[pos]]*num[arr[pos]];
}
 
void solve()
{
    int cl = 1, cr = 0;
    for (int i = 1; i <= m; i++)
    {
        for (; cr < p[i].r; cr++) update(cr+1, 1);
        for (; cr > p[i].r; cr--) update(cr, -1);
        for (; cl < p[i].l; cl++) update(cl, -1);
        for (; cl > p[i].l; cl--) update(cl-1, 1);
        if (p[i].l == p[i].r)
        {
            ans[p[i].id].x = 0; ans[p[i].id].y = 1;
            continue;
        }
        LL len = p[i].r-p[i].l+1;
        ans[p[i].id].x = cur_ans - len;
        ans[p[i].id].y = len * (len-1);
        LL tmp = __gcd(ans[p[i].id].x, ans[p[i].id].y);
        ans[p[i].id].x /= tmp; ans[p[i].id].y /= tmp;
    }
}
 
int main()
{
    //ROP;
    scanf("%d%d", &n, &m);
    int block_size = (int)sqrt(m);
    for (int i = 1; i <= n; i++)
    {
        scanf("%d", &arr[i]);
        pos[i] = (i-1) / block_size + 1;
    }
    for (int i = 1; i <= m; i++)
    {
        scanf("%d%d", &p[i].l, &p[i].r);
        p[i].id = i;
    }
    sort(p+1, p+1+m);
    solve();
    for (int i = 1; i <= m; i++) printf("%lld/%lld\n", ans[i].x, ans[i].y);
    return 0;
}
```

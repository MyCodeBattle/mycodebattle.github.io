---
categories: Posts
date: 2014-07-06 00:00:00
title: Codeforces Round - 255 (Div. 2) A~B
tags: []
layout: post
---

## A

### 传送门

[A. DZY Loves Chessboard](http://codeforces.com/problemset/problem/445/A)

### 题意

放上黑色或者白色，条件是相邻的颜色不能相同。

### 思路

一开始想依次检查上下左右，如果存在颜色就放相反的，但是过不去。看了数据才知道这种思路是错的。  
后来**hcbbt** 告诉我用奇偶的办法。Orz…

### 代码


```c++
#include <cstdio>
#include <cstring>
using namespace std;
 
char mp[110][110];
 
int main()
{
    //freopen("input.txt", "r", stdin);
    int row, col, i, j, n;
    bool flag;
    while (~scanf("%d%d%*c", &row, &col))
    {
        for (i = 0; i < row; i++)
            gets(mp[i]);
        for (i = 0; i < row; i++)
            for (j = 0; j < col; j++)
                if (mp[i][j] == '.')
                {
                    if ((i % 2 == 0) && (j % 2 == 0))
                        mp[i][j] = 'W';
                    else if (i % 2 == 0 && (j % 2))
                        mp[i][j] = 'B';
                    else if ((i % 2) && (j % 2))
                        mp[i][j] = 'W';
                    else
                        mp[i][j] = 'B';
                }
        for (i = 0; i < row; i++)
            puts(mp[i]);
    }
    return 0;
}
```
 

## B

### 传送门

[B. DZY Loves Chemistry](http://codeforces.com/problemset/problem/445/B)

### 题意

总共有N种颜料，有些放在一起会反应。如果会反应危险系数就会*2，给出会反应的列表，求最大的危险系数。

### 思路

把会反应的变成连通的图，然后开始走，每走一步ans就*2。最后输出。一开始给了个WA，我以为思路错了就放弃了。后来看了数据才知道是没开long long。以后会注意的。

### 代码


```c++
#include <cstdio>
#include <cstring>
using namespace std;
const int MAXN = 50 + 10;
 
char mp[MAXN][MAXN];
int vis[MAXN];
long long ans;
 
void DFS(int j)
{
    vis[j] = 1;
    for (int k = 0; k < MAXN; k++)
        if (mp[j][k] && !vis[k])
        {
            ans *= 2;
            DFS(k);
        }
}
 
int main()
{
    //freopen("in.txt", "r", stdin);
    int num, i, j, n, a, b;
    while (~scanf("%d%d", #, &n))
    {
        memset(mp, 0, sizeof(mp));
        memset(vis, 0, sizeof(vis));
        ans = 1;
        for (i = 0; i < n; i++)
        {
            scanf("%d%d", &a, &b);
            mp[a][b] = mp[b][a] = 1;
        }
        for (i = 1; i <= num; i++)
            for (j = 1; j <= num; j++)
                if (mp[i][j] && !vis[i])
                {
                    vis[i] = 1;
                    ans *= 2;
                    DFS(j);
                }
        printf("%I64d\n", ans);
    }
    return 0;
}
```
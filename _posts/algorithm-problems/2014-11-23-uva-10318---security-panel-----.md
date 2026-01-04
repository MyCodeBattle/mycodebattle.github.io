---
categories: Posts
date: 2014-11-23 00:00:00
title: UVa 10318 - Security Panel (暴力 + 剪枝 + 回溯)
tags: []
layout: post
---

## 题意

给一个3 _3的图案，代表着按一个按钮的时候周围灯改变的情况，这时候中间那个格子代表着按的灯。  
如果那个位置是_，灯的状态会改变。

求最少按哪几个按钮，可以点亮全部的灯。

## 思路

每个按钮要么按一次，要么不按。  
因为我们是按照顺序DFS下来的，如果到了第r行，第r - 2行还有灯没被点亮，这时候那个灯已经永远点不亮了，这种状态是无效的，可以返回。  
大概就是这样。记录路径的时候我用了string，反正和用数组是一样的。

这题折腾一天了。

一开始是用状态压缩，就从早上折腾到了晚上，那个剪枝加了和没加一样，到现在还不知道原因。

后来还是采用了数组表示

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
#include <string>
#include <map>
#include <iomanip>
#include <cmath>
#define LL long long
#define ULL unsigned long long
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
#define BitCountll(x) __builtin_popcountll(x)
#define LeftPos(x) 32 - __builtin_clz(x) - 1
#define LeftPosll(x) 64 - __builtin_clzll(x) - 1
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
using namespace std;
const double eps = 1e-6;
const int MAXN = 1e9 + 10;
const int MOD = 1000007;
const int dir[][2] = { {-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 0}, {0, 1}, {1, -1}, {1, 0}, {1, 1} };
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
int pivot, clr, row, col, ww[10][10], mat[15], M[30];
char mp[10][10];
bool flag;
string ans;
 
void Transform()
{
    MS(mat, 0); MS(M, 0);
    int cnt = 0;
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (mp[i][j] == '*') mat[cnt++] = 1;
            else cnt++;
}
 
void ChangeState(int num)
{
    int x = num / col, y = num % col;
    for (int i = 0; i < 9; i++)
    {
        int xx = x + dir[i][0], yy = y + dir[i][1];
        if (xx >= 0 && xx < row && yy >= 0 && yy < col && mat[i])
        {
            int curPos = xx * col + yy;
            M[curPos] ^= 1;
        }
    }
}
 
bool Check(int k)
{
    for (int i = 0; i < k * col; i++)
        if (M[i] != 1) return false;
    return true;
}
 
bool DFSID(int curNum, string path)
{
    if (curNum == row * col)
    {
        for (int i = 0; i < curNum; i++)
            if (M[i] != 1) return false;
        ans = path;
        return flag = true;
    }
    int r = curNum / col;
    if (r - 2 >= 0 && !Check(r - 2)) return false;
    char tmp = 'a' + curNum + 1;
    if (DFSID(curNum + 1, path)) return true;
    ChangeState(curNum);
    if (DFSID(curNum + 1, path + tmp)) return true;
    ChangeState(curNum);
    return false;
}
 
int main()
{
    //ROP;
    int i, j, cases = 0;
    while (scanf("%d%d%*c", &row, &col), row + col)
    {
        for (i = 0; i < 3; i++) scanf("%s", mp[i]);
        Transform();
        flag = false;
        DFSID(0, "");
        printf("Case #%d\n", ++cases);
        if (flag)
        {
            printf("%d", ans[0] - 'a');
            for (int i = 1; i < SZ(ans); i++) printf(" %d", ans[i] - 'a');
            puts("");
        }
        else puts("Impossible.");
    }
    return 0;
}
```
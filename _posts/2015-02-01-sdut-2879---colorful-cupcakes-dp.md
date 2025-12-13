---
categories: Posts
date: 2015-02-01 00:00:00
title: SDUT 2879 - Colorful Cupcakes (DP)
tags: []
layout: post
---

## 题意

给出ABC三种颜色的个数，求相邻颜色不相同，首尾颜色不相同的串的个数。

## 思路

$dp[i][a][b][k]$表示前i个位置A有a个B有b个，当前位置颜色是k的个数。

假设当前颜色是红色，也就是0（自己定）  
$dp[i][a][b][k] = \sum dp[i-1][a-1][b][ii], \text{ ii = 1,2,3. ii != k}$，ii是上一个位置的颜色，不能和k相同。

## 代码
    
    
    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879808182838485

| ```c++
#include <stack>#include <cstdio>#include <list>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>using namespace std;#define LL long long#define ULL unsigned long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define X first#define Y second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;const double eps = 1e-8;const int MAXN = 50 + 3;const int MOD = 1e9 + 7;const int dir[][2] = { {-1, 0}, {0, -1}, { 1, 0 }, { 0, 1 } };int cases = 0;typedef pair<int, int> pii; int dp[MAXN][MAXN][MAXN][3]; int DFS(int pre, int a, int b, int k, int last){   //前pre位有a个红色b个绿色，此位是k颜色的个数    if (dp[pre][a][b][k] != -1) return dp[pre][a][b][k];    if (a < 0 || b < 0 || pre-a-b < 0) return 0;    if (pre == 1 && k == last) return 0;    //如果第一位和最后一位相同，0种情况    if (pre == 1) return ((a && k == 0) || (b && k == 1) || (pre-a-b && k == 2));    //有可能出现第一位本来已经没多余的某种颜色了，却能走到这一步。排除    //因为枚举前一位是什么颜色的时候并没考虑那种颜色还有没有剩余    int ans = 0;    for (int ii = 0; ii < 3; ii++)  //前一位是什么颜色    {        if (k == ii) continue;        if (k == 0) ans = (ans + DFS(pre-1, a-1, b, ii, last)) % MOD;        if (k == 1) ans = (ans + DFS(pre-1, a, b-1, ii, last)) % MOD;        if (k == 2) ans = (ans + DFS(pre-1, a, b, ii, last)) % MOD;    }    return dp[pre][a][b][k] = ans;} char str[100];int cnt[3]; int main(){    //ROP;    int T;    scanf("%d", &T);    while (T--)    {        scanf("%s", str);        MS(dp, -1); MS(cnt, 0);        int len = strlen(str);        for (int i = 0; i < len; i++) cnt[str[i]-'A']++;        int ans = 0;        for (int i = 0; i < 3; i++)     //最后一位是什么颜色        {            MS(dp, -1);            ans = (ans + DFS(len, cnt[0], cnt[1], i, i)) % MOD;        }        printf("%d\n", ans);    }    return 0;}
```
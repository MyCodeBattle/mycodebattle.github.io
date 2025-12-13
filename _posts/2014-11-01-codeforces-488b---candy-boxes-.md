---
categories: Posts
date: 2014-11-01 00:00:00
title: Codeforces 488B - Candy Boxes (构造)
tags: []
layout: post
---

## 题意

如果有一个序列满足(a1 + a2 + a3 + a4) / 4 = (a2 + a3) / 2，那么这个序列符合条件的。

现在给出4个数中的n个，判断能否构造出这么一个序列。

## 思路

这是我写过最长的DIV2 - B（ ＴДＴ）

解这个题目之前，首先要推出两条式子

$$x_4 = 3x_{1}$$  
$$4x_{1} = x_2 + x_3$$  
  
读取输入以后对他们从小到大排序  
  
解释一下代码里的各个变量的含义。  
input[]，表示输入的数.  
ans[i]，表示最终序列第i位的数  
  
先考虑n = 0的情况。  
这时候随便输出一个序列即可。  
  
n = 1时，直接把input[1]当成ans[1]，根据第二条式子推出ans[4]，然后就类似1 1 3 3直接得到答案。  
  
n = 2时  
1\. 如果input[2]（也就是两个输入里大的那个数，后面也一样）% 3 == 0，说明input[2]可以作为ans[4]，然后ans[1]可以得出。这时候要判断一下ans[1]是否比input[1]小，如果不是的话这个序列就不存在了。  
这样一来就知道了三个数，可以直接输出ans[1] _4 - input[1]（题目没要求按位的顺序输出）和ans[1]了。  
2\. input[2]不能整除3，这时候将input[1]作为ans[1]，判断input[2]是否小于ans[1] _ 3。如果大于的话，显然无解。  
然后就可以求出ans[4]，和上面一样可以输出剩下的一位数了。  
  
n = 3时，总的思路和上面差不多，简略说了。  
判断input[3]能否作为ans[4]，分两种情况。最后判断得出的序列能否成立。  
  
这里要注意当input[3] / 3 = input[1]这种情况还要讨论一下。  
  
n = 4，直接判断。  
  
##代码##  
  

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
const int MAXN = 1500 + 10;
const int MOD = 1000007;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
int ans[10], input[10];
bool flag = true;
 
bool Solve(int n)
{
    if (n == 0)
    {
        puts("YES");
        printf("%d\n%d\n%d\n%d\n", 1, 1, 3, 3);
    }
    if (n == 1)
    {
        puts("YES");
        ans[1] = input[1], ans[4] = ans[1] * 3, ans[2] = ans[1], ans[3] = ans[4];
        for (int i = 2; i <= 4; i++) printf("%d\n", ans[i]);
    }
    if (n == 2)
    {
        if (input[2] % 3)
        {
            if (input[1] * 3 < input[2]) return flag = false;
            puts("YES");
            ans[1] = input[1], ans[4] = ans[1] * 3;
            int tmp = 4 * ans[1] - input[2];
            printf("%d\n%d\n", ans[4], tmp);
        }
        else
        {
            if (input[2] / 3 > input[1]) return flag = false;
            puts("YES");
            ans[1] = input[2] / 3;
            int tmp = 4 * ans[1] - input[1];
            printf("%d\n%d\n", ans[1], tmp);
        }
    }
    if (n == 3)
    {
        if (input[3] % 3)
        {
            if (input[1] * 3 < input[3]) return flag = false;
            for (int i = 1; i <= 3; i++) ans[i] = input[i];
            ans[4] = ans[1] * 3;
            if (4 * ans[1] != ans[2] + ans[3]) return flag = false;
            puts("YES");
            printf("%d\n", ans[4]);
        }
        else
        {
            if (input[3] / 3 > input[1]) return flag = false;
            if (input[3] / 3 == input[1])
            {
                puts("YES");
                printf("%d\n", input[1] * 4 - input[2]);
                return true;
            }
            ans[1] = input[3] / 3, ans[4] = input[3], ans[2] = input[1], ans[3] = input[2];
            if (4 * ans[1] != ans[2] + ans[3]) return flag = false;
            puts("YES");
            printf("%d\n", ans[1]);
        }
    }
    if (n == 4)
    {
        for (int i = 1; i <= 4; i++) ans[i] = input[i];
        if (4 * ans[1] == ans[2] + ans[3]) puts("YES");
        else flag = false;
    }
}
 
int main()
{
    int n, i, j;
    scanf("%d", &n);
    for (i = 1; i <= n; i++) scanf("%d", &input[i]);
    sort(input + 1, input + n + 1);
    Solve(n);
    if (!flag)
    {
        puts("NO");
        return 0;
    }
    return 0;
}
```
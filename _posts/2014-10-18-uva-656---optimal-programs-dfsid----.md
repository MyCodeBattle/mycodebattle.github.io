---
categories: Posts
date: 2014-10-18 00:00:00
title: UVa 656 - Optimal Programs (DFSID + 模拟 + 枚举)
tags: []
layout: post
---

## 题意

给出五个操作，和两个序列。

要求输出一种操作，使得从上一个序列的每个数可以变到下一个序列的每个数。

输出最小的操作数，如果相同，输出字典序最小的。

## 思路

没想到什么好的办法，暴力判断每一种操作，并记录

如果操作过后就是后来的那个数，然后对这个操作检查之后的所有数，如果都满足，输出。

因为感觉BFS会超内存，就用了DFSID

因为我是按照字典序来依次执行操作的，所以当有合适的操作时候他一定是字典序最小的。

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
const int MAXN = 150 + 10;
const int MOD = 1e9 + 7;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
 
typedef pair<int, int> pii;
typedef vector<int>::iterator viti;
typedef vector<pii>::iterator vitii;
 
string comd, str[] = {"ADD", "DIV", "DUP", "MUL", "SUB"};
int n, ori[MAXN], fin[MAXN];
bool flag;
 
int Fun(int cmd, stack<int> &stk)
{
    if (SZ(stk) == 1 && cmd != 2) return -1;
    if (cmd == 0)   //ADD
    {
        int a = stk.top(); stk.pop();
        if (abs(a + stk.top()) > 30000)
        {
            stk.push(a);
            return -1;
        }
        stk.top() += a;
    }
    else if (cmd == 1)  //DIV
    {
        if (stk.top() == 0) return -1;
        int a = stk.top(); stk.pop();
        stk.top() /= a;
    }
    else if (cmd == 2)  //DUP
        stk.push(stk.top());
    else if (cmd == 3)  //MUL
    {
        int a = stk.top(); stk.pop();
        if (abs(a * stk.top()) > 30000)
        {
            stk.push(a);
            return -1;
        }
        stk.top() *= a;
    }
    else
    {
        int a = stk.top(); stk.pop();
        if (abs(stk.top() - a) > 30000)
        {
            stk.push(a);
            return -1;
        }
        stk.top() -= a;
    }
    return 0;
}
 
bool Check(string cmd)
{
    for (int i = 1; i < n; i++)
    {
        stack<int> stk;
        stk.push(ori[i]);
        for (int j = 0; j < SZ(cmd); j++)
        {
            int tmp = Fun(cmd[j] - '0', stk);
            if (tmp == -1) return false;
        }
        if (!(SZ(stk) == 1 && stk.top() == fin[i])) return false;
    }
    return flag = true;
}
 
void Goback(int fst, int sec, stack<int> &stk, int cmd)
{
    if (cmd == 2)   //DUP
        stk.pop();
    else
    {
        stk.pop();
        stk.push(sec);
        stk.push(fst);
    }
}
 
bool DFS(int cnt, string comd, stack<int> stk, int step)
{
    if (cnt > step) return false;
    int fst = stk.top(); stk.pop();
    int sec = INF;
    if (!stk.empty()) sec = stk.top();
    stk.push(fst);
    for (int i = 0; i < 5; i++)
    {
        int tmp = Fun(i, stk);
        if (tmp == -1) continue;    //此操作不合法
        char tempStr = i + '0';
        if (SZ(stk) == 1 && stk.top() == fin[0])    //此操作过后可以转换
            if (Check(comd + tempStr))
            {
                comd += tempStr;
                for (i = 0; i < SZ(comd); i++)
                    if (i == 0) cout << str[comd[i] - '0'];
                    else cout << " " << str[comd[i] - '0'];
                puts("");
                return true;
            }
        if (DFS(cnt + 1, comd + tempStr, stk, step)) return true;
        Goback(fst, sec, stk, i);   //回到开始情况
    }
    return false;
}
 
int main()
{
    //ROP;
    int i, j, cases = 0;
    while (scanf("%d", &n), n)
    {
        printf("Program %d\n", ++cases);
        flag = false;
        for (i = 0; i < n; i++) scanf("%d", &ori[i]);
        for (i = 0; i < n; i++) scanf("%d", &fin[i]);
        if (ori[0] == fin[0])       //先排除一下无操作的情况
        {
            for (i = 1; i < n; i++)
                if (ori[i] != fin[i]) break;
            if (i == n)
            {
                puts("Empty sequence");
                puts("");
                continue;
            }
        }
        for (int step = 2; step <= 10; step++)
        {
            if (flag) break;
            stack<int> stk; stk.push(ori[0]);
            DFS(1, "", stk, step);
        }
        if (!flag) puts("Impossible");
        puts("");
    }
    return 0;
}
```
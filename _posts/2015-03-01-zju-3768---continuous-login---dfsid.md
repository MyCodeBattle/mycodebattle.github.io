---
categories: Posts
date: 2015-03-01 00:00:00
title: ZJU 3768 - Continuous Login (二分 + DFSID)
tags: []
layout: post
---

## 题意

给出一个目标值，只能用连续的和拼出来。输出最少的连续和。

## 思路

DFSID出奇迹。

一开始最后一个数也是线性搜过去，TLE了。剪了一下1500ms。

后来最后一个数改成$logn$级别的查询竟然变成了10ms！

## 代码


```c++
vector<int> ans, arr;
map<int, int> mp;
int depth;
 
bool DFS(int curPos, int sum, int curDep)
{
    if (curDep == depth)
    {
        if (sum == 0) return true;
        return false;
    }
    if (depth - curDep == 1)
    {
        if (mp.count(sum))
        {
            ans.push_back(mp[sum]);
            return true;
        }
        return false;
    }
    for (int i = curPos; i >= 1; i--)
    {
        if (arr[i] * (depth-curDep) < sum) break;
        if (arr[i] > sum) continue;
        ans.PB(i);
        if (DFS(i, sum-arr[i], curDep+1)) return true;
        ans.pop_back();
    }
    return false;
}
 
int main()
{
    //ROP;
    arr.PB(0);
    for (int i = 1, sum = 0; sum <= MAXN; i++)
    {
        sum += i;
        arr.PB(sum);
        mp[sum] = i;
    }
    int T;
    scanf("%d", &T);
    while (T--)
    {
        ans.clear();
        int n;
        scanf("%d", &n);
        depth = 1;
        int startPos = upper_bound(arr.begin(), arr.end(), n) - arr.begin()-1;
        while (!DFS(startPos, n, 0)) depth++;
        for (int i = 0; i < SZ(ans); i++)
            if (!i) printf("%d", ans[i]);
            else printf(" %d", ans[i]);
        puts("");
    }
    return 0;
}
```
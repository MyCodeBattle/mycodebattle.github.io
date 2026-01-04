---
categories: Posts
date: 2015-01-23 00:00:00
title: Codeforces 507C - Guess Your Way Out! (思维)
tags: []
layout: post
---

## 题意

k高满二叉树，现在要求出在访问第n个叶子节点之前访问过多少结点。

## 思路

先确定根到目标叶子的路径。  
如果两个l或者两个r连在一起，就加上右边分支的节点数。

路径如何确定？  
我是先找到目标结点正常的编号，就是二叉树从左到右递增的编号。  
然后倒着往上找。

细节写得有些不优雅。。


```c++
int main()
{
    LL h, n;
    cin >> h >> n;
    if (h == 1 && n == 2)
    {
        printf("2\n");
        return 0;
    }
    string path;
    LL targetNode = (1ll<<h) + n - 1;
    while (targetNode != 1)
    {
        if (targetNode & 1) path += "r";
        else path += "l";
        targetNode >>= 1;
    }
    reverse(path.begin(), path.end());
    int sz = SZ(path);
    LL ans = 1, cnt = 1;
    char pre = 'r';
    for (int i = 0; i < SZ(path); i++)
    {
        if (path[i] == pre)
        {
            if (i != SZ(path) - 1) ans++;
            ans += (1ll << (h-i)) - 1;
        }
        else ans += 1, pre = path[i];
    }
    if (path[sz - 2] != path[sz - 1]) ans--;
    cout << ans << endl;
    return 0;
}
```
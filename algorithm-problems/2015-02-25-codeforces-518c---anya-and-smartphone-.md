---
categories: Posts
date: 2015-02-25 00:00:00
title: Codeforces 518C - Anya and Smartphone (模拟)
tags: []
layout: post
---

## 题意

一个屏幕有K个图标，每点一次图标图标就会往前移一位，现在问总的点击次数。

## 思路

模拟即可。我还用了两个map来映射，其实只要用数组就行了。懒得改了。

## 代码


```c++
map<int, pii> mp;
map<pii, int> rmp;
 
void Swap(int a, int b)
{
    int xa = mp[a].X, ya = mp[a].Y;
    int xb = mp[b].X, yb = mp[b].Y;
    mp[a].X = xb, mp[a].Y = yb;
    mp[b].X = xa, mp[b].Y = ya;
    rmp[MP(xa, ya)] = b; rmp[MP(xb, yb)] = a;
}
 
int main()
{
    //ROP;
    ios::sync_with_stdio(0);
 
    int n, m, k;
    cin >> n >> k >> m;
    int tmp;
    for (int i = 0; i < n; i++)
    {
        cin >> tmp;
        mp[tmp] = {i/m, i%m};
        rmp[MP(i/m, i%m)] = tmp;
    }
    LL ans = 0;
    while (k--)
    {
        cin >> tmp;
        int x = mp[tmp].X, y = mp[tmp].Y;
        ans += x+1;
        if (x == 0 && y == 0) continue;
        //处理不跨页的情况
        if (y != 0)
        {
            int preElement = rmp[MP(x, y-1)];
            Swap(tmp, preElement);
        }
        if (y == 0) //跨页
        {
            int preElement = rmp[MP(x-1, m-1)];
            Swap(tmp, preElement);
        }
    }
    cout << ans << endl;
    return 0;
}
```
---
categories: Posts
date: 2015-01-29 00:00:00
title: UVa 1312 - Cricket Field (高效枚举)
tags: []
layout: post
---

## 题意

找出最大的正方形，不包含点。

## 思路

先仰慕帆神。

枚举左右边界，然后从下到上枚举上边界，维护最大值和左下角的坐标。

## 代码


```c++
int n, vis[MAXN], width;
vector<int> x;
pii P[MAXN];
 
bool cmp(const pii &a, const pii &b)
{
    return a.Y < b.Y;
}
 
void Handle()
{
    for (int i = 0; i < n; i++) scanf("%d%d", &P[i].X, &P[i].Y);
    x.clear();
    MS(vis, 0);
    vis[0] = 1;
    x.PB(0);
    for (int i = 0; i < n; i++)
    {
        if (!vis[P[i].X])
        {
            vis[P[i].X] = 1;
            x.PB(P[i].X);
        }
    }
    if (!vis[width]) x.PB(width);
    sort(x.begin(), x.end());
}
 
int main()
{
    //ROP;
    int height, T;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%d%d%d", &n, &width, &height);
        Handle();
        sort(P, P + n, cmp);
        int maxValue = 0, curBottom;
        pii ans;
        for (int i = 0; i < SZ(x); i++)
        {
            for (int j = i+1; j < SZ(x); j++)
            {
                int tmpWide = x[j] - x[i], curBottom = 0;
                for (int k = 0; k < n; k++)
                {
                    if (P[k].X <= x[i] || P[k].X >= x[j]) continue;
                    int tmpHeight = P[k].Y - curBottom;
                    if (maxValue < min(tmpWide, tmpHeight))
                    {
                        maxValue = min(tmpWide, tmpHeight);
                        ans.X = x[i]; ans.Y = curBottom;
                    }
                    curBottom = P[k].Y;
                }
                int tmpHeight = height - curBottom;
                if (maxValue < min(tmpWide, tmpHeight))
                {
                    maxValue = min(tmpWide, tmpHeight);
                    ans.X = x[i]; ans.Y = curBottom;
                }
            }
        }
        printf("%d %d %d\n", ans.X, ans.Y, maxValue);
        if (T) puts("");
    }
    return 0;
}
```
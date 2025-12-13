---
categories: Posts
date: 2015-02-01 00:00:00
title: SDUT 2157 - Greatest Number (二分)
tags: []
layout: post
---

## 题意

选出4个以内的数，使得值最接近K。

## 思路

两两相加到一个数组里，枚举一个，另一个二分。

## 代码


```c++
vector<int> arr, sum;
 
int main()
{
    //ROP;
    int n, limit;
    while (~scanf("%d%d", &n, &limit), n + limit)
    {
        arr.clear(); sum.clear();
        for (int i = 0; i < n; i++)
        {
            int a;
            scanf("%d", &a);
            if (a <= limit) arr.PB(a);
        }
        arr.PB(0);
        for (int i = 0; i < SZ(arr); i++)
            for (int j = i; j < SZ(arr); j++)
                if (arr[i] + arr[j] <= limit) sum.PB(arr[i] + arr[j]);
        sort(sum.begin(), sum.end());
        int ans = 0;
        for (int i = 0; i < SZ(sum); i++)
        {
            int cur = limit - sum[i];
            int l = 0, r = SZ(sum), mid;
            int tmp = 0;
            while (l <= r)
            {
                mid = MID(l, r);
                if (sum[mid] > cur) r = mid - 1;
                else
                {
                    tmp = max(tmp, sum[mid]);
                    l = mid + 1;
                }
            }
            ans = max(ans, sum[i] + tmp);
        }
        printf("Case %d: %d\n", ++cases, ans);
        puts("");
    }
    return 0;
}
```
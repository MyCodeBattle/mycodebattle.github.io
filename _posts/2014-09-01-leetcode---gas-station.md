---
categories: Posts
date: 2014-09-01 00:00:00
title: LeetCode - Gas Station
tags: []
layout: post
---

## 题意

判断从哪个加油站开始可以走一圈。

## 思路

一开始偷懒，直接再赋值一遍，这样就不用处理到头的情况了，MLE。

不过只用一个变量来记录就行，如果超出了就让它等于0，意思就从第一个开始。

走过的加油站的数量专门由k来统计。

## 代码


```c++
class Solution {
public:
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost)
    {
        int len = gas.size(), k;
        for (int i = 0; i < gas.size(); i++) //枚举起点
        {
            int rem = 0, cnt = i;
            for (k = 0; k < len; k++)
            {
                if (cnt + k == len) cnt = -k;
                rem += gas[cnt + k];
                if (rem < cost[cnt + k]) break;
                rem -= cost[cnt + k];
            }
            if (k == len) return i;
        }
        return -1;
    }
};
```
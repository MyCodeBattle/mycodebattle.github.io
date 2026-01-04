---
categories: Posts
date: 2015-01-23 00:00:00
title: HDU 1005 - Number Sequence (规律)
tags: []
layout: post
---

## 思路

观察到一个数由前两个数决定，前两个数的组合只能有49种情况，所以循环节必在49之内。

## 代码


```c++
int arr[100];
 
int main()
{
    int a, b, c;
    arr[1] = arr[2] = 1;
    while (cin >> a >> b >> c, a + b + c)
    {
        for (int i = 3; i <= 52; i++) arr[i] = (a * arr[i - 1] + b * arr[i - 2]) % 7;
        int fir = 0, ed = 0;
        for (int i = 1; i <= 49; i++)
        {
            for (int j = i + 1; j <= 52; j++)
                if (arr[i] == arr[j] && arr[i + 1] == arr[j + 1])
                {
                    fir = i;
                    ed = j - 1;
                    break;
                }
            if (ed) break;
        }
        printf("%d\n", arr[(c-fir) % (ed-fir+1) + fir]);
    }
    return 0;
}
```
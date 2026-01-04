---
categories: Posts
date: 2015-01-24 00:00:00
title: HDU 1111 - Secret Code (DFS + 一点数学 + 模拟)
tags: []
layout: post
---

## 题意

题意看了半小时才懂。

有两个复数，X和B。

$X = a_0 + a_1*B + a_2 * B^2 + ... + a_n * B^n$

现在要求出$a_0 ~ a_n$

## 思路

假设现在从头开始算。

复数除法：$\frac {a + b_i}{c + d_i} = \frac {ac + bd}{c^2 + d^2} + \frac {bc - ad}{c^2 + d^2}i$

那么枚举$a_0, X_r - a_0$之后两边同除B，显然这时候要实部和虚部都要分别整除$c^2 + d^2$。

然后递归下去计算即可。

## 代码


```c++
LL Xi, Xr, Bi, Br, limit;
int cnt, ans[MAXN];
bool flag;
 
void DFS(LL r, LL ii, int pos)
{
    if (pos > 100 || flag) return;
    if (ii == 0 && r == 0)
    {
        cnt = pos;
        flag = true;
        return;
    }
    for (int i = 0; i*i < limit; i++)
    {
        ans[pos] = i;
        LL a = (r-i) * Br + ii*Bi, b = ii*Br - (r-i) * Bi;
        if (a % limit == 0 && b % limit == 0)
        {
            DFS(a / limit, b / limit, pos + 1);
            if (flag) return;
        }
    }
}
 
int main()
{
    //ROP;
    ios::sync_with_stdio(0);
 
    int T, i, j;
    cin >> T;
    while (T--)
    {
        flag = false;
        cin >> Xr >> Xi >> Br >> Bi;
        limit = Br*Br + Bi*Bi;
        DFS(Xr, Xi, 0);
        if (!flag) cout << "The code cannot be decrypted.";
        else
        {
            cout << ans[cnt-1];
            for (int i = cnt-2; i >= 0; i--) cout << "," << ans[i];
        }
        cout << endl;
    }
    return 0;
}
```
---
categories: Posts
date: 2015-03-04 00:00:00
title: PKU 2192 - Zipper (DP | DFS)
tags: []
layout: post
---

## 题意

问两个词能不能拼成一个词。

## 思路

DFS和DP都行。

$dp[i][j]$表示第一个单词前i个和第二个单词前j个能否拼成第三个单词前i+j个。


```c++
if (dp[i-1][j] && s1[i] == s[i+j] || dp[i][j-1] && s2[j] == s[i+j]) dp[i][j] = true;
```


不过有些人说DFS过是因为数据水是什么心态？说得跟DP能过所以其他方法都不能过不然就是数据水一样。

## 代码


```c++
string s1, s2, target;
 
bool DFS(int l1, int l2, int tar)
{
    if (l1+l2+1 != tar) return false;
    if (tar+l1+l2 == -3) return true;
    if (l1 != -1 && target[tar] == s1[l1])
        if (DFS(l1-1, l2, tar-1)) return true;
    if (l2 != -1 && target[tar] == s2[l2])
        if (DFS(l1, l2-1, tar-1)) return true;
    return false;
}
 
int main()
{
    //ROP;
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        printf("Data set %d: ", ++cases);
        cin >> s1 >> s2 >> target;
        printf("%s\n", (DFS(SZ(s1)-1, SZ(s2)-1, SZ(target)-1) ? "yes": "no"));
    }
    return 0;
}
```
 
```c++
bool dp[MAXN][MAXN];
char s1[MAXN], s2[MAXN], tar[MAXN<<1];
 
bool Solve()
{
    int l1 = strlen(s1+1), l2 = strlen(s2+1), ltar = strlen(tar+1);
    for (int i = 1; i <= l2; i++)
        if (s2[i] == tar[i]) dp[0][i] = true;
    for (int i = 1; i <= l1; i++)
        if (s1[i] == tar[i]) dp[i][0] = true;
    for (int i = 1; i <= l1; i++)
        for (int j = 1; j <= l2; j++)
            if (dp[i-1][j] && s1[i] == tar[i+j] || dp[i][j-1] && s2[j] == tar[i+j]) dp[i][j] = true;
    return dp[l1][l2];
}
 
int main()
{
    //ROP;
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        MS(dp, 0);
        printf("Data set %d: ", ++cases);
        scanf("%s%s%s", s1+1, s2+1, tar+1);
        printf("%s\n", Solve() ? "yes": "no");
    }
    return 0;
}
```
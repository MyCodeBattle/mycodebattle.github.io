---
categories: Posts
date: 2014-10-01 00:00:00
title: PKU 3080 - Blue Jeans (KMP + 枚举)
tags: []
layout: post
---

## 题意

找出最长公共子序列。

## 思路

枚举第一个字符串的子串，然后对后面的KMP。

偷懒用了string，140+ms不忍直视

这题直接暴力都比用KMP快。。真是。。

## 代码
    
    
    123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104

| ```c++
#include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>#define LL long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 10000 + 10;const int MOD = 1e9 + 7;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} }; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int f[15][100];string str[15]; void GetFail(int r){    f[r][0] = f[r][1] = 0;    int m = SZ(str[r]);    for (int i = 1; i < m; i++)    {        int j = f[r][i];        while (j && str[r][j] != str[r][i]) j = f[r][j];        f[r][i + 1] = (str[r][j] == str[r][i] ? j + 1 : 0);    }} bool KMP(string P, int r){    int m = SZ(str[r]), n = SZ(P);    int j = 0;    for (int i = 0; i < m; i++)    {        while (j && P[j] != str[r][i]) j = f[r][j];        if (P[j] == str[r][i]) j++;        if (j == n) return true;    }    return false;} int main(){    //ROP;    ios::sync_with_stdio(0);    int T, i, j, n, k;    cin >> T;    string tmp, sub;    while (T--)    {        bool flag = false;        cin >> n;        for (i = 0; i < n; i++)        {            cin >> tmp;            str[i] = tmp;        }        string ans;        for (i = 0; i < n; i++) GetFail(i);        for (i = 0; i < SZ(str[0]); i++)            for (j = 3; j + i - 1 < SZ(str[0]); j++)            {                sub = str[0].substr(i, j);                for (k = 1; k < n; k++)                    if (!KMP(sub, k)) break;                if (k == n)                {                    flag = true;                    if (ans.size() < sub.size()) ans = sub;                    else if (ans.size() == sub.size()) ans = min(ans, sub);                }            }        if (flag) cout << ans << endl;        else cout << "no significant commonalities" << endl;    }    return 0;}
```  

    12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879

| ```c++
#include <cstdio>#include <stack>#include <set>#include <iostream>#include <string>#include <vector>#include <queue>#include <functional>#include <cstring>#include <algorithm>#include <cctype>#include <string>#include <map>#include <cmath>#define LL long long#define SZ(x) (int)x.size()#define Lowbit(x) ((x) & (-x))#define MP(a, b) make_pair(a, b)#define MS(arr, num) memset(arr, num, sizeof(arr))#define PB push_back#define F first#define S second#define ROP freopen("input.txt", "r", stdin);#define MID(a, b) (a + ((b - a) >> 1))#define LC rt << 1, l, mid#define RC rt << 1|1, mid + 1, r#define LRT rt << 1#define RRT rt << 1|1#define BitCount(x) __builtin_popcount(x)const double PI = acos(-1.0);const int INF = 0x3f3f3f3f;using namespace std;const int MAXN = 10000 + 10;const int MOD = 1e9 + 7;const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} }; typedef pair<int, int> pii;typedef vector<int>::iterator viti;typedef vector<pii>::iterator vitii; int f[15][100];string str[15]; int main(){ //   ROP;    ios::sync_with_stdio(0);	int T, i, j, n, k;	cin >> T;	string tmp, sub;	while (T--)	{		bool flag = false;		cin >> n;		for (i = 0; i < n; i++)		{			cin >> tmp;			str[i] = tmp;		}		string ans;		//for (i = 0; i < n; i++) GetFail(i);		for (i = 0; i < SZ(str[0]); i++)			for (j = 3; j + i - 1 < SZ(str[0]); j++)			{				sub = str[0].substr(i, j);				for (k = 1; k < n; k++)					if (str[k].find(sub) == string::npos) break;				if (k == n)				{					flag = true;					if (ans.size() < sub.size()) ans = sub;					else if (ans.size() == sub.size()) ans = min(ans, sub);				}			}		if (flag) cout << ans << endl;		else cout << "no significant commonalities" << endl;	}	return 0;}
```
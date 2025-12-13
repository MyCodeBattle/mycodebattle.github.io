---
categories: Posts
date: 2014-09-01 00:00:00
title: TopCoder SRM 633 Div2 Problem 250 - Target
tags: []
layout: post
---

#  [TopCoder SRM 633 Div2 Problem 250 - Target](/2014/09/topcoder-srm-633-div2-250/ "TopCoder SRM 633 Div2 Problem 250 - Target")

By [MyCodeBattle](http://mycodebattle.gitcafe.io/about "MyCodeBattle")

Published Sep 19 2014 18:36

**Contents**

  1. 1. 题意
  2. 2. 思路
  3. 3. 代码

* include 
* include 
* include 
* include 
* include 
* include 
* include 
* include 
* include 
* include 
* include 
* include 
* define LL long long
* define lowbit(x) ((x) & (-x))
* define MP(a, b) make_pair(a, b)
* define MS(arr, num) memset(arr, num, sizeof(arr))
* define PB push_back
* define ROP freopen(“input.txt”, “r”, stdin);

## 题意

打出相同的图案。

## 思路

做这题的时候用了最2的做法。找出规律，一条一条算，后来看到别人十几行的代码简直要撞墙。

## 代码

```  
​#include 

# include 

# include 

# include 

# include 

# include 

# include 

# include 

# include 

# include 

# include 

# include 

# include 

# define LL long long

# define lowbit(x) ((x) & (-x))

# define MP(a, b) make_pair(a, b)

# define MS(arr, num) memset(arr, num, sizeof(arr))

# define PB push_back

# define ROP freopen(“input.txt”, “r”, stdin);

const double PI = acos(-1.0);  
const int INF = 0x3f3f3f3f;  
using namespace std;

class Target {  
public:  
vector draw(int n) {  
vector ans;  
int mid = (n + 1) >> 1;  
for (int i = 1; i <= n; i++)  
{  
string str;  
if (i & 1)  
{  
int single = (i - 1) >> 1;  
if (i <= mid)  
{  
string temp = “# “;  
for (int cnt = 0; cnt < single; cnt++)  
str += temp;  
str.append(n - (i - 1) _2, ‘#’);  
temp = “ #”;  
for (int cnt = 0; cnt < single; cnt++) str += temp;  
}  
else  
str = ans[2 _ mid - i - 1];  
//str.append(10);  
ans.push_back(str);  
}  
else  
{  
if (i > mid)  
str = ans[2 _mid - i - 1];  
else  
{  
string temp = “# “;  
for (int cnt = 1; cnt <= (i >> 1); cnt++) str += temp;  
int emp = n - 4 _ (i >> 1);  
str.append(emp, ‘ ‘);  
temp = “ #”;  
for (int cnt = 1; cnt <= (i >> 1); cnt++) str += temp;  
}  
//str.append(10);  
ans.push_back(str);  
}  
}  
return ans;  
}  
};

[Solving Reports](/categories/Solving-Reports/)

[Online Judge - TopCoder](/tags/Online-Judge-TopCoder/)[Foundation - Strings](/tags/Foundation-Strings/)

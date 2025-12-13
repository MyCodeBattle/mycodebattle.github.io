---
categories: Posts
date: 2014-09-01 00:00:00
title: LeetCode - Evaluate Reverse Polish Notation
tags: []
layout: post
---

## 题意

计算逆波兰表达式。

## 思路

用栈。  
如果是数字就进栈，遇到运算符取出两个栈里的东西，算完以后进栈。最后留下一个元素在栈里。

注意处理负号。。。

## 代码
    
    
    1234567891011121314151617181920212223242526272829303132333435

| ```c++
class Solution {	stack<int> stk;	public:	int evalRPN(vector<string> &tokens)	{		vector<string>::iterator it;		for (it = tokens.begin(); it != tokens.end(); it++)		{			string tmp = *it;			if (isdigit(tmp[0]) || (tmp[0] == '-' && tmp.size() != 1)) stk.push(Convert(tmp));			else			{									int b = stk.top(); stk.pop();				int a = stk.top(); stk.pop();				int c;				if (tmp[0] == '+') c = a + b;				else if(tmp[0] == '-') c = a - b;				else if (tmp[0] == '*') c = a * b;				else c = a / b;				stk.push(c);			}		}		return stk.top();	}	int Convert(string str);}; int Solution::Convert(string str){	int ans = 0, sig = 1;	if (str[0] == '-') sig = -1;	for (int i = 0; i < str.size(); i++)		if (isdigit(str[i])) ans = ans * 10 + str[i] - '0';	return ans * sig;}
```
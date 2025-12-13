---
categories: Posts
date: 2014-09-01 00:00:00
title: 输入外挂
tags: []
layout: post
---

```c++
//适用于正负数,(int,long long,float,double)
template <class T>
bool Read(T &ret)
{
	char c; int sgn; T bit=0.1;
	if(c=getchar(),c==EOF) return 0;
	while(c!='-'&&c!='.'&&(!isdigit(c))) c=getchar();
	sgn=(c=='-')?-1:1;
	ret=(c=='-')?0:(c-'0');
	while(c=getchar(),isdigit(c)) ret=ret*10+(c-'0');
	if(c==' '||c=='\n'){ ret*=sgn; return 1; }
	while(c=getchar(),isdigit(c)) ret+=(c-'0')*bit,bit/=10;
	ret*=sgn;
	return 1;
}
```
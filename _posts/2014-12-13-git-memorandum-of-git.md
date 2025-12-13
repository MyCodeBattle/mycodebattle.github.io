---
categories: Posts
date: 2014-12-13 00:00:00
title: Git命令备忘
tags: []
layout: post
---

昨天刚开始接触Git，记一些常用命令备忘一下。


```c++
git init
```
 初始化仓库


```c++
git add <filename>
```
 把文件添加到暂存区


```c++
git commit -m "somthing"
```
 把暂存区里的文件提交到当前分支


```c++
git log
```
 查看提交历史


```c++
git reflog
```
 查看所有分支的提交记录


```c++
git reset HEAD@{n}/xxxxx
```
，回退


```c++
git status
```
 查看暂存区状态


```c++
git remote add origin git@github.com:{username}/{repository}.git
```
 把当前分支和远程分支关联起来


```c++
git push -u origin master
```
  
上面命令将本地的master分支推送到origin主机，同时指定origin为默认主机，后面就可以不加任何参数使用git push了


```c++
git push origin master
```
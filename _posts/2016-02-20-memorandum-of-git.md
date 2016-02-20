---
categories: Memorandum
date: 2015-10-28 16:21:58
title: Git命令备忘
tags: 
layout: post
---

昨天刚开始接触Git，记一些常用命令备忘一下。

`git init` 初始化仓库

`git add <filename>` 把文件添加到暂存区

`git commit -m "somthing"` 把暂存区里的文件提交到当前分支

`git log` 查看提交历史

`git reflog` 查看所有分支的提交记录

`git reset HEAD@{n}/xxxxx`，回退

`git status` 查看暂存区状态

`git remote add origin git@github.com:{username}/{repository}.git` 把当前分支和远程分支关联起来

`git push -u origin master`
上面命令将本地的master分支推送到origin主机，同时指定origin为默认主机，后面就可以不加任何参数使用git push了

`git push origin master`

`git remote`  列出当前存在的远程分支

`git reset HEAD filename` 有两个修改过的文件，我们想要分开提交，但不小心用 git add . 全加到了暂存区域。该命令能取消暂存的文件。
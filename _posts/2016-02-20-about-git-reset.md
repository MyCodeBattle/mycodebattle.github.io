---
categories: Article
date: 2016-01-04 19:11:55
title: 关于git reset
tags:
layout: post
---

`git reset`有两种模式。

- `git reset [-q] [<tree-ish>] [--] <paths>…​`
- `git reset [--soft | --mixed [-N] | --hard | --merge | --keep] [-q] [<commit>]`

第一种相当于git add的反操作。
`git reset 1.txt`
也可以从某个commit中拿出某个文件放到当前的暂存区中。
`git reset <tree-ish> 1.txt`
另一个命令是`git checkout <tree-ish> 1.txt`，从某个commit中拿出文件放到暂存区和工作区中。


第二种模式中
- --mixed 这是默认的参数，重置成某个commit的暂存区而不重置工作区。
- --soft 不动暂存区和工作区，仅仅将指针指向某个commit。如果对上次提交不满意，相当于撤消了一次提交。
- --hard 重置暂存区和工作区。




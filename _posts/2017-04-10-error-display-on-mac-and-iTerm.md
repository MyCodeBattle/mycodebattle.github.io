---
title: Mac OS 下用 iTerm 连接服务器时终端显示不出中文的解决办法
layout: post
date: 2017-04-10
categories: 
---

作者：一绊
链接：https://www.zhihu.com/question/20117388/answer/62263969

# 问题
服务器是 Ubuntu，用 Mac 的 iTerm2 SSH 连上去，终端显示中文乱码，也不能输入中文，然而本地终端可以显示和输入。


# 原因

这种情况一般是终端和服务器的字符集不匹配，MacOSX下默认的是utf8字符集。输入locale可以查看字符编码设置情况，而我的对应值是空的。因为我在本地和服务器都用zsh替代了bash，而且使用了oh-my-zsh，而默认的.zshrc没有设置为utf-8编码，所以本地和服务器端都要在.zshrc设置，步骤如下，bash对应.bash_profile或.bashrc文件。

# 解决办法


1. 在终端下输入vim ~/.zshrc
或者使用其他你喜欢的编辑器编辑~/.zshrc文件
2. 在文件内容末端添加：
> export LC_ALL=en_US.UTF-8  
> export LANG=en_US.UTF-8

接着重启一下终端，或者输入source ~/.zshrc使设置生效。

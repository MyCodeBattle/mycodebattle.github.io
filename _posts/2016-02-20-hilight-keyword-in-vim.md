---
categories: Article
date: 2015-09-09 22:10:45
title: vim自定义语法高亮 
tags:  
layout: post
---

转载自 http://www.cnblogs.com/plwang1990/p/4106695.html

 ## 定义语法规则 ## 

首先要创建自己的语法规则：
进入目录~/.vim/syntax，在该目录下新建文件mysyntax.vim（名称随意，.vim结尾即可）
windows用户目录为$VIM_INSTALL/vimfiles/syntax($VIM_INSTALL为vim的安装目录)

之后在mysyntax.vim中输入：

    syn keyword Conditional if
    syn keyword InternalFunction print input

这里我们指定了if为关键词Conditional，print与input为关键词InternalFunction，Conditional与InternalFunction为我们自己定义的变量名。
暂时就添加这两行，先看看效果。

 ## 设置识别文件类型 ## 

接下来要设置vim在读入.me文件时，自动识别其语法为我们刚才定义的mysyntax：
进入目录~/.vim/ftdetect，在该目录下新建文件mysyn.vim（名称随意，.vim结尾即可）
windows用户目录为$VIM_INSTALL/vimfiles/ftdetect

之后在mysyn.vim中输入：`au BufRead,BufNewFile *.me set filetype=mysyntax`
filetype的名字即为上一步新建的文件的文件名

 ## 给定义的语法变量指定颜色 ## 

在vim中输入:colorscheme查看当前使用的color文件名，例：molokai
然后打开~/.vim/colors/molokai.vim

在其中添加如下两行新定义的变量的颜色

    hi Conditional guifg=#8DA5ED
    hi InternalFunction guifg=Orchid

然后再重新打开test.me，流程走完
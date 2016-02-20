---
categories: Article
date: 2015-09-09 17:30:38
title: 给vim增加Vundle和NERDTree插件
tags: 
layout: post
---

先给vim加了两个插件。

windows下的插件应该放在`/Users/用户名/.vim`目录下。

然后clone一下vundle，编辑_vimrc。第一行的路径按照自己的改。

```
" 设置含有并且初始化Vundle的运行环境
set rtp+=~/.vim/bundle/vundle.vim/
call vundle#begin()

Plugin 'vundle.vim'
Plugin 'nerdtree'

call vundle#end()            " required
filetype plugin indent on    " required
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

set autochdir
let mapleader=","
let NERDTreeChDirMode=2
nnoremap <leader>file :NERDTree .<CR>
```

装NERDTree的时候也一样，放在同一个目录下。
这里有一个问题，理论上来说打开NERDTree的时候应该是当前目录，而我无论怎么开都是C:\System。

所以在_vimrc中加入
```
set autochdir
let mapleader=","
let NERDTreeChDirMode=2
nnoremap <leader>file :NERDTree .<CR>
```

每次在normal模式下键入`,file`就能打开当前目录下的树了。

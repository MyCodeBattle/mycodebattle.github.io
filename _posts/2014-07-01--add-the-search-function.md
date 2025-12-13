---
categories: Posts
date: 2014-07-01 00:00:00
title: 为博客增加搜索功能
tags: []
layout: post
---

## 扯蛋

自从用这个模板几天后，我就发现了不方便之处：有时候想要找一篇以前的题解，只能一页一页用浏览器自带的
```c++
Control + F
```
去找，非常不方便。博客上的那个Search也用不了，只能看不能用，这感觉真是。。。但是自己什么也不会，这事只能先放下了。

某一天，我在群里看到**懒懒熊(lanlazy.com)** 在群里说他改了一下他的博客，可以搜索了。我去看了一下，非常地方便。然后就问他实现的方法。

懒懒熊：“!%^$#%^&#%^@%!#&#%^&#%^@!#&#%。”

我：（ ＴДＴ）

然后我就厚着脸皮请他做一个教程，懒懒熊欣然同意。  
他的教程见此[利用AJAX+RSS实现博客站内搜索匹配功能](http://lanlazy.com/2014/07/09/%E5%88%A9%E7%94%A8AJAX+RSS%E5%AE%9E%E7%8E%B0%E5%8D%9A%E5%AE%A2%E7%AB%99%E5%86%85%E6%90%9C%E7%B4%A2%E5%8C%B9%E9%85%8D%E5%8A%9F%E8%83%BD/)

但是当我完成后发现还是不管用。然后昨晚懒懒熊特地帮我找原因，弄到十二点半。在此表示感谢(ˉ▽￣～)。

我就在这里把他的教程重新整理一下，实现该功能的思路可以去看他的文章，在此我就略过了。

下文中的我都是指懒懒熊。。

## 实施

所有用到的文件我（这个是我）已经打包，请到[这里](http://pan.baidu.com/s/1qWFedn2)下载

### 改造原有搜索框

-文件模板在
```c++
你的主题\layout\_partial\header.ejs
```
 的26行左右.  
找到判断是否开启谷歌搜索的判断语句，为了不破坏原有的代码，我们把**else** 中部分改为如下


```c++
<form id="searchform" class="search" action="<%- config.root %>search/index.html" method="get" accept-charset="utf-8">
<label>Search</label>
<input type="text" id="search" autocomplete="off" name="q" maxlength="20" placeholder="<%= __('search') %>" />
</form>
```
 

### 将autocomplete.js引入

大家将下载过来的
```c++
autocomplete.js
```
和
```c++
common.js
```
，放到
```c++
\theme\你的主题\source\js
```
下  
在每个页面都要加载，所以要修改模板
```c++
head.ejs
```
  
在
```c++
head.ejs
```
中添加，注意加载顺序


```c++
<script src="<%- config.root %>js/jquery-2.1.0.min.js"></script>
<script src="<%- config.root %>js/autocomplete.js"></script>
<script src="<%- config.root %>js/common.js"></script>
```
 

### 添加样式

autocomplete插件本身带有自动完成框的样式，由于我是截取使用的，样式部分没有采用单独的css而是直接写在了head里，大家可以采用独立css link的方式加载，结构更好一些。当时为了先实现，代码搞的脏。  
在
```c++
head.ejs
```
中添加以下代码


```c++
<style type="text/css">
        .ac_results {
            padding: 0px;
            border: 1px solid black;
            background-color: white;
            overflow: hidden;
            z-index: 99999;
        }
        .ac_results ul {
            width: 100%;
            list-style-position: outside;
            list-style: none;
            padding: 0;
            margin: 0;
        }
        .ac_results li {
            margin: 0px;
            padding: 2px 5px;
            cursor: default;
            display: block;
            font: menu;
            font-size: 12px;
            line-height: 16px;
            overflow: hidden;
        }
        .ac_loading {
            background: #FFF;
        }
        .ac_odd {
            background-color: #EEE;
        }
        .ac_over {
            background-color: #AAA;
            color: #FFF;
        }
    </style>
```
 

### 替换
```c++
jquery-2.1.0.min
```


因为我原本的文件是
```c++
jquery-2.0.3.min
```
，不能实现该功能。后来我把它替换成
```c++
jquery-2.1.0.min
```
就可以了。不过大家最好先备份一下原来的文件。。  
找到
```c++
\themes\你的主题\source\js
```
，替换。

### 执行hexo clean

这步一定要执行，不然没效果。

顺便提一下，可能有的主题（比如我这个）默认设定atom.xml中记录的文章数是15个。这样就会导致只能搜最近的十五篇文章。  
如果想要搜索全部的文章，可以到根目录下的
```c++
_config.yml
```
中，增加


```c++
feed:
  type: atom
  path: atom.xml
  limit: 200
```
 

limit填写需要保存的文章数。  
不过这样atom.xml会变得越来越大。正在寻找解决办法。

解决办法如下：  
找到
```c++
\根目录\node_modules\hexo-generator-feed
```
，打开
```c++
atom.ejs
```
，删除第23行的
```c++
<content type="html"><%-: post.content | cdata %></content>
```
，不过这样做了之后正常的RSS功能就坏了，就看大家舍不舍得了。

## 大功告成~
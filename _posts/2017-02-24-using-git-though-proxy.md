---
title: 通过代理使用 Git
layout: post
date: 2017-02-24
categories: Git
---

原文链接http://cms-sw.github.io/tutorial-proxy.html

昨天`Github`竟然被墙了，导致 push 不上去。

## 通过 SSH 协议连接 Git 仓库

如果是这样连接远程的，就是通过 SSH 协议。

> git@github.com:cms-sw/cmssw.git  
ssh://git@github.com/cms-sw/cmssw.git


这样的话，要配置 SSH 本身的配置文件，设置`ProxyCommand`选项在 ~/.ssh/config。

```
Host github.com
    User                    git
    ProxyCommand            nc -x localhost:1080 %h %p
```

## 通过 HTTP 或者 HTTPS 协议连接


如果是这样的

>http://github.com/cms-sw/cmssw.git   
https://github.com/cms-sw/cmssw.git


要这么配置

```
git config --global http.proxy socks5://localhost:1080
```

## 通过 Git 协议

如果是这样的

```
git://github.com/cms-sw/cmssw.git
```

就这么搞

```
git config --global core.gitproxy "git-proxy"
git config --global socks.proxy "localhost:1080"
```


# ToolCover

[![codebeat badge](https://codebeat.co/badges/03386646-bf13-40a4-a8a2-f81cdfef59a2)](https://codebeat.co/projects/github-com-williamfzc-toolcover-master)
[![Maintainability](https://api.codeclimate.com/v1/badges/24dc28bf1389249b3a19/maintainability)](https://codeclimate.com/github/williamfzc/ToolCover/maintainability)

以网页的形式，旨在用最简单的方式为所有命令行程序提供一个跨平台、美观的交互方案。

## 使用方法

目前只支持linux与mac系统。

1. 强烈建议先star再下载
1. `git clone`之后先运行`manage.py`查看教程
1. 如果运行有误，通常是config.py中配置的问题，根据需要自行修改
1. 运行后打开浏览器访问本地5000端口，开始教程

运行自己的程序：

1. 拷贝程序到`app/packages`目录下（需要把原有的test_app移除）
1. 根据需要在config.py中配置
1. 运行后打开浏览器访问本地5000端口，即可与子程序交互

一般使用场景多运行于服务器，由客户端访问，在`manage.py`中调节。


## 优势

- 非常适用于局域网做展示或者为一系列命令行工具提供交互。
- 经过简单配置就可以直接将命令行工具转变成有UI交互，非常方便。
- 几乎不需要对源代码进行改动，甚至不需要接触源代码。
- UI由bootstrap+jinja2实现，html形式展示，跨平台，甚至在手机等移动设备上也可以运行。

## 概念设计

- 利用了flask作为交互逻辑引擎
- 命令行app包嵌入到`app/packages`下
- 查找app包内的run.py与README.md作为程序的入口与文档
- 用子进程启动run.py，管理它的input与output
- 将input/output与路由进行绑定
- 由bootstrap渲染成UI

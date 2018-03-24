# ToolCover

[![codebeat badge](https://codebeat.co/badges/03386646-bf13-40a4-a8a2-f81cdfef59a2)](https://codebeat.co/projects/github-com-williamfzc-toolcover-master)
[![Maintainability](https://api.codeclimate.com/v1/badges/24dc28bf1389249b3a19/maintainability)](https://codeclimate.com/github/williamfzc/ToolCover/maintainability)

- 以网页的形式，旨在用最简单的方式为所有命令行程序提供一个跨平台、美观的交互方案。
- 基于flask + bootstrap。
- 目前只支持linux与mac系统。

## 使用方法

把大象放进冰箱一共需要几步？

1. 打开门
1. 把大象塞进去
1. 关上门

所有事情都应该如此简单。你只需要：

1. 把程序拷到`app/packages`里
1. 在config.py配置入口
1. 运行

然后就可以愉快的访问本地5000端口进行交互了！

> 源码自带教程，`git clone`之后可以直接运行查阅。推荐直接参照它学习使用。
位置`app/packages/test_app`

## 使用场景

- 使用场景多运行于服务器，由客户端访问实现远程控制。
- 非常适用于为命令行工具提供UI界面。

## 优势

- 非常适用于局域网做展示或者为一系列命令行工具提供交互。
- 经过简单配置就可以直接将命令行工具转变成有UI交互，非常方便。
- 几乎不需要对源代码进行改动，甚至不需要接触源代码。
- UI由bootstrap+jinja2实现，html形式展示，跨平台，甚至在手机等移动设备上也可以运行。

## Bug与建议

目前项目还在继续优化中，有任何建议欢迎指出。

欢迎fork/star/issue/PR。


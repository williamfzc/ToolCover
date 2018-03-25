# ToolCover

[![codebeat badge](https://codebeat.co/badges/03386646-bf13-40a4-a8a2-f81cdfef59a2)](https://codebeat.co/projects/github-com-williamfzc-toolcover-master)
[![Maintainability](https://api.codeclimate.com/v1/badges/24dc28bf1389249b3a19/maintainability)](https://codeclimate.com/github/williamfzc/ToolCover/maintainability)

- 以网页的形式，旨在用最简单的方式为所有命令行程序提供一个跨平台、美观的交互方案。
- 基于flask + bootstrap，python3。
- 目前只支持linux与mac系统。

## 灵感

对于python来说UI是个远古难题，官方的tkinter非常老气。前段时间尝试了各种第三方工具之后第一感觉都是，太麻烦了。通常情况下，这些UI框架的学习成本都不低，在编写工具之余还需要费心研究UI的制作很容易让开发者烦躁，在工作中深有体会。

个人认为，未来的应用肯定是趋向web化的，web应用能够很好地适配到不同平台，一次开发多处使用，那么，为什么我们不直接用web作为交互手段呢？

其实在这方面已经有flexx作为先驱，做的也很好，但开发过程远称不上简单，仍然需要对源码进行较大改动。

那么，有没有一种完全无缝对接的UI解决方案呢？有的。

## 效果

先看一下效果。如果我们的源码是这样：

![你的源码](https://upload-images.jianshu.io/upload_images/9838087-b34bea5985809c21.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

经过ToolCover的渲染，他将变成一个**可以交互**的web页面：

![效果](https://upload-images.jianshu.io/upload_images/9838087-c6a75d7e724dcdcd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

你只需要在编程的时候正常使用标准输入输出，就可以渲染出合适的web页面，并且用它进行交互。

当然，你也可以不按上面的实例来写，你只需要考虑在终端中输出与输入应该是什么样，ToolCover会自动完成这个过程，没有学习成本。


## 使用方法

把大象放进冰箱一共需要几步？

1. 打开门
1. 把大象塞进去
1. 关上门

所有事情都应该如此简单。你只需要：

1. 把程序拷到`app/packages`里
1. 在config.py配置入口
1. 运行 `python manage.py`

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


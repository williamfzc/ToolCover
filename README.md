# ToolCover

[![codebeat badge](https://codebeat.co/badges/03386646-bf13-40a4-a8a2-f81cdfef59a2)](https://codebeat.co/projects/github-com-williamfzc-toolcover-master)

以网页的形式，旨在用最简单的方式为所有命令行程序提供一个跨平台、美观的交互方案。

## 对比

目前python层面上做UI的常见方法主要有两种：

### 原生方法

python官方提供了tkinter作为原生UI的实现，而这套UI已经过时了。
而且，没有图形化的辅助，tkinter的纯代码实现对使用者而言非常不友好。

### 第三方

wxpython与pyqt是比较有名的两大UI库。

- wxpython
    - 很大程度上美化了控件，降低使用的复杂度。
    - 具有跟tkinter同样的问题，没有图形化界面非常不友好。
- pyqt
    - qt是大名鼎鼎的UI解决方案，有图形界面。
    - 目前是一种比较好的方案，唯一的不足大概是对于小项目来说过于笨重。

### 同类产品

- flexx
    - 以html形式制造app的创意来源
    - 使用方法与传统无异，仍然需要在源代码中绑定控件
    - 控件样式比较固化
- gooey
    - 最小改动来制造app的创意来源
    - 使用装饰器就可以将命令行程序转换成具备UI的app
    - 理念先进，但基于桌面平台    

## 优势

- 经过增量配置就可以直接将命令行工具转变成有UI交互，配置非常方便。
- 不需要对源代码进行改动，甚至不需要接触源代码。
- UI由bootstrap+jinja2实现，html形式展示，跨平台，甚至在手机等移动设备上也可以运行。

## 概念设计

- 命令行app包嵌入到`app/packages`下
- 查找app包内的run.py与README.md作为程序的入口与文档
- 用子进程启动run.py，管理它的input与output
- 将input/output与路由进行绑定
- 由bootstrap渲染成UI

## 后续

- 普通模式与自定义模式
    - 普通模式将直接接触app的输入输出，按默认方式定义UI
    - 自定义模式可以使用提供的API自定义UI内容
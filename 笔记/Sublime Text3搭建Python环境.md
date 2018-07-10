# Sublime Text3搭建Python环境

## Package Control

快捷键`ctrl+c`调出控制台,输入下面代码:

```
import urllib.request,os,hashlib; h = '6f4c264a24d933ce70df5dedcf1dcaee' + 'ebe013ee18cced0ef93d5f746d80ef60'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
```

按下 `Ctrl+Shift+P `调出命令面板输入` install `调出` Install Package `选项并回车，然后在列表中选中要安装的插件。

## SideBarEnhancements

可用于进行ST3的浏览器预览,并可自定义浏览器预览的快捷键。

安装此插件，点击工具栏的preferences > package setting > side bar > Key Building-User，键入以下代码。

```
[
 
    //chrome
    { "keys": ["f1"], "command": "side_bar_files_open_with",
            "args": {
                "paths": [],
                "application": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
                "extensions":".*"
            }
     },
    //firefox
    { "keys": ["f2"], "command": "side_bar_files_open_with",
             "args": {
                "paths": [],
                "application": "E:\\软件\\Firefox\\firefox.exe",
                "extensions":".*" //匹配任何文件类型
            }
    },
    //ie
     { "keys": ["f3"], "command": "side_bar_files_open_with",
             "args": {
                "paths": [],
                "application": "C:\\Program Files\\Internet Explorer\\iexplore.exe",
                "extensions":".*"
            }
    },
    ]
```

## Anaconda

Python的终极插件。

白框解决:

> Sublime > Preferences > Package Settings > Anaconda > Settings – Default 下修改 linting behaviour 选项即可

```

```



## SublimeREPL

SublimeREPL 允许你在 Sublime Text 中运行各种语言（NodeJS ，Python，Ruby， Scala 和 Haskell 等等）。

接下来配置快捷键，打开 Sublime > Preferences > Key Building ，在右侧栏（ User 部分）添加下面的代码。下面的代码用 F5 来执行当前 Python 脚本，用 F4 来实现切换至 Python 命令行窗口。

```
[
    {"keys":["f5"],
    "caption": "SublimeREPL: Python - RUN current file",
    "command": "run_existing_window_command", "args":
    {"id": "repl_python_run",
    "file": "config/Python/Main.sublime-menu"}}
    ,
    {"keys":["f4"],
    "caption": "SublimeREPL: Python",
    "command": "run_existing_window_command", "args":
    {"id": "repl_python",
    "file": "config/Python/Main.sublime-menu"}}
]
```

## SublimeTmpl

SublimeTmpl能新建html、css、javascript、php、python、ruby六种类型的文件模板，所有的文件模板都在插件目录的templates文件夹里，可以自定义编辑文件模板

SublimeTmpl默认的快捷键:

```
ctrl+alt+h html
ctrl+alt+j javascript
ctrl+alt+c css
ctrl+alt+p php
ctrl+alt+r ruby
ctrl+alt+shift+p python
```

这里我想修改一下python模板，所以就需要进行如下操作：Sublime > Preferences > Package Settings > SublimeTmpl > Settings – User 添加如下代码。然后 ctrl+alt+shift+p 来新建一个模板试试看。

```
{  
    "disable_keymap_actions": false, // "all"; "html,css"  
    "date_format" : "%Y-%m-%d %H:%M:%S",  
    "attr": {  
        "author": "Wangzhen",  
        "email": "wang765256860@163.com",  
        "link": "None"  
    }  
} 
```

## AutoPEP8

自动排版

## 解决中文乱码

ConvertToUTF8
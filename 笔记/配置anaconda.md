# 配置anaconda

<!-- TOC -->

- [配置anaconda](#配置anaconda)
    - [MAC篇](#mac篇)
        - [下载安装](#下载安装)
        - [识别conda命令](#识别conda命令)
        - [修改vscode中的setting.json文件](#修改vscode中的settingjson文件)

<!-- /TOC -->

## MAC篇

### 下载安装

[下载地址][]

[下载地址]:
https://www.anaconda.com/download/#macos

### 识别conda命令

在终端中加入：

```
export PATH=~/anaconda3/bin:$PATH
```

### 修改vscode中的setting.json文件

找到如下两个参数`python.autoComplete.extraPaths` & `python.pythonPath`，把`site-packages` & `bin/python`的正确路径配置一下。

```
"python.pythonPath": "/usr/wangzhen/anaconda3/bin/python3.6",
"python.autoComplete.extraPaths": ["/Users/wangzhen/anaconda3/lib/python3.6/site-packages"]
```

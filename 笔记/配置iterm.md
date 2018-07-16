# 配置iterm.md

## 下载iterm

[iterm][]

[iterm]:
https://www.iterm2.com/

## 安装并打开iterm

![make iterm2 default](https://segmentfault.com/img/remote/1460000012786470)

打开偏好设置，在keys下设置热键

## 配色方案

[color][]

[color]:
https://iterm2colorschemes.com/

zenburn配色不错

## 安装oh-my-zsh

github:<https://github.com/robbyrussell/oh-my-zsh>

## 自动提示和代码补全

克隆仓库到本地~/.oh-my-zsh/custom/plugins 路径下

```
git clone git://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
```

用 vim 编辑 `.zshrc` 文件，找到插件设置命令，默认是 `plugins=(git)` ，我们把它修改为`plugins=(zsh-autosuggestions git)`

将字体调亮一点：

1. cd ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions
2. 编辑 zsh-autosuggestions.zsh 文件，修改`ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=10'`

## 语法高亮

安装zsh-syntax-highlighting插件

```
brew install zsh-syntax-highlighting
```

配置.zshrc文件，插入一行：

```
source /xxx/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
```
>/xxx/代表的是.zshrc的路径

加载.zshrc配置

```
source ~/.zshrc
```

## 卸载

```
uninstall_oh_my_zsh
```


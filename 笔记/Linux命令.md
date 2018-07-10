# Linux命令

[TOC]

## Linux目录结构：

> / ： 所有目录都在
> /boot : boot 配置文件、内核和其它启动 时所需的文件
> /etc ： 存放系统配置有关的文件
> /home ： 存放普通用户目录
> /mnt ： 硬盘上手动 挂载的文件系统
> /media ： 自动挂载（加载）的硬盘分区以及类似CD、数码相机等可移动介质。
> /cdrom ： 挂载光盘？ 
> /opt ： 存放一些可选程序,如某个程序测试版本,安装到该目录的程序的所有数据,库文件都存在同个目录下
> /root ： 系统管理员的目录，对于系统来说，系统管理员好比上帝，他可以对系统做任何操作，比如删除你的文件，一般情况下不要使用root用户。
> /bin ： 存放常用的程序文件（命令文件）。
> /sbin ： 系统管理命令，这里存放的是系统管理员使用的管理程序 
> /tmp ： 临时目录，存放临时文件，系统会定期清理该目录下的文件。
> /usr ： 在这个目录下，你可以找到那些不适合放在/bin或/etc目录下的额外的工具。比如游戏、打印工具等。/usr目录包含了许多子目录： /usr/bin目录用于存放程序;/usr/share用于存放一些共享的数据，比如音乐文件或者图标等等;/usr/lib目录用于存放那些不能直接 运行的，但却是许多程序运行所必需的一些函数库文件。/usr/local ： 这个目录一般是用来存放用户自编译安装软件的存放目录；一般是通过源码包安装的软件，如果没有特别指定安装目录的话，一般是安装在这个目录中。
>
> > /usr/bin/ 非必要可执行文件 (在单用户模式中不需要)；面向所有用户。
> > /usr/include/ 标准包含文件。
> > /usr/lib/ /usr/bin/和/usr/sbin/中二进制文件的库。
> > /usr/sbin/ 非必要的系统二进制文件，例如：大量网络服务的守护进程。
> > /usr/share/ 体系结构无关（共享）数据。
> > /usr/src/ 源代码,例如:内核源代码及其头文件。
> > /usr/X11R6/ X Window系统 版本 11, Release 6.
> > /usr/local/ 本地数据的第三层次， 具体到本台主机。通常而言有进一步的子目录， 例如:	 					            bin/、lib/、share/.
>
> /var ： 该目录存放那些经常被修改的文件，包括各种日志、数据文件；
>
> > /var/cache/ 应用程序缓存数据。这些数据是在本地生成的一个耗时的I/O或计算结果。应用程序必须能够再生或恢复数据。缓存的文件可以被删除而不导致数据丢失。
> > /var/lib/ 状态信息。 由程序在运行时维护的持久性数据。 例如：数据库、包装的系统元数据等。
> > /var/lock/ 锁文件，一类跟踪当前使用中资源的文件。
> > /var/log/ 日志文件，包含大量日志文件。
> > /var/mail/ 用户的电子邮箱。
> > /var/run/ 自最后一次启动以来运行中的系统的信息，例如：当前登录的用户和运行中的守护进程。现已经被/run代替[13]。
> > /var/spool/ 等待处理的任务的脱机文件，例如：打印队列和未读的邮件。
> > /var/spool/mail/ 用户的邮箱(不鼓励的存储位置)
> > /var/tmp/ 在系统重启过程中可以保留的临时文件。
>
> /lib : 目录是根文件系统上的程序所需的共享库，存放了根文件系统程序运行所需的共享文件。这些文件包含了可被许多程序共享的代码，以避免每个程序都包含有相同的子程序的副本，故可以使得可执行文件变得更小，节省空间。
> /lib32 : 同上
> /lib64 ： 同上
> /lost+found ： 该目录在大多数情况下都是空的。但当突然停电、或者非正常关机后，有些文件就临时存放在；
> /dev : 存放设备文件
> /run ： 代替/var/run目录，
> /proc : 虚拟文件系统，可以在该目录下获取系统信息，这些信息是在内存中由系统自己产生的，该目录的内容不在硬盘上而在内存里；
> /sys ： 和proc一样，虚拟文件系统，可以在该目录下获取系统信息，这些信息是在内存中由系统自己产生的，该目录的内容不在硬盘上而在内存里；

## 语言环境

查看是否安装了中文支持:

```
locale -a
```

## 软件管理apt

```
apt-cache search package 搜索包
apt-cache show package 获取包的相关信息，如说明、大小、版本等
sudo apt-get install package 安装包
sudo apt-get install package –reinstall 重新安装包
sudo apt-get -f install 强制安装
sudo apt-get remove package 删除包
sudo apt-get remove package –purge 删除包，包括删除配置文件等
sudo apt-get autoremove 自动删除不需要的包
sudo apt-get update 更新源
sudo apt-get upgrade 更新已安装的包
sudo apt-get dist-upgrade 升级系统
sudo apt-get dselect-upgrade 使用 dselect 升级
apt-cache depends package 了解使用依赖
apt-cache rdepends package 了解某个具体的依赖
sudo apt-get build-dep package 安装相关的编译环境
apt-get source package 下载该包的源代码
sudo apt-get clean && sudo apt-get autoclean 清理下载文件的存档
sudo apt-get check 检查是否有损坏的依赖
```

## date

显示当前日期

```
#格式化输出
date +"%Y%m%d %H%M%S"
```

## cal

显示日历

`cal -y`显示当前年份的日历

`cal 2017`显示指定年份的日历

## tzselect

选择时区

## 快捷键

```
ctrl-a ： 把光标移动到命令行最开始的地方。 
ctrl-e ： 把光标移动到命令行末尾。 
ctrl-u ： 清除命令行中光标所处位置之前的所有字符。 
ctrl-k ： 清除从提示符所在位置到行末尾之间的字符
ctrl-w ： 清除左边的字段 
ctrl-y ： 将会贴上被ctrl-u 或者 ctrl-k 或者 ctrl-w清除的部分。 
ctrl-r ： 将自动在命令历史缓存中增量搜索后面入的字符。 
tab ： 命令行自动补全－自动补全当前的命令行。如果启用自动补全脚本命令参数和选项也可以自动补齐。

ctrl-l ： 清屏
```

## cd命令

change directory

只输入`cd`代表切换到家目录

`.`表示当前目录

`..`表示上一级目录

`-`表示回到切换前的目录

## pwd

查看当前的工作路径

## 获取帮助

`-h`  `--help`  `info`  `man`

## chmod

更改文件权限

> user:rwx
>
> group:rwx
>
> other:rwx

其中r的值为4,w的值为2,x的值为1

```
chmod u+x,g+w f01　　//为文件f01设置自己可以执行，组员可以写入的权限
chmod u=rwx,g=rw,o=r f01
chmod 764 f01
chmod a+x f01　　//对文件f01的u,g,o都设置可执行属性
```

## mkdir

创建目录

```
mkdir abc  #为直接创建一个abc的目录
mkdir -p abc/ba/c/c   #可以创建多级目录
```

## 移动侧边栏

```
gsettings set com.canonical.Unity.Launcher launcher-position Left
```

## rm:删除命令

`rm a.txt`删除a文件

`rm -i a.txt`会提示是否删除

`rm -rf ab`可以删除目录ab

**少用,危险**

## mv

可以重命名

`mv p.py q.py`

`mv bb aa`将bb目录改名为aa

`mv q.py aa`将q.py移动到aa目录下

## cp

复制

`cp q.py w.py`复制为w.py

`cp -i q.py w.py`如果有重名的文件会提示是否覆盖

`cp -r aa ss`将aa目录复制并粘贴成一个ss目录,其目录下的子文件都会复制

## stat

查看文件的状态

## passwd

`passwd`修改当前用户密码

`passwd username`修改制定用户的密码,需要权限

## ls

ls:列出目标目录中所有的子目录和文件

`-a`用于显示所有文件和子目录

`-l`除了文件名之外,还将文件的权限、所有者、文件大小等信息详细列出来

`-r`将目录的内容清单以英文字母顺序的逆序显示

`-t`按文件修改时间进行排序,而不是按文件名进行排序

`-A`  同`-a`,但不列出"."和".."

## cat

```
cat file1  			#显示 file1的文件内容
cat file1 file2     # 显示file1和file2的文件内容 
cat -n file1  		#  由1开始对所有输出的行数编号
cat -s file  		# 当遇到连续2行以上的空白行，只保留一行空白行
```

*tac*是倒着输出,从最后一行开始

## wc(word count)

```
wc new.txt
2  2  17 new.txt     #输出的信息一次是:行数 字数 字节数 文件名称
#wc -m filename：显示一个文件的字符数
#wc -l filename：显示一个文件的行数
#wc -L filename：显示一个文件中的最长行的长度
#wc -w filename：显示一个文件的字数
#wc -c filename：显示一个文件的字节数
```

> wc统计的行是用换行符来确定的。

有以下几点说明：

1：一个汉字占三个字节，一个回车符等不可见字符也占一个字节
2：一行的末尾如果没有回车符，则不算是一行，也就是说，如果一个文件的最后一行末尾没有换行符，wc命令统计的行数会比实际行数少一，所谓实际行数是你所看到的行数，实际上，没有回车符，确实不能算作一行（注：若是在一个已存在的文本中，则默认为所有的行都有一个不可见的回车符）

## sort

```
sort：#sort将文件的每一行作为一个单位，相互比较，比较原则是从首字符向后，依次按ASCII码值进行比较，最后将他们按升序输出。
sort -u：它的作用很简单，就是在输出行中去除重复行。
sort -r：降序
sort -o：将排序结果输出到文件中  sort -r number.txt -o number.txt
sort -n：当比较10和2的时候，排序程序会先比较1和2，使用-n则会告诉程序进行数值比较

```

## cut

```
选项与参数：
-d  ：后面接分隔字符。与 -f 一起使用；
-f  ：依据 -d 的分隔字符将一段信息分割成为数段，用 -f 取出第几段的意思；
-c  ：以字符 (characters) 的单位取出固定字符区间；
```

## tee

读取标准输入的数据，并将其内容输出成文件。

```
cat sec.log | tee file1  # 读取sec.log ，并生成file1文件
cat sec.log | tee - a file1   # 读取sec.log ，并追加，
cat sec.log  |tee  file1 file2 
```



##history

查看执行过的命令

```
history  # 显示最近1000条历史命令
history 5   # 显示最后5条命令
!number# number为history之后命令前的序号：执行该条命令
!cat # 执行最后一条以cat开头的命令
```



## head和tail

head:输出文件的开始的部分， 可以指定行数 , 默认显示10行

```
head -n 5 file 
```

tail:查看文件尾部的内容。默认显示最后10行

```
tail file1
tail -n 5 file1
tail -f file1  # 动态监控文件
```

## which

查找其他命令的位置

## chown

更改文件的所有者和所有组

```
chown root:root  file
chown root   file  
chown :root   file
```

## useradd

添加用户

```
# -c 备注 加上备注。并会将此备注文字加在/etc/passwd中的第5项字段中         
#  -d 用户主文件夹。指定用户登录所进入的目录，并赋予用户对该目录的的完全控制权        
#  -e 有效期限。指定帐号的有效期限。格式为YYYY-MM-DD，将存储在/etc/shadow         
#  -f 缓冲天数。限定密码过期后多少天，将该用户帐号停用       
#  -g 主要组。设置用户所属的主要组  www.cit.cn           
#  -G 次要组。设置用户所属的次要组，可设置多组         
# -M 强制不创建用户主文件夹         
#  -m 强制建立用户主文件夹，并将/etc/skel/当中的文件复制到用户的根目录下         
#  -p 密码。输入该帐号的密码         
#  -s shell。用户登录所使用的shell         
#  -u uid。指定帐号的标志符user id，简称uid

useradd user1 # 添加用户 user1
useradd  -d /home/userTT user2 
```

## userdel

删除用户

```
userdel  user1  #
userdel -r user1

#  -r, --remove   用户主目录中的文件将随用户主目录和用户邮箱一起删除。在其它文件系统中的文件必须手动搜索并删除。
#    -f, --force    此选项强制删除用户账户，甚至用户仍然在登录状态。它也强制删除用户的主目录和邮箱，即使其它用户也使用同一个主目录或邮箱不属于指定的用户
```

## usermod

```
#　-c<备注> 　修改用户帐号的备注文字。 
#　-d登入目录> 　修改用户登入时的目录。 
#　-e<有效期限> 　修改帐号的有效期限。 
#　-f<缓冲天数> 　修改在密码过期后多少天即关闭该帐号。 
#　-g<群组> 　修改用户所属的群组。 
#　-G<群组> 　修改用户所属的附加群组。 
#　-l<帐号名称> 　修改用户帐号名称。 
#　-L 　锁定用户密码，使密码无效。 
#　-s<shell> 　修改用户登入后所使用的shell。 
#　-u<uid> 　修改用户ID。 


#　-U 　解除密码锁定。

usermod -G staff user2  # 将 newuser2 添加到组 staff 中 
usermod -l newuser1 newuser  # 修改 newuser 的用户名为 newuser1 
usermod -L newuser1  # 锁定账号 newuser1
usermod -U newuser1  # 解除对 newuser1 的锁定
```


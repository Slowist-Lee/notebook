# WSL 安装

参考[链接](https://blog.csdn.net/wojiuguowei/article/details/122100090?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522171968068416777224433087%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=171968068416777224433087&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-122100090-null-null.142^v100^pc_search_result_base8&utm_term=WSL&spm=1018.2226.3001.4187)

## 一、安装WSL 2.0

1. 启用适用于 Linux 的 Windows 子系统：打开powershell并输入：

```bash
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

![](https://github.com/Slowist-Lee/image-hosting/blob/master/WSL%201.png?raw=true)

2. 检查WSL2的要求：win+R打开运行，然后输入winver检查windows版本，此版本需要大于1903

![](https://github.com/Slowist-Lee/image-hosting/blob/master/WSL%203.png?raw=true)

3. 启用虚拟化:以管理员打开powershell输入下列命令

```
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

![在这里插入图片描述](https://github.com/Slowist-Lee/image-hosting/blob/master/WSL%204.png?raw=true)

4. 下载[X64的WSL2 Linux内核升级包](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)并安装

5. 设置WSL默认版本

```
wsl --set-default-version 2
```

## 二、安装Ubuntu20.04LTS

1. 打开Microsoft Store

2.  一般Windows都会将ubuntu加入到我的软件库中，如果没有可以自行搜索ubuntu然后安装，搜索到商店的有可能安装不了

![在这里插入图片描述](https://github.com/Slowist-Lee/image-hosting/blob/master/WSL%205.png?raw=true)

3.  找到Ubuntu 20.04LTS点击安装即可，这里我已经安装好了直接点击启动就行

4. 打开后设置初始的用户名和密码即可，如果出现参考的对象类型不支持尝试的操作，请重置下网络net winsock reset


<mark>Tips</mark>: 用户名应该只包含**小写**字母和数字，并且不能以数字开头，否则会报错

5. 设置root密码

> <mark>Tips</mark>: 这步往往可以省略，在初始化的时候应该已经设置

```
sudo passwd
```

## 三、配置ssh

1. 修改配置文件/etc/ssh/sshd_config，开启下列选项

```bash
sudo nano /etc/ssh/sshd_config
```

利用`nano`编辑器来编辑，以下三行去掉注释/修改至这个状态

- <mark>Tips</mark>: `nano`使用方法
   - 按 `Ctrl + O` （字母“o”，不是数字零），这将提示您输入文件名进行保存。
   - 按 `Enter` 确认保存文件（如果文件名没有变化，可以直接按 `Enter`）。
   - 按 `Ctrl + X` 退出`nano`编辑器。

```
PermitRootLogin yes ##允许root认证登录
PasswordAuthentication yes ##允许密码认证
PubkeyAuthentication yes
```

```
HostKey /etc/ssh/ssh_host_rsa_key
HostKey /etc/ssh/ssh_host_ecdsa_key
HostKey /etc/ssh/ssh_host_ed25519_key
```

2. 由于自带的openssh-server没有生成密钥所以需要生成密钥文件，否则会出现sshd: no hostkeys available – exiting.

<mark>Tips</mark>：若没有必要，不要给密钥设密码，若一定要设，`rsa_key` 最好别设密码

```bash
sudo ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key
sudo ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key
sudo ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N ""
sudo ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key -N ""
```

```bash
sudo chown root:root /etc/ssh/ssh_host_*
sudo chmod 600 /etc/ssh/ssh_host_*
```
   
3. 启动ssh

```
service ssh start
```

若之前启动过`ssh`, 尝试一下：

```bash
sudo systemctl restart ssh
```

再检验`ssh`的状态：
```bash
sudo systemctl status ssh
```

4. 开机启动ssh：win+R打开运行，输入shell::startup进入开机启动项，创建wsl_ssh_start.bat，其内容为

```
C:\Users\用户名\AppData\Local\Microsoft\WindowsApps\ubuntu2004.exe run "sudo service ssh restart"
```

## 5. 设置默认root登录：以管理员打开powershell，输入以下命令，

注意：用户名需要替换掉，版本页需要替换掉，如果wsl的路径不在这里可以去C:\Program Files\WindowsApps\XXX.UbuntuXXX\ubuntu版本.exe

```
C:\Users\用户名\AppData\Local\Microsoft\WindowsApps\ubuntu版本.exe config --default-user slowist
```

C:\Users\leexi\AppData\Local\Microsoft\WindowsApps\ubuntu2004.exe config --default-user slowist

<mark>Tip 1</mark>

!!! warning "如何查看Ubuntu的版本呢？"
	**查看 WindowsApps 目录**: 打开文件资源管理器，导航到：`C:\Users\用户名\AppData\Local\Microsoft\WindowsApps\` 在这个文件夹下查找以 `ubuntu` 开头的执行文件。例如，文件名可能是 `ubuntu2004.exe`、`ubuntu1804.exe` 或其他类似名称。

<mark>Tip 2</mark>

!!! warning "报错：NAT模式下的WSL不支持localhost代理"
	可以禁用windows代理：
	
	1. **打开 Windows 设置** 按 `Win + I` 打开设置。
	
	2. **网络和 Internet** 选择“网络和 Internet”。   
	
	3. **代理** 在左侧菜单中选择“代理”。
	
	4. **禁用代理** 确保“自动检测设置”和“使用代理服务器”都被禁用。

!!! tip "解决 localhost 代理问题的方法"
    在使用 WSL（Windows Subsystem for Linux）时，如果遇到 "检测到 localhost 代理配置，但未镜像到 WSL，NAT 模式下的 WSL 不支持 localhost 代理" 的错误，可以尝试以下解决方案：
    1. 配置 WSL 使用代理
    如果需要在 WSL 中使用代理，可以手动配置代理设置：
    export http_proxy="http://your_proxy:your_port"
    export https_proxy="http://your_proxy:your_port"
    export no_proxy="localhost,127.0.0.1"
    请将 `your_proxy` 和 `your_port` 替换为实际的代理服务器地址和端口。
    1. 升级到 WSL 2
    WSL 2 的网络堆栈与 WSL 1 不同，可能更适合处理网络代理问题：
    Step1. 检查当前 WSL 版本：`wsl -l -v`。
    Step2. 升级到 WSL 2：
    wsl --set-version <distribution_name> 2
    将 `<distribution_name>` 替换为您的发行版名称。
    2.1 将 WSL 2 设置为默认版本：
    wsl --set-default-version 2
    2.2 手动启动 SSH 服务
    如果只是尝试启动 SSH 服务，可以手动执行以下步骤：
    2.2.1 启动 WSL 终端。
    2.2.2 启动 SSH 服务：`sudo service ssh start`  


## 四、连接SSH的一般步骤

1. 在`WSL` 里启动SSH服务

   ```bash
   sudo service ssh start
   ```

2. 找到分配给WSL的IP

   ```bash
   hostname -I
   ```

3. 在Windows Powershell里连接WSL

   ```bash
   ssh your_username@WSL_IP_address
   ```
 
`ssh slowist@172.20.149.110`

## 五、如何在LINUX上运行汇编程序

- VS Code 安装 Remote Development 插件
- `/mnt/c/Users/leexi/AppData/Local/Programs/Microsoft\ VS\ Code/bin/code 1.asm`


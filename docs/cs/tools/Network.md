# 主机代理情况下的WSL 联网

1. 确认你的代理软件打开了Allow LAN（局域网连接），通常在【设置】标签页
2. 在WSL里：

```bash
cat /etc/resolv.conf | grep nameserver | awk '{print $2}'
```

得到主机和WSL通信的IP

3. 配代理：

```bash
export http_proxy="http://172.28.192.1:8888" 
export https_proxy="http://172.28.192.1:8888"
```

或者修改配置文件：

```bash
echo 'export http_proxy="http://172.28.192.1:8888"' >> ~/.bashrc 
echo 'export https_proxy="http://172.28.192.1:8888"' >> ~/.bashrc
source ~/.bashrc # 生效
```

一些常识：

1. ping 的通（例如google.com）但是没办法curl/wget 是因为ping走的是ICMP，而curl/wget 是HTTPS协议。所以还是得通过配代理。


之前有一些乱七八糟设置的话可以用一下工具，https://github.com/sakai135/wsl-vpnkit 。他好像会卡在ipv6，此时试一下ping google.com 或者 ping baidu.com 可能已经通了，按照 https://learn.microsoft.com/en-us/windows/wsl/troubleshooting#wsl-has-no-network-connectivity-once-connected-to-a-vpn 操作。


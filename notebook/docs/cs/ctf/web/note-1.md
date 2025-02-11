# Web 基础

!!! abstract
    第一部分笔记，有点零散ww

https://cubicy.icu

客户端：（跳转、点击逻辑）


服务端：（登录，认真）
多服务器：分布式系统


认证：证明你是你
鉴权：知道你的身份之后，是否有权限访问

DNS系统，将域名→IP

OSI

1物理层：电线、电波；进行一些冗余的编码/纠错
2数据链路：网卡，处理冲突/静默
//物理层

3网络层：IP 子网运行、分组传输、路由选择 //主机到主机，数据包寻址（快递公司）
4传输层：TCP 包裹分拣，数据包是给谁的 //应用到应用，或者说端到端（菜鸟驿站）

5会话层/表示层/应用层
//应用层

![](image/Pasted%20image%2020240703142957.png)

TCP与UDP

传输层：端对端（数据不会混淆）
TCP：无边界的字节流
只传输字符本身，开头结尾都由应用层来决定（规定特殊开头和结尾）//黏包
Buffer里攒够发，recv/send 不是一一对应

UDP：无连接的数据包，来一个发一个，接受buffer满了，直接丢掉（比较自由）

IP协议

DNS记录
A记录：IPv4
AAAA记录：IPv6
CNAME记录：别名，指向另一个域名

### `nslookup` 命令：

#### 基本使用：

1. 如果什么都不加：默认交互模式

命令示例：

```bash
PS C:\Users\leexi> nslookup
默认服务器:  dns1.zju.edu.cn
Address:  10.10.0.21

>
> cc98.org
服务器:  dns1.zju.edu.cn
Address:  10.10.0.21

非权威应答:
名称:    cc98.org
Address:  10.10.98.98

> www.baidu.com
服务器:  dns1.zju.edu.cn
Address:  10.10.0.21

非权威应答:
名称:    www.a.shifen.com
Addresses:  2409:8c20:6:1135:0:ff:b027:210c
          2409:8c20:6:1d55:0:ff:b09c:7d77
          36.155.132.3
          36.155.132.76
Aliases:  www.baidu.com

```

2. **非权威应答**：缓存，一个电脑上不可能存这么多域名，

- 缓存有什么问题：可能缺乏时效性，cc98的IP地址突然变了，可能就会返回错误结果

3. 真正（所谓权威）的流程：
以`www.cc98.org` 为例，完整而言是`www.cc98.org.`
先查找根域名是`org.`的服务器，再挑一个问是`cc98.org`的服务器

#### 可以指定使用类型：

##### `nslookup -qt=A` A类型

返回的就是地址

```bash
PS D:\MyRepository\zjuers-slowist-version> nslookup -qt=A www.cc98.org
服务器:  dns1.zju.edu.cn
Address:  10.10.0.21

非权威应答:
名称:    www.cc98.org
Address:  10.10.98.98
```

##### `nslookup -qt=NS` NameServer

可以一层一层地寻找根服务器对应的IP，进行询问

for e.g. 

第一层：`.`

```bash
PS C:\Users\leexi> nslookup -qt=NS .
服务器:  dns1.zju.edu.cn
Address:  10.10.0.21

非权威应答:
(root)  nameserver = d.root-servers.net
(root)  nameserver = i.root-servers.net
(root)  nameserver = g.root-servers.net
(root)  nameserver = k.root-servers.net
(root)  nameserver = f.root-servers.net
(root)  nameserver = e.root-servers.net
(root)  nameserver = l.root-servers.net
(root)  nameserver = c.root-servers.net
(root)  nameserver = j.root-servers.net
(root)  nameserver = m.root-servers.net
(root)  nameserver = a.root-servers.net
(root)  nameserver = b.root-servers.net
(root)  nameserver = h.root-servers.net

a.root-servers.net      internet address = 198.41.0.4
b.root-servers.net      internet address = 170.247.170.2
c.root-servers.net      internet address = 192.33.4.12
d.root-servers.net      internet address = 199.7.91.13
e.root-servers.net      internet address = 192.203.230.10
f.root-servers.net      internet address = 192.5.5.241
g.root-servers.net      internet address = 192.112.36.4
h.root-servers.net      internet address = 198.97.190.53
i.root-servers.net      internet address = 192.36.148.17
j.root-servers.net      internet address = 192.58.128.30
k.root-servers.net      internet address = 193.0.14.129
l.root-servers.net      internet address = 199.7.83.42
m.root-servers.net      internet address = 202.12.27.33
a.root-servers.net      AAAA IPv6 address = 2001:503:ba3e::2:30
b.root-servers.net      AAAA IPv6 address = 2801:1b8:10::b
```

接着，选择一台服务器，for .e.g. `198.41.0.4` 指定像这个服务器询问，哪台服务器掌管结尾是`.com`的服务器

```bash
PS C:\Users\leexi> nslookup -qt=NS com. 198.41.0.4
in-addr.arpa    nameserver = a.in-addr-servers.arpa
in-addr.arpa    nameserver = c.in-addr-servers.arpa
in-addr.arpa    nameserver = d.in-addr-servers.arpa
in-addr.arpa    nameserver = b.in-addr-servers.arpa
in-addr.arpa    nameserver = e.in-addr-servers.arpa
in-addr.arpa    nameserver = f.in-addr-servers.arpa
a.in-addr-servers.arpa  internet address = 199.180.182.53
b.in-addr-servers.arpa  internet address = 199.253.183.183
c.in-addr-servers.arpa  internet address = 196.216.169.10
d.in-addr-servers.arpa  internet address = 200.10.60.53
e.in-addr-servers.arpa  internet address = 203.119.86.101
f.in-addr-servers.arpa  internet address = 193.0.9.1
a.in-addr-servers.arpa  AAAA IPv6 address = 2620:37:e000::53
b.in-addr-servers.arpa  AAAA IPv6 address = 2001:500:87::87
c.in-addr-servers.arpa  AAAA IPv6 address = 2001:43f8:110::10
d.in-addr-servers.arpa  AAAA IPv6 address = 2001:13c7:7010::53
e.in-addr-servers.arpa  AAAA IPv6 address = 2001:dd8:6::101
f.in-addr-servers.arpa  AAAA IPv6 address = 2001:67c:e0::1
服务器:  UnKnown
Address:  198.41.0.4

com     nameserver = c.gtld-servers.net
com     nameserver = m.gtld-servers.net
com     nameserver = f.gtld-servers.net
com     nameserver = h.gtld-servers.net
com     nameserver = a.gtld-servers.net
com     nameserver = b.gtld-servers.net
com     nameserver = g.gtld-servers.net
com     nameserver = i.gtld-servers.net
com     nameserver = j.gtld-servers.net
com     nameserver = e.gtld-servers.net
com     nameserver = d.gtld-servers.net
com     nameserver = l.gtld-servers.net
com     nameserver = k.gtld-servers.net
a.gtld-servers.net      internet address = 192.5.6.30
b.gtld-servers.net      internet address = 192.33.14.30
c.gtld-servers.net      internet address = 192.26.92.30
d.gtld-servers.net      internet address = 192.31.80.30
e.gtld-servers.net      internet address = 192.12.94.30
f.gtld-servers.net      internet address = 192.35.51.30
g.gtld-servers.net      internet address = 192.42.93.30
h.gtld-servers.net      internet address = 192.54.112.30
i.gtld-servers.net      internet address = 192.43.172.30
j.gtld-servers.net      internet address = 192.48.79.30
k.gtld-servers.net      internet address = 192.52.178.30
l.gtld-servers.net      internet address = 192.41.162.30
m.gtld-servers.net      internet address = 192.55.83.30
a.gtld-servers.net      AAAA IPv6 address = 2001:503:a83e::2:30
b.gtld-servers.net      AAAA IPv6 address = 2001:503:231d::2:30
```

接着再问`baidu.com` …… 以此类推

##### `nslookup -qt=TXT`  DNS服务器里的txt

```bash
PS C:\Users\leexi> nslookup -qt=TXT cubicy.icu
服务器:  dns1.zju.edu.cn
Address:  10.10.0.21
非权威应答:
cubicy.icu      text =
        "google-site-verification=1fhjV2lfeA6mIocyby2UVcZ8bC8o8NpJreyw1OLPDUY"
cubicy.icu      text =
        "v=spf1 -all"
cubicy.icu      text =    "5aSx5oGL44K944Oz44Kw5rKi5bGx6IG044GE44GmCuazo+OBhOOBpuOBsOOBi+OCiuOBruengeOBr+OCguOBhgrmjajjgabjgZ/jgYTjgYvjgokK5b+Y44KM44Gf44GE44GL44KJCuOCguOBhiDlkJvjga7jgZPjgajjgarjgpPjgaYK5b+Y44KM44Gh44KD44GG44GL44KJ44GtICAKU1VLSVNVS0lTVUtJU1VLSVNVS0k="
cubicy.icu      nameserver = sam.ns.cloudflare.com
cubicy.icu      nameserver = itzel.ns.cloudflare.com
sam.ns.cloudflare.com   internet address = 173.245.59.141
sam.ns.cloudflare.com   internet address = 108.162.193.141
sam.ns.cloudflare.com   internet address = 172.64.33.141
```

其中 `google-site-verification=1fhjV2lfeA6mIocyby2UVcZ8bC8o8NpJreyw1OLPDUY` 是google用来鉴定的









```bash

PS C:\Users\leexi> nslookup -qt=TXT cubicy.icu
服务器:  dns1.zju.edu.cn
Address:  10.10.0.21

非权威应答:
cubicy.icu      text =

        "google-site-verification=1fhjV2lfeA6mIocyby2UVcZ8bC8o8NpJreyw1OLPDUY"
cubicy.icu      text =

        "v=spf1 -all"
cubicy.icu      text =

        "5aSx5oGL44K944Oz44Kw5rKi5bGx6IG044GE44GmCuazo+OBhOOBpuOBsOOBi+OCiuOBruengeOBr+OCguOBhgrmjajjgabjgZ/jgYTjgYvjgokK5b+Y44KM44Gf44GE44GL44KJCuOCguOBhiDlkJvjga7jgZPjgajjgarjgpPjgaYK5b+Y44KM44Gh44KD44GG44GL44KJ44GtICAKU1VLSVNVS0lTVUtJU1VLSVNVS0k="

icu     nameserver = b.nic.icu
icu     nameserver = a.nic.icu
icu     nameserver = c.nic.icu
icu     nameserver = d.nic.icu
d.nic.icu       internet address = 212.18.249.108
a.nic.icu       internet address = 194.169.218.108
b.nic.icu       internet address = 185.24.64.108
PS C:\Users\leexi>
```

`tracert`：

- 排除网络故障

`ttl:`

用完了，丢包

tracert 
- ttl设成1，第一个路由器会报告
- ttl->2
- ……

代理：

正向代理：
VPN：Virtual Private Network

反向代理：
隐藏真实IP，Cloudflare帮网站代发

CDN/防火墙

内网穿透

![](image/Pasted%20image%2020240703145634.png)

HTTP协议：(超文本传输协议)

1. 应用层的协议，基于TCP（http3，UDP+rules）
2. 封装
3. 无状态，前后的对话之间没有关系，需要应用层自行维护
4. 典型的方案:Cookie/Session/Token  Cookie：浏览器上；Session：服务器上；Token有标识，知道你处于什么上下文

Cookie Editor : 插件，查看cookie

Get请求：纯文本
?后面请求的参数

后端技术栈
Node.js PHP Python Ruby 

CTF 用逻辑漏洞欺骗后端

逻辑漏洞：if money!=0 then money-=price. What if money=-1 ?

if a == 1 写成 if a = 1

注入漏洞：混淆了数据和代码，把自己的恶意代码插入数据里

拼接代码非常危 

例如`printf("%d", _____)`

正常输入：`1` `2` `3`

恶意输入：`1); system("shutdown -s -t 0"); //`

就变成了`printf("%d", 1); system("shutdown -s -t 0"); //)`

爆了

### SQL 

php js sql //  html/css

MySQL

![](image/Pasted%20image%2020240703154359.png)

google :online compiler

![](image/Pasted%20image%2020240703154703.png)
一开始定义了一个表
 --类型在后面，primary key 主键，唯一，可以快速索引

```sql

-- create（
CREATE TABLE EMPLOYEE (
  empId INTEGER PRIMARY KEY,

  name TEXT NOT NULL,
  dept TEXT NOT NULL
);

-- insert
INSERT INTO EMPLOYEE VALUES (0001, 'Clark', 'Sales');
INSERT INTO EMPLOYEE VALUES (0002, 'Dave', 'Accounting');
INSERT INTO EMPLOYEE VALUES (0003, 'Ava', 'Sales');

-- fetch 
SELECT * FROM EMPLOYEE WHERE dept = 'Sales';
SELECT 1 As 'mynum';
```

Cookie 包含用户ID的Cookie到客户端
Session

Cookie：存储在客户端的小型文本文件，通常用于存储用户的偏好设置、身份验证信息等。

  - 示例：用户登录后，服务器发送一个包含用户ID的Cookie到客户端，客户端在后续请求中自动包含该Cookie，以便服务器识别用户。

  - Cookie劫持：攻击者通过XSS攻击或其他手段获取用户的Cookie，从而冒充用户身份。

Session：存储在服务器端的临时数据存储区域，通常用于存储用户的会话状态信息。

 - 示例：用户登录后，服务器创建一个Session，并将Session ID通过Cookie发送给客户端。客户端在后续请求中包含该Session ID，服务器根据Session ID查找对应的Session数据。

- 如果服务器被攻破，Session中就可能有一些敏感信息。

逻辑漏洞

a\==1&&a\==2

![](image/Pasted%20image%2020240703160310.png)

html：网页的骨架，嵌套
css：样式

区分：
	名字不一样，div/hr
	class="？"
```css
body{ //整个网页
	font-family:Arial,sans-serif;//字体
	margin
	padding
	background-color=###f4f4f4;
}
```

nav ul{

}
.intro{ //所有有class的都可以

}

JavaScript 交互

TypeScript（加强类型）

强大的类型系统


node.js 不需要去浏览器，可以有自己的开发环境


同源策略限制：

请求：同源，e.g.https://   |    /域名

跨域：加一个 /api/ 进行转发

### Lab : 使用BurpSuite 进行抓包


[Burpsuite实现抓包（http、https）\_burpsuite抓包本地请求-CSDN博客](https://blog.csdn.net/2302_77482152/article/details/136348964?ops_request_misc=&request_id=&biz_id=102&utm_term=怎么用BurpSuite对登录抓包&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-1-136348964.142^v100^pc_search_result_base8&spm=1018.2226.3001.4187)    


我想抓取的是学在浙大，是https  
1. 先按照http设置代理, 因为我的电脑已经连了VPN,端口被占了，所以需要修改端口的设置.  
- **解决方法**  
    1. 配置 Burp Suite 使用其他地址  
    你可以配置Burp Suite使用你机器上的其他IP地址。步骤如下：  
    打开 Burp Suite。 
    进入 **Proxy** 标签，然后选择 P**roxy Settings** 子标签。  
    在 **Proxy Listeners** 部分，点击 **Add** 按钮。  
    在弹出的对话框中，将 **Bind to port** 设为你需要的端口（例如 8081），将 **Bind to address** 设置为 `All interfaces` 或你机器的具体IP地址。  
    点击 **OK**。  
    2. 配置浏览器使用新地址和端口  
    打开你使用的浏览器（例如 Chrome）。  
    进入代理设置，根据你的操作系统设置代理：  
    **Windows**:  
    1. 打开设置，搜索并选择 **网络和Internet 选项**。  
    2. 在 **代理服务器** 部分，填写你在Burp Suite中设置的IP地址和端口（例如：192.168.1.100:8081）。  
    3. 确认代理链配置  
    如果你通过另一个代理服务器访问外部网络，需要在Burp Suite中配置该代理：  
    在 Burp Suite 中，进入 **Network** 标签，然后选择 **Connections** 子标签。  
    在 **Outgoing proxy servers** 部分，点击 **Add**。  
    配置你的上游代理服务器信息（IP地址、端口、认证等），并点击 **OK**。  
    4. 测试连接  
    配置完成后，确保浏览器和Burp Suite都能正确连接并进行抓包。可以访问一个简单的网页进行测试，查看Burp Suite的HTTP history是否有记录。
2. 启动代理服务器，关闭拦截  
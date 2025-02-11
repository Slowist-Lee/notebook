
## 1 Task 1

### 1.1 权威域名服务器

使用`nslookup` 查询 `cubicy.icu` 的服务器:

- 先查询`.`

```bash
PS C:\Users\leexi> nslookup -qt=NS .
服务器:  dns1.zju.edu.cn
Address:  10.10.0.21

非权威应答:
(root)  nameserver = m.root-servers.net
(root)  nameserver = b.root-servers.net
(root)  nameserver = j.root-servers.net
(root)  nameserver = a.root-servers.net
(root)  nameserver = k.root-servers.net
(root)  nameserver = i.root-servers.net
(root)  nameserver = c.root-servers.net
(root)  nameserver = h.root-servers.net
(root)  nameserver = d.root-servers.net
(root)  nameserver = f.root-servers.net
(root)  nameserver = g.root-servers.net
(root)  nameserver = l.root-servers.net
(root)  nameserver = e.root-servers.net

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

- 再指定其中一台服务器，查询`icu.`

```bash
PS C:\Users\leexi> nslookup -qt=NS icu. 198.41.0.4
in-addr.arpa    nameserver = b.in-addr-servers.arpa
in-addr.arpa    nameserver = a.in-addr-servers.arpa
in-addr.arpa    nameserver = c.in-addr-servers.arpa
in-addr.arpa    nameserver = e.in-addr-servers.arpa
in-addr.arpa    nameserver = d.in-addr-servers.arpa
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

icu     nameserver = c.nic.icu
icu     nameserver = a.nic.icu
icu     nameserver = d.nic.icu
icu     nameserver = b.nic.icu
a.nic.icu       internet address = 194.169.218.108
b.nic.icu       internet address = 185.24.64.108
c.nic.icu       internet address = 212.18.248.108
d.nic.icu       internet address = 212.18.249.108
a.nic.icu       AAAA IPv6 address = 2001:67c:13cc::1:108
b.nic.icu       AAAA IPv6 address = 2a04:2b00:13cc::1:108
c.nic.icu       AAAA IPv6 address = 2a04:2b00:13ee::108
d.nic.icu       AAAA IPv6 address = 2a04:2b00:13ff::108
```

最后指定`cubicy.icu`

```bash
PS C:\Users\leexi> nslookup -qt=NS cubicy.icu 194.169.218.108
服务器:  UnKnown
Address:  194.169.218.108
cubicy.icu      nameserver = sam.ns.cloudflare.com
cubicy.icu      nameserver = itzel.ns.cloudflare.com
PS C:\Users\leexi>
```

所以查询到权威DNS是`194.169.218.108`

### 1.2 查询IP地址

使用`nslookup` 命令

```bash
PS C:\Users\leexi> nslookup cubicy.icu
服务器:  dns1.zju.edu.cn
Address:  10.10.0.21

非权威应答:
名称:    cubicy.icu
Addresses:  2606:4700:3033::ac43:b3f4
          2606:4700:3033::6815:1fce
          172.67.179.244
          104.21.31.206
```

因此IP是 `104.21.31.206` & `172.67.179.244`
### 1.3 查询DNS A 记录

使用`nslookup -qt=A`命令

```bash
PS C:\Users\leexi> nslookup -qt=A cubicy.icu
服务器:  dns1.zju.edu.cn
Address:  10.10.0.21
非权威应答:
名称:    cubicy.icu
Addresses:  104.21.31.206
          172.67.179.244
```

响应有 `104.21.31.206` & `172.67.179.244`

不同IP 地址的好处：
- 可以分担服务器负荷
- 假设其中一个服务器出现故障，可以使用另一个服务器，这样就不会使得网站崩溃

### 1.4 隐藏的文本

```bash
PS C:\Users\leexi> nslookup -qt=TXT cubicy.icu
服务器:  dns1.zju.edu.cn
Address:  10.10.0.21

非权威应答:
cubicy.icu      text =
"5aSx5oGL44K944Oz44Kw5rKi5bGx6IG044GE44GmCuazo+OBhOOBpuOBsOOBi+OCiuOBruengeOBr+OCguOBhgrmjajjgabjgZ/jgYTjgYvjgokK5b+Y44KM44Gf44GE44GL44KJCuOCguOBhiDlkJvjga7jgZPjgajjgarjgpPjgaYK5b+Y44KM44Gh44KD44GG44GL44KJ44GtICAKU1VLSVNVS0lTVUtJU1VLSVNVS0k="
cubicy.icu      text =

        "v=spf1 -all"
cubicy.icu      text =

        "google-site-verification=1fhjV2lfeA6mIocyby2UVcZ8bC8o8NpJreyw1OLPDUY"

cubicy.icu      nameserver = sam.ns.cloudflare.com
cubicy.icu      nameserver = itzel.ns.cloudflare.com
sam.ns.cloudflare.com   internet address = 173.245.59.141
sam.ns.cloudflare.com   internet address = 108.162.193.141
sam.ns.cloudflare.com   internet address = 172.64.33.141
```

所以文本是：`5aSx5oGL44K944Oz44Kw5rKi5bGx6IG044GE44GmCuazo+OBhOOBpuOBsOOBi+OCiuOBruengeOBr+OCguOBhgrmjajjgabjgZ/jgYTjgYvjgokK5b+Y44KM44Gf44GE44GL44KJCuOCguOBhiDlkJvjga7jgZPjgajjgarjgpPjgaYK5b+Y44KM44Gh44KD44GG44GL44KJ44GtICAKU1VLSVNVS0lTVUtJU1VLSVNVS0k=`

扔进Cyberchef进行`Base64`解密，得到的文本是：

```
失恋ソング沢山聴いて
泣いてばかりの私はもう
捨てたいから
忘れたいから
もう 君のことなんて
忘れちゃうからね  
SUKISUKISUKISUKISUKI
```

### 1.5 查询 IP (IPv4)

通过`nslookup`依次查询`cubicy.icu` `www.cubicy.icu` `blog.cubicy.icu`的IP地址

```bash
PS C:\Users\leexi> nslookup cubicy.icu
服务器:  UnKnown
Address:  fe80::c2b4:7dff:fe97:80d3

非权威应答:
名称:    cubicy.icu
Addresses:  2606:4700:3033::ac43:b3f4
          2606:4700:3033::6815:1fce
          104.21.31.206
          172.67.179.244

PS C:\Users\leexi> nslookup www.cubicy.icu
服务器:  UnKnown
Address:  fe80::c2b4:7dff:fe97:80d3

非权威应答:
名称:    www.cubicy.icu
Addresses:  2606:4700:3033::6815:1fce
          2606:4700:3033::ac43:b3f4
          104.21.31.206
          172.67.179.244

PS C:\Users\leexi> nslookup blog.cubicy.icu
服务器:  UnKnown
Address:  fe80::c2b4:7dff:fe97:80d3

非权威应答:
名称:    blog.cubicy.icu
Addresses:  2606:4700:3033::6815:1fce
          2606:4700:3033::ac43:b3f4
          172.67.179.244
          104.21.31.206
```

说明他们的IP地址都是`172.67.179.244 & 104.21.31.206`

### 访问服务器

1. 直接访问：失败了。
2. 哪种服务：`CDN`

核实: 使用`nslookup -type=CNAME`:

```bash
PS C:\Users\leexi> nslookup -type=CNAME cubicy.icu
服务器:  UnKnown
Address:  fe80::c2b4:7dff:fe97:80d3

cubicy.icu
        primary name server = itzel.ns.cloudflare.com
        responsible mail addr = dns.cloudflare.com
        serial  = 2345512884
        refresh = 10000 (2 hours 46 mins 40 secs)
        retry   = 2400 (40 mins)
        expire  = 604800 (7 days)
        default TTL = 1800 (30 mins)
```

接着使用一下CDNPlanet:  [https://www.cdnplanet.com/tools/cdnfinder/](https://www.cdnplanet.com/tools/cdnfinder/)
![](image/Pasted%20image%2020240718003632.png)

## Task 2

### 2.1 报文：

使用 BurpSuite 对[学在浙大](https://courses.zju.edu.cn/)的登录过程进行抓包 ，最关键的HTTP请求应该是：

```
POST /cas/login?service=https%3A%2F%2Fidentity.zju.edu.cn%2Fauth%2Frealms%2Fzju%2Fbroker%2Fcas-client%2Fendpoint?state%3DvrrbjUz1MwQIGPJX3popmm-ZA402VVkwzfh-EwEQf8U.CYqmWq1Mmjo.TronClass HTTP/1.1
Host: zjuam.zju.edu.cn
Cookie: JSESSIONID=60D04A28237C8F0EED420B1099A5EBD7.cas16; _pf0=mz6SazkJNbcw2iwdpGXvl2IIkDk4nIkv0ZEFQMneIB8%3D; _ga=GA1.3.360544648.1721227648; _csrf=S8mwplVi9KWoF2WQ0TlCeGjdL%2FYXNwL8j2MIDa0x7f4%3D; _pv0=eR%2FyPB0WsMTHUztw7P3%2BlYKZkUbHna6slTwgYbb75gdImhdu%2FmOWuTtnqSAYsKmagzvpJfjO6ySlgIA0k4xdCQzClvvWVBqArX9jlIAO8LNygVplCmmGe7HHb58hLYyAR9i4cv8jh1Awo%2BHZybdHi4XMjc1LouCmLThCn5NMlnOsQsUg2q%2FfbLmOK0vxIuNI%2FqslzG%2FqtVAAmJ2Rs3XRpKXoKhwqZvMXMri9ZRWCGWWl0QYTbAp08%2F%2B%2BCfauzlBFLwr8%2BfIq7GSNOn1YCMTpBdov0KRcRr2UiUDjGSw0f3Pdtcb%2FTzKXkYMGwFg%2Br6f8m0cko1EYGIsf%2BLxeT%2BJRrEx485oVGMFDifuJfgj4U7tL5rmb0x1ZjVONFw0Gjc8LwtiIaDrTMTKGq%2FYPKNN9wZ2%2BKvVmYOWXW8%2F7rJuVSvA%3D
Content-Length: 7359
Cache-Control: max-age=0
Sec-Ch-Ua: "Not/A)Brand";v="8", "Chromium";v="126"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: zh-CN
Upgrade-Insecure-Requests: 1
Origin: https://zjuam.zju.edu.cn
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://zjuam.zju.edu.cn/cas/login?service=https%3A%2F%2Fidentity.zju.edu.cn%2Fauth%2Frealms%2Fzju%2Fbroker%2Fcas-client%2Fendpoint?state%3DvrrbjUz1MwQIGPJX3popmm-ZA402VVkwzfh-EwEQf8U.CYqmWq1Mmjo.TronClass
Accept-Encoding: gzip, deflate, br
Priority: u=0, i
Connection: keep-alive

username=3230103034&password=4befe58f7a5945b1f28364900c74da80906304f37a188ad6c0934f381ebb6b933050ead16c2fd5fbc48f3e030b9514856a6086f3eda288592fe40fe172e97d0c&authcode=&execution=8247e21d-9866-472d-8c4b-e700d301c8e4_ZXlKaGJHY2lPaUpJVXpVeE1pSjkuYzBOMU9UUklkVmMxZUd4RFIxRlRVa1pZUkZCbk1rOW1kamQ2VEdsa2EzUmxSVEZwWkZwUGJFaGhSMXA2YVVSRFJIQlRXVXRyVkRCQ1MxVXlXazF2U3psS1lVSkViRTg1Y2l0eGQxRkxjMUZqV0hZMk1FWlhSMG81ZEhreFkxaG9ja2huWkc5RGJXOWxkbXRwYUVKVFluRmFWWGw2YTI1WGVtb3JiRE5QUVU5SmJucGtWVWRGYjNSYU5XTkRXbWN3VjI4NU1GVjNNVmhzVEhCUlJsQldUVFoxVm1oVldrSjRMMXA1Y25wcU5UbDJabTF1ZDBRclJXUjBVbFJIYVhSNmFrZE9lU3REY1hkVlpVMDBabGxNY0Rrdk1XOTJhMnBNU0VsNlVYUk1kVGh4Y1N0NlR6bGlTVUpFWnpWTGExUXdjVkJXY21KSWVqZFJjbVJzTWxsUVpFRXlUVEJFYmtKS1dsVkRMMVJKTVVGSmNIUk5iVzFZU0hOMlkwTlNVVkJsV1ZoTGVVVlRTWE0zV1VrclRFazNiVWRrVlV4Q1FrRk1hM3AwVEVsa09YbHZWQ3RKY0Vod2RuQldSVzVsTkVFNGRVMXhiRFZwYUc0dmIyOWtaRVpEYUhwa2Rua3hTRU5XYlhoTFdFVXdabWxDU1RSNE4yRXlZamRoTW5SUWFGbGtUbTh2YTNZeFVuTk9OM1pUVGxOM09IZEZRMVZIVGprMFZVNTFlWE5hZWtadlNqbDFNV1pxZDJsc1VtTkRMMlJzWjNKTldIbEZVSEJ1T1VGaE4ySkdPSFk0ZW1wTFMzQXZhMEk1YTFkNVJFWkxlbUpsTjJKVGRqUkthbWhqVjBWcFRqaFBhSFUxSzNkR1FuVkJTVXhSTHpNNVVpczFUVmMxT0U4ck5sUTJjMVJRVldwU1J6YzJibGROZDA5QmFrdGpUV1ZYTkZoNVJtVXpiME5aTjNRdk5IcG5hamxWS3poR1lYZ3hjSFpDWkd0bGJGUnVOSEZYVXl0Vk9GQndTVEkyUm5sNlRXRnVZVWhUV1RRM1UxQkdNa3dyZG1FMlRYTnBLMUpYTkV0S1RYUnJVVmxEY1dwa2MxRXhNbkZrTjJGYWJXOXJkMjVsY1hZMVJYbGthVk5JUkhVMmIwMU5iakZxV1haalozbEJha1pMVEVwUGIyMXFhMHg2TDJkTVoxcFFVMDlxY0dsVlYzQlNXV2xxYW5CV1VWQk9ORkJVTmtSdFJpOVdkR2R3YkVseWJVVlFXRXN5T0dWT2RYQkxiRlJaYnpoVUwzWTNibkIxTUZGVFVHaFplbTB2V1RoaVRFbG5jbTVKZURacVlWcE9XU3RzU0VOTVlqaGlWbkJaUlRCeE1VSTVObWRVTW1vNGREZHVZM1JoVm5sa1oyeHhORkZ5Umpka1NHcDJjREZzTkhVeVEzQmplV3hLTnpSNWIydE5OMVpWTjFka05YUTBWekl5YjBOUk5HZDZTMFZ6ZUZFMU9HNTRkM1V6Ym5GMmNEZHNiMEpaVEdoclRHMXdiREl2V1hNNVNISnRNMGxFWVVwMmRYRXJNVzlPUVRWU1VrVmFkSEJoVnpsQmNHUldkRlZ6TURSSWFTOTJhbU0wU1RGTWRFRXpXRWd2TjBOUVZUUnJZMFZRVWtscE5VWnBNM3BZU1RKeVIwcFJkVUp4VTBaVU5VNU1NWGhyVDFaTlQzcFpUMnR4ZUhKM1NsQm1RbEpYVGtkR1UwVXdVazl6V20xNGFWTXhNMGwxWjJSbGVVdFhjbEkzVVhKbk5VUjRaMnd6YkdwblJGcFllRVJyWlhFNFExcHVTbGhFVFZwQ2NHNXhlWEZQYW14QlNWcExRVUUzU2tKSlFUWnBVV3B6UlROamNVOVRWMXBzV2xaSFRrWjVka3RwTld4amJrWlJNVWwyWTBneGJVcHpNMEZ5V1N0YWR6UlNTR2xOUldFMmJqZG9lR1YwWW1aeWVtdFdXVlkxVEhKbWVETlBMM1ZUWVVsTE9GaE5hM0pYT0dGQmNuRTRVaXR3TmpWQ1dVSnZhVlp5TWxJNU5GQlVOMU55VFZBNVJFNXlXa1ZKYzNwRVJuQklUeTlTWlN0bFRXd3pVV3c0UTIxdFZ5OXdkbWR4VTJORmVVZDFTMkpXU25aaFR6azRRV2RXY0dwb1dtTTFUWEZLV0hkUWVrNUVTRE4wVnpod2NFNXRRa2RZWTFjeVdreERaRmhaYUM5eWJUaDBaSEJIWjBGNE5qZGpURnBuUVdoUFJUUnBiV2xZWlhGc1dHc3ZUbk5DVVV3eVRVTkhNbXhETWpGamRuWnhLMFJIUm5wQlQwNUNNMmh3ZDJoeFRsazFXbG81ZFVwU05ITkZlV0ZuYWpsTFlsSnZNV1J6VGtOWVlVRldUbkIyZFZaWVpGZEZZeXRFYTJ0MlJsVkxTbHBHU1ZobWNtMDNjV3BVU0hKMWNEVkpjSHB6TVdwUFFVWldlRkYwZDJWVVIzcE1hek5DZGxGSU9XUnFiWGRMVDFjM1lpOUlaMFJxWVhGa1RqZEdRVFZuTVhJeVRteERRM2Q1TDBWTFpsVnphVFZHVjBGTWVIQkNiMmRtZG14QldERkVWbVpwTWtnNFRUbEZUVUpxYlhOalNVcGxSVUl4WmpSUVZXWTBNSGRoZVdvek1HMW9kbEY0YTFsaVFqRkhWbUpYZEdWNWFucHVOV1ZMYXpOc1RHSm5URFU1VGxKM2VXNWlkMkpqYkdjcmJWWmxZVzlhV1VKd2EycFFZMWRhZVhWblQzWnliR2x0UzNsRVFrSlNVMW8xZUdJek5HaE1OU3NyVUhaRFdqRnZWR1pVTlRRd2NsSm1ORWM1WTJkTGVVaEdlV3d6Y21kaFluVjJibU5SVEROWVkxTXpZemhQT0hWUGVEa3dTa1JXYkhKTmNFeEhhV1JaZVVVeFVGVk5VMnRHTUZaeFUwVmhWRXgyYzJOM2JuaEpTa0YyYlZoUGVFZEpSWFZyVmpKcVFqTk9RbFpTWVhCbVNIbHdVeXN4WlUxSU1rb3pOSGgyV2tGV1pWVlBaMkZhUlhOcVNrb3JaWFIzVlZWU09IaHJVbTVpVlV3M2VFZGpiRFJKZVU1VFJXTnJkV0p2YkVkd01GQXpTMmcxT1haNWVEVTJjVEpHTWt0V1pVVmpXbFkwY0hKbU5IUmhWR2wyWkRWRFQza3ZZVEZIVVhWMGFsVXJaa2M1VEhJeVRXMW5LM3BzVVRSbkszaHVPRWRFVWxKVk1EQlhVSHBvTjNoNVMyWjVhbFlyVGtwc2VrTkZheTg1V1VKQ2VXTlZRa05hU0c1aFZIZE1jVVoxUkU4NWVXaDNaMlYyWm1oSlZ6SlVOREZuWldGNGVVMDVSMDAxZFZkWlRITkxTbk5JWTFKNFZ5OTNLelp1YTFWUmVHZFhhMUJzYXk5TU4zUlJRVWRIUTA1QmFuUnVhRmh0Ymt0M1dFOUtOMDlsU2pGbVRHeDBjamsxZFhZcmNYaFNlSGxCVVVjclprY3hXbXg2Y0ZGSWJsUkRiMGQwTkdaTmJGTTJUVzlKY3pKNU5GZDFiaTlKVDA4M1duSTBiWGhJWWxSU1JqbHpRMFI1ZUc1ek1FUlFjMHcwWm14TU1sUnRaak5aVkZscFUxRnRVVzFxV1dkV1dYRkdkbk52WXpONFZrazROV0oyTjBGMGNURjJSbGRhY21Gdk1qRkRNeTh3YjA1MWQwWTFWMnhDWTFoRWR6RklSSGRRVjNWd04waFBjRGN3VTJSalFVWmxaRzV5YlRsWk1VTXJlVTFEZUZGRVprOWpRMlpuY0V0SmFFNDJkMlZQUTBGWU1VVk5NbkJIUTJscFFtMDJRMk1yTjNFMlZWaHpUVGRSYzNnemEyaGtSM3BrUVc1MlJVVklhbkl5VkZSa1NGUkdNbEU0ZWtobE1pOUdhR2xxWkVaclIzaHVUa3hZT0RObVdqRk1UMDVqVTJKM2RDODNlVEExTVVkQ1RIUmhhVXBWVnpsYWRVZHZWR0YxVEdSaFpITmpRVTFUU0VWYU1GWnBOell2WjJ4M1JqRjBVV2x4VlZOUmVEbHlORGszUlRjM1l6RmpPWGxTZGtsMmJrcFZhRGhZZFVwYVdHMHZPWFJEY2t4MlNHY3lVVFpCZWxsck1YWXliSFJLYzNsclZEZHhNMnhEWTJ4V00yUkJOazUwYWtWU1JUUktNbTVDYm1OYU5VOUNUMGxpVlZkVE9TOHdTMnRhTmpKbGFrdGlURE55UmpWRlRsQk1kbGswYkV0S2NIWTNhV05QTjJSd1RVaFRURTloVjJwM1NqTkxiRWwyYWxObVlXbExaMjFzTWxWVWEwWnBTWEpLZFRNd1ZITXZLM2xJUTFKb1FqUTVaM1ZWVmpCMFFWQmhNV1ZNWjJoaGVtTlZRMU5KVVd4d2RqWkpVMVprUW1Fd1pGQmtWMVJJUkV0d01tOVRSeXRvVEhsUVNDdGlLM0V4ZUhvdlNXMWxWRXBIWTNVMmVXbFBMelJzZDJFNFVFOU1OV0pVUkVreU0wZDJZVEZCUld0UFRDc3hjblJoVkdsWU5uRTBWMDVIVkRRNGRFSjRZMjFMVWxwMlprTnphMVUyU0dGbWNHbFRTRlZJVmpkdlQyNXFLMlZyTW0xV09TOWtWWFV5U1djNVltWnlNU3REVmtSR2NHZEZUbGszWjJ4eVRUVlZka05QTkVJdllYTnZMMXBQZUdjeFNHeE5aa2xIYTA1MU9IVkJVWEp6WkdsSlVGSnpiak5DYld0aE9VRTFhRGR4YTBGaVYya3JkelJTS3psTWRXMDBSalZNU1VvdmFFbEtiRE1yY0U0M1RWWnJiMUYyTldRMmJEUmpZWGxDZUc1U1puZ3pNVVZHVFV4V1pWaG9hVzVWVlVaelVIbHVZMkpyYmtvM09XSjVVM2hIZUhwSVFuVlllR1ozUTFSMlRuaDZTR1kxVW5KRmVqVkdVMHRoZGpSUU9HVTBVVVpuU210dGFrWkZWeTlhVDJsbmVteDViV05uYlhOdE5VTkpUM0JKUnpKSVRsWkZlVnBKTWpoMmRrZ3lka0ZQVG1KSlJubFdPRmxCYzFWUVExQmphV3B4TW1acWVtMTNMMDE0TjNwcFRtaDNla1pRY0ZGTFZFSjRkbGhTTUdsVldGbExlVkJVVlZSamRESkdSR2syUTNoQlpXa3dURTVCTVRFMFIzVjBZWHBUZUhkSFkwOXlXbEF4VVhJeFREZHBibVV3U25kQ1VUWk5kakpNWjJzMlVXUkZOSGhhZFU5bU5rMUlVVmRUU1RsUFdsVnlkbkowYjBNMWREZDNaV3hFTjBsSFZHaGpjV3B5VVhjNVJtNVVSMUp0WlVwMFkwaG9MMVZ1ZVhkcGRUVXdWMGxxU1daUGNVTnRRbFV3TDBwdmVrTkpjSEZNWlc0eE0zaE5lVWM1UW14MmVYbDFhVFV4YzBzMU9FSkVla2NyYzJVeWIzaG9WamRWTnpSRldXd3JiMUpCUVVsU09XZDVLMWhOYmtWemJ6bEdPV3RhY2tSUVpXVkZaV0ZVYTFNeWVtMWhlRTVOTlVKd1V6QnlXbmhxUVV0MVlVbEVNWFE1Um05MFNFd3pabVJ2UVc5U2NDczVVbXRLWlRsRWNGaEhTMnAzYjFRMlIyNWlkRnBvVVVSMGREZEdUbVpTTkVoWlNtdDZiM1F3YmpOcVNWcExWMUZJVVhkVWFHdEJWbEpOYldkUmFXUkpjVllyTVVGRFQwZG5TaXN2U2swd04wMW1XV3BWY0ZkWFdURm5RaTlWTDBaSlMwcFROWGhWYVdneU5GQkRRWFZwUzJaUmVFaFdUaXRIYmtaNE0xcFlXVTVJTUZvdmFFbE1WVlZQVW5ZM2JYZEhUVEkwYzNZNVkxRXhkelo1U21SbE4xbGljamMxTkhoUU1XdEZaWGRQWml0NWNsVXdSRlpQUzFsWk5XRXJiMjVJVDBJNVdrUmxNRXMxYVRsVU55dHpXVUl2VkROck9ITjViMmRHVkhFd2FFSllibk5oSzNoeFluSmFNMkpyYW5sUlpIZHNRblJ4T0hOUVZXdDBObXQxVTFWTFdYbFBNbWwwYnpCYU5sSXZNMnhSZUdvM1YxQTBOMGRUUzJONFkzUlFZa3Q2U25kSk1WWnBSMHBpU1d3eWJtZHFZVzFtZGtjek1FUXlMelJDUkUxcFIxRmlLeXRJU1hWRlRuZzJMMlZIWkc1elZEZE1NMU5rTTI5cmFWWkhhbVY2U0dWSk5ISjNTVGR1WW5wdlRVRllNRlZLWVZwcFlsZFdLMGM0TVhWM1lVVkhSVkZoYmxSU01HTnVSM2RHWTA1RldDdDJTa3hQTTFCdFNGTnJOa1JYWlV0VWJtMXVjMlZpYzJKSldIcERRVmx1TlVscVQyVnBVRTl5TXpSbk5qVlFiR1EwVFRWT1NVTndUbk01UkZOUVRXSmhaVUpFUkZoWFQyeEdOR1Y0UjFaUWNUZHZkMUJvTlVKaVVsQkxZakJsV0ZKMldsZFFWRE5YUjJkNmRrMHJkREpzZW5SYVJXRlVOSFZXU25Fd01WQm1kWFJDYkRGSFFtdHNNMEp2ZEd0WmMyeHpiRkJOZFdJeU4xcHNLM1ZLUVRjd2NYUnJNR3N4Y2xsaGEySnZTRlo2ZFhWSFQwTXpjMjlqTVhFdlRYRktjRVpPY1RRMFNYRkRkUzg1YW1ZMlRWSjJZemhCVEdkWmVtNHpRbk54V0U0M1lXTlFiM1UxWlRGUFpHbHlkRGxMUkZSR01WTm1XQzk0VkRkeFZ6TTNSWFZ4U0d4bmFUYzBUek0zYVZaa1kxZFBVRkJSVTA5VWRqZHFZVFJsV2xGNGNsZFZNbEpQTUZFeVlXSjBkblU0YjBaa1RHTjRXalZ0VjJ4VVlpc3lOakJLTmxKcmJUWlZjbWM1VnpkUllqTm5PREUzTmpOM2RIQkpZV3BrUWl0a2FYZFBlRWg1UW1jOVBRLldER0VxZE4wWnlNZlp5S3QzcEdwd1FSX2xaSEM1dWpURTlsRF9wc25yZjVHeXc4M1JKZzdzTk1tMFl0c2xWTmNfREpDOEhidGEzYThTR0ljbFhLZHB3&_eventId=submit
```

对组成部分的分析如下：

### 请求行

```
POST /cas/login?service=https%3A%2F%2Fidentity.zju.edu.cn%2Fauth%2Frealms%2Fzju%2Fbroker%2Fcas-client%2Fendpoint?state%3DvrrbjUz1MwQIGPJX3popmm-ZA402VVkwzfh-EwEQf8U.CYqmWq1Mmjo.TronClass HTTP/1.1
```

### 请求头

```text
Host: zjuam.zju.edu.cn  
Cookie: JSESSIONID=60D04A28237C8F0EED420B1099A5EBD7.cas16; _pf0=mz6SazkJNbcw2iwdpGXvl2IIkDk4nIkv0ZEFQMneIB8%3D; _ga=GA1.3.360544648.1721227648; _csrf=S8mwplVi9KWoF2WQ0TlCeGjdL%2FYXNwL8j2MIDa0x7f4%3D; _pv0=eR%2FyPB0WsMTHUztw7P3%2BlYKZkUbHna6slTwgYbb75gdImhdu%2FmOWuTtnqSAYsKmagzvpJfjO6ySlgIA0k4xdCQzClvvWVBqArX9jlIAO8LNygVplCmmGe7HHb58hLYyAR9i4cv8jh1Awo%2BHZybdHi4XMjc1LouCmLThCn5NMlnOsQsUg2q%2FfbLmOK0vxIuNI%2FqslzG%2FqtVAAmJ2Rs3XRpKXoKhwqZvMXMri9ZRWCGWWl0QYTbAp08%2F%2B%2BCfauzlBFLwr8%2BfIq7GSNOn1YCMTpBdov0KRcRr2UiUDjGSw0f3Pdtcb%2FTzKXkYMGwFg%2Br6f8m0cko1EYGIsf%2BLxeT%2BJRrEx485oVGMFDifuJfgj4U7tL5rmb0x1ZjVONFw0Gjc8LwtiIaDrTMTKGq%2FYPKNN9wZ2%2BKvVmYOWXW8%2F7rJuVSvA%3D
Content-Length: 7359
Cache-Control: max-age=0
Sec-Ch-Ua: "Not/A)Brand";v="8", "Chromium";v="126"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: zh-CN
Upgrade-Insecure-Requests: 1
Origin: https://zjuam.zju.edu.cn
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://zjuam.zju.edu.cn/cas/login?service=https%3A%2F%2Fidentity.zju.edu.cn%2Fauth%2Frealms%2Fzju%2Fbroker%2Fcas-client%2Fendpoint?state%3DvrrbjUz1MwQIGPJX3popmm-ZA402VVkwzfh-EwEQf8U.CYqmWq1Mmjo.TronClass
Accept-Encoding: gzip, deflate, br
Priority: u=0, i
Connection: keep-alive

```

### 请求体

```
username=3230103034&password=4befe58f7a5945b1f28364900c74da80906304f37a188ad6c0934f381ebb6b933050ead16c2fd5fbc48f3e030b9514856a6086f3eda288592fe40fe172e97d0c&authcode=&execution=8247e21d-9866-472d-8c4b-e700d301c8e4_ZXlKaGJHY2lPaUpJVXpVeE1pSjkuYzBOMU9UUklkVmMxZUd4RFIxRlRVa1pZUkZCbk1rOW1kamQ2VEdsa2EzUmxSVEZwWkZwUGJFaGhSMXA2YVVSRFJIQlRXVXRyVkRCQ1MxVXlXazF2U3psS1lVSkViRTg1Y2l0eGQxRkxjMUZqV0hZMk1FWlhSMG81ZEhreFkxaG9ja2huWkc5RGJXOWxkbXRwYUVKVFluRmFWWGw2YTI1WGVtb3JiRE5QUVU5SmJucGtWVWRGYjNSYU5XTkRXbWN3VjI4NU1GVjNNVmhzVEhCUlJsQldUVFoxVm1oVldrSjRMMXA1Y25wcU5UbDJabTF1ZDBRclJXUjBVbFJIYVhSNmFrZE9lU3REY1hkVlpVMDBabGxNY0Rrdk1XOTJhMnBNU0VsNlVYUk1kVGh4Y1N0NlR6bGlTVUpFWnpWTGExUXdjVkJXY21KSWVqZFJjbVJzTWxsUVpFRXlUVEJFYmtKS1dsVkRMMVJKTVVGSmNIUk5iVzFZU0hOMlkwTlNVVkJsV1ZoTGVVVlRTWE0zV1VrclRFazNiVWRrVlV4Q1FrRk1hM3AwVEVsa09YbHZWQ3RKY0Vod2RuQldSVzVsTkVFNGRVMXhiRFZwYUc0dmIyOWtaRVpEYUhwa2Rua3hTRU5XYlhoTFdFVXdabWxDU1RSNE4yRXlZamRoTW5SUWFGbGtUbTh2YTNZeFVuTk9OM1pUVGxOM09IZEZRMVZIVGprMFZVNTFlWE5hZWtadlNqbDFNV1pxZDJsc1VtTkRMMlJzWjNKTldIbEZVSEJ1T1VGaE4ySkdPSFk0ZW1wTFMzQXZhMEk1YTFkNVJFWkxlbUpsTjJKVGRqUkthbWhqVjBWcFRqaFBhSFUxSzNkR1FuVkJTVXhSTHpNNVVpczFUVmMxT0U4ck5sUTJjMVJRVldwU1J6YzJibGROZDA5QmFrdGpUV1ZYTkZoNVJtVXpiME5aTjNRdk5IcG5hamxWS3poR1lYZ3hjSFpDWkd0bGJGUnVOSEZYVXl0Vk9GQndTVEkyUm5sNlRXRnVZVWhUV1RRM1UxQkdNa3dyZG1FMlRYTnBLMUpYTkV0S1RYUnJVVmxEY1dwa2MxRXhNbkZrTjJGYWJXOXJkMjVsY1hZMVJYbGthVk5JUkhVMmIwMU5iakZxV1haalozbEJha1pMVEVwUGIyMXFhMHg2TDJkTVoxcFFVMDlxY0dsVlYzQlNXV2xxYW5CV1VWQk9ORkJVTmtSdFJpOVdkR2R3YkVseWJVVlFXRXN5T0dWT2RYQkxiRlJaYnpoVUwzWTNibkIxTUZGVFVHaFplbTB2V1RoaVRFbG5jbTVKZURacVlWcE9XU3RzU0VOTVlqaGlWbkJaUlRCeE1VSTVObWRVTW1vNGREZHVZM1JoVm5sa1oyeHhORkZ5Umpka1NHcDJjREZzTkhVeVEzQmplV3hLTnpSNWIydE5OMVpWTjFka05YUTBWekl5YjBOUk5HZDZTMFZ6ZUZFMU9HNTRkM1V6Ym5GMmNEZHNiMEpaVEdoclRHMXdiREl2V1hNNVNISnRNMGxFWVVwMmRYRXJNVzlPUVRWU1VrVmFkSEJoVnpsQmNHUldkRlZ6TURSSWFTOTJhbU0wU1RGTWRFRXpXRWd2TjBOUVZUUnJZMFZRVWtscE5VWnBNM3BZU1RKeVIwcFJkVUp4VTBaVU5VNU1NWGhyVDFaTlQzcFpUMnR4ZUhKM1NsQm1RbEpYVGtkR1UwVXdVazl6V20xNGFWTXhNMGwxWjJSbGVVdFhjbEkzVVhKbk5VUjRaMnd6YkdwblJGcFllRVJyWlhFNFExcHVTbGhFVFZwQ2NHNXhlWEZQYW14QlNWcExRVUUzU2tKSlFUWnBVV3B6UlROamNVOVRWMXBzV2xaSFRrWjVka3RwTld4amJrWlJNVWwyWTBneGJVcHpNMEZ5V1N0YWR6UlNTR2xOUldFMmJqZG9lR1YwWW1aeWVtdFdXVlkxVEhKbWVETlBMM1ZUWVVsTE9GaE5hM0pYT0dGQmNuRTRVaXR3TmpWQ1dVSnZhVlp5TWxJNU5GQlVOMU55VFZBNVJFNXlXa1ZKYzNwRVJuQklUeTlTWlN0bFRXd3pVV3c0UTIxdFZ5OXdkbWR4VTJORmVVZDFTMkpXU25aaFR6azRRV2RXY0dwb1dtTTFUWEZLV0hkUWVrNUVTRE4wVnpod2NFNXRRa2RZWTFjeVdreERaRmhaYUM5eWJUaDBaSEJIWjBGNE5qZGpURnBuUVdoUFJUUnBiV2xZWlhGc1dHc3ZUbk5DVVV3eVRVTkhNbXhETWpGamRuWnhLMFJIUm5wQlQwNUNNMmh3ZDJoeFRsazFXbG81ZFVwU05ITkZlV0ZuYWpsTFlsSnZNV1J6VGtOWVlVRldUbkIyZFZaWVpGZEZZeXRFYTJ0MlJsVkxTbHBHU1ZobWNtMDNjV3BVU0hKMWNEVkpjSHB6TVdwUFFVWldlRkYwZDJWVVIzcE1hek5DZGxGSU9XUnFiWGRMVDFjM1lpOUlaMFJxWVhGa1RqZEdRVFZuTVhJeVRteERRM2Q1TDBWTFpsVnphVFZHVjBGTWVIQkNiMmRtZG14QldERkVWbVpwTWtnNFRUbEZUVUpxYlhOalNVcGxSVUl4WmpSUVZXWTBNSGRoZVdvek1HMW9kbEY0YTFsaVFqRkhWbUpYZEdWNWFucHVOV1ZMYXpOc1RHSm5URFU1VGxKM2VXNWlkMkpqYkdjcmJWWmxZVzlhV1VKd2EycFFZMWRhZVhWblQzWnliR2x0UzNsRVFrSlNVMW8xZUdJek5HaE1OU3NyVUhaRFdqRnZWR1pVTlRRd2NsSm1ORWM1WTJkTGVVaEdlV3d6Y21kaFluVjJibU5SVEROWVkxTXpZemhQT0hWUGVEa3dTa1JXYkhKTmNFeEhhV1JaZVVVeFVGVk5VMnRHTUZaeFUwVmhWRXgyYzJOM2JuaEpTa0YyYlZoUGVFZEpSWFZyVmpKcVFqTk9RbFpTWVhCbVNIbHdVeXN4WlUxSU1rb3pOSGgyV2tGV1pWVlBaMkZhUlhOcVNrb3JaWFIzVlZWU09IaHJVbTVpVlV3M2VFZGpiRFJKZVU1VFJXTnJkV0p2YkVkd01GQXpTMmcxT1haNWVEVTJjVEpHTWt0V1pVVmpXbFkwY0hKbU5IUmhWR2wyWkRWRFQza3ZZVEZIVVhWMGFsVXJaa2M1VEhJeVRXMW5LM3BzVVRSbkszaHVPRWRFVWxKVk1EQlhVSHBvTjNoNVMyWjVhbFlyVGtwc2VrTkZheTg1V1VKQ2VXTlZRa05hU0c1aFZIZE1jVVoxUkU4NWVXaDNaMlYyWm1oSlZ6SlVOREZuWldGNGVVMDVSMDAxZFZkWlRITkxTbk5JWTFKNFZ5OTNLelp1YTFWUmVHZFhhMUJzYXk5TU4zUlJRVWRIUTA1QmFuUnVhRmh0Ymt0M1dFOUtOMDlsU2pGbVRHeDBjamsxZFhZcmNYaFNlSGxCVVVjclprY3hXbXg2Y0ZGSWJsUkRiMGQwTkdaTmJGTTJUVzlKY3pKNU5GZDFiaTlKVDA4M1duSTBiWGhJWWxSU1JqbHpRMFI1ZUc1ek1FUlFjMHcwWm14TU1sUnRaak5aVkZscFUxRnRVVzFxV1dkV1dYRkdkbk52WXpONFZrazROV0oyTjBGMGNURjJSbGRhY21Gdk1qRkRNeTh3YjA1MWQwWTFWMnhDWTFoRWR6RklSSGRRVjNWd04waFBjRGN3VTJSalFVWmxaRzV5YlRsWk1VTXJlVTFEZUZGRVprOWpRMlpuY0V0SmFFNDJkMlZQUTBGWU1VVk5NbkJIUTJscFFtMDJRMk1yTjNFMlZWaHpUVGRSYzNnemEyaGtSM3BrUVc1MlJVVklhbkl5VkZSa1NGUkdNbEU0ZWtobE1pOUdhR2xxWkVaclIzaHVUa3hZT0RObVdqRk1UMDVqVTJKM2RDODNlVEExTVVkQ1RIUmhhVXBWVnpsYWRVZHZWR0YxVEdSaFpITmpRVTFUU0VWYU1GWnBOell2WjJ4M1JqRjBVV2x4VlZOUmVEbHlORGszUlRjM1l6RmpPWGxTZGtsMmJrcFZhRGhZZFVwYVdHMHZPWFJEY2t4MlNHY3lVVFpCZWxsck1YWXliSFJLYzNsclZEZHhNMnhEWTJ4V00yUkJOazUwYWtWU1JUUktNbTVDYm1OYU5VOUNUMGxpVlZkVE9TOHdTMnRhTmpKbGFrdGlURE55UmpWRlRsQk1kbGswYkV0S2NIWTNhV05QTjJSd1RVaFRURTloVjJwM1NqTkxiRWwyYWxObVlXbExaMjFzTWxWVWEwWnBTWEpLZFRNd1ZITXZLM2xJUTFKb1FqUTVaM1ZWVmpCMFFWQmhNV1ZNWjJoaGVtTlZRMU5KVVd4d2RqWkpVMVprUW1Fd1pGQmtWMVJJUkV0d01tOVRSeXRvVEhsUVNDdGlLM0V4ZUhvdlNXMWxWRXBIWTNVMmVXbFBMelJzZDJFNFVFOU1OV0pVUkVreU0wZDJZVEZCUld0UFRDc3hjblJoVkdsWU5uRTBWMDVIVkRRNGRFSjRZMjFMVWxwMlprTnphMVUyU0dGbWNHbFRTRlZJVmpkdlQyNXFLMlZyTW0xV09TOWtWWFV5U1djNVltWnlNU3REVmtSR2NHZEZUbGszWjJ4eVRUVlZka05QTkVJdllYTnZMMXBQZUdjeFNHeE5aa2xIYTA1MU9IVkJVWEp6WkdsSlVGSnpiak5DYld0aE9VRTFhRGR4YTBGaVYya3JkelJTS3psTWRXMDBSalZNU1VvdmFFbEtiRE1yY0U0M1RWWnJiMUYyTldRMmJEUmpZWGxDZUc1U1puZ3pNVVZHVFV4V1pWaG9hVzVWVlVaelVIbHVZMkpyYmtvM09XSjVVM2hIZUhwSVFuVlllR1ozUTFSMlRuaDZTR1kxVW5KRmVqVkdVMHRoZGpSUU9HVTBVVVpuU210dGFrWkZWeTlhVDJsbmVteDViV05uYlhOdE5VTkpUM0JKUnpKSVRsWkZlVnBKTWpoMmRrZ3lka0ZQVG1KSlJubFdPRmxCYzFWUVExQmphV3B4TW1acWVtMTNMMDE0TjNwcFRtaDNla1pRY0ZGTFZFSjRkbGhTTUdsVldGbExlVkJVVlZSamRESkdSR2syUTNoQlpXa3dURTVCTVRFMFIzVjBZWHBUZUhkSFkwOXlXbEF4VVhJeFREZHBibVV3U25kQ1VUWk5kakpNWjJzMlVXUkZOSGhhZFU5bU5rMUlVVmRUU1RsUFdsVnlkbkowYjBNMWREZDNaV3hFTjBsSFZHaGpjV3B5VVhjNVJtNVVSMUp0WlVwMFkwaG9MMVZ1ZVhkcGRUVXdWMGxxU1daUGNVTnRRbFV3TDBwdmVrTkpjSEZNWlc0eE0zaE5lVWM1UW14MmVYbDFhVFV4YzBzMU9FSkVla2NyYzJVeWIzaG9WamRWTnpSRldXd3JiMUpCUVVsU09XZDVLMWhOYmtWemJ6bEdPV3RhY2tSUVpXVkZaV0ZVYTFNeWVtMWhlRTVOTlVKd1V6QnlXbmhxUVV0MVlVbEVNWFE1Um05MFNFd3pabVJ2UVc5U2NDczVVbXRLWlRsRWNGaEhTMnAzYjFRMlIyNWlkRnBvVVVSMGREZEdUbVpTTkVoWlNtdDZiM1F3YmpOcVNWcExWMUZJVVhkVWFHdEJWbEpOYldkUmFXUkpjVllyTVVGRFQwZG5TaXN2U2swd04wMW1XV3BWY0ZkWFdURm5RaTlWTDBaSlMwcFROWGhWYVdneU5GQkRRWFZwUzJaUmVFaFdUaXRIYmtaNE0xcFlXVTVJTUZvdmFFbE1WVlZQVW5ZM2JYZEhUVEkwYzNZNVkxRXhkelo1U21SbE4xbGljamMxTkhoUU1XdEZaWGRQWml0NWNsVXdSRlpQUzFsWk5XRXJiMjVJVDBJNVdrUmxNRXMxYVRsVU55dHpXVUl2VkROck9ITjViMmRHVkhFd2FFSllibk5oSzNoeFluSmFNMkpyYW5sUlpIZHNRblJ4T0hOUVZXdDBObXQxVTFWTFdYbFBNbWwwYnpCYU5sSXZNMnhSZUdvM1YxQTBOMGRUUzJONFkzUlFZa3Q2U25kSk1WWnBSMHBpU1d3eWJtZHFZVzFtZGtjek1FUXlMelJDUkUxcFIxRmlLeXRJU1hWRlRuZzJMMlZIWkc1elZEZE1NMU5rTTI5cmFWWkhhbVY2U0dWSk5ISjNTVGR1WW5wdlRVRllNRlZLWVZwcFlsZFdLMGM0TVhWM1lVVkhSVkZoYmxSU01HTnVSM2RHWTA1RldDdDJTa3hQTTFCdFNGTnJOa1JYWlV0VWJtMXVjMlZpYzJKSldIcERRVmx1TlVscVQyVnBVRTl5TXpSbk5qVlFiR1EwVFRWT1NVTndUbk01UkZOUVRXSmhaVUpFUkZoWFQyeEdOR1Y0UjFaUWNUZHZkMUJvTlVKaVVsQkxZakJsV0ZKMldsZFFWRE5YUjJkNmRrMHJkREpzZW5SYVJXRlVOSFZXU25Fd01WQm1kWFJDYkRGSFFtdHNNMEp2ZEd0WmMyeHpiRkJOZFdJeU4xcHNLM1ZLUVRjd2NYUnJNR3N4Y2xsaGEySnZTRlo2ZFhWSFQwTXpjMjlqTVhFdlRYRktjRVpPY1RRMFNYRkRkUzg1YW1ZMlRWSjJZemhCVEdkWmVtNHpRbk54V0U0M1lXTlFiM1UxWlRGUFpHbHlkRGxMUkZSR01WTm1XQzk0VkRkeFZ6TTNSWFZ4U0d4bmFUYzBUek0zYVZaa1kxZFBVRkJSVTA5VWRqZHFZVFJsV2xGNGNsZFZNbEpQTUZFeVlXSjBkblU0YjBaa1RHTjRXalZ0VjJ4VVlpc3lOakJLTmxKcmJUWlZjbWM1VnpkUllqTm5PREUzTmpOM2RIQkpZV3BrUWl0a2FYZFBlRWg1UW1jOVBRLldER0VxZE4wWnlNZlp5S3QzcEdwd1FSX2xaSEM1dWpURTlsRF9wc25yZjVHeXc4M1JKZzdzTk1tMFl0c2xWTmNfREpDOEhidGEzYThTR0ljbFhLZHB3&_eventId=submit
```


### 保持登陆状态

- 在我登陆之后，网站生成了一个标识会话的`ID`: `JSESSIONID=60D04A28237C8F0EED420B1099A5EBD7.cas16`,并通过Set-Cookie响应头发送给客户端
- 在后续每次请求时通过`Cookie`头发送回服务器

### 区分不同的包


1. 我觉得主要问题在于HTTP协议的特点：HTTP消息包括请求头和响应头，包含了**Content-Type**、**Content-Length**，指定了消息体的长度，能让接收方知道消息的边界
2. HTTP packets are distinguishable just by looking at what comes after the TCP header.  通过查看TCP标头后面的内容，来查看HTTP数据包

### 直接访问：

不成功。直接访问IP地址会导致CDN无法确定用户请求的具体内容，从而拒绝访问

#### 如何区分：

用域名和用IP地址访问，请求头不同。访问网页不同，`HOST`一栏的后面可能是域名/IP地址

### 拦截包并修改 HTTP 报文访问页面：

原先申请的时候报文是这样的，既然报文是在`host`做不同，干脆修改`host`:



```text
GET / HTTP/1.1
Host: 101.132.222.48
Accept-Language: zh-CN
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
```

之后将`Host`修改成`cubicy.icu`就访问到了未备案界面

```text
GET / HTTP/1.1
Host: cubicy.icu
Accept-Language: zh-CN
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
```


![](image/Pasted%20image%2020240718010401.png)
### 为什么未备案

根据之前的探索，这个网站使用了CDN
因为我直接修改报文，而没有通过本地的DNS解析，所以是用的是源服务器地址是 `101.132.222.48`，而这个地址没有被备案
而使用`ns-lookup`返回的两个结果，即cdn提供的两个服务器，`104.21.31.206`,`172.67.179.244` 都备案了，如果用这两个来访问，不会有类似的结果
所以进行一下尝试，过程类似，不赘述了

![](image/Pasted%20image%2020240718011421.png)

果然这两个成功访问


## Task 3

用了`selenium.webdriver` 让网站自动登录（得在代码里提供一下账号密码）
然后用正则表达式去表达
具体代码见附件`GetScore.py`
具体实现效果如下：
Note: 
1. 其中在成绩下面两行在交上的代码被注释掉了
2. 具体的chromedriver地址/id/password都被修改掉了，要想运行需要填写相关的值

![alt text](image/Pasted%20image%2020240707140337.png)

## Bonus:

- TCP建立的是可靠的连接，必须要传输成功所有数据包，所以如果一个数据包丢失，接收端必须等待重新传输的包，这会导致整个连接的阻塞
- TCP需要进行三次握手建立连接，所以会导致连接时间延迟
- 上述性能使得TCP的表现并不好
- HTTP/3使用的是基于UDP的QUIC，在应用层实现多路复用，每个流有独立的顺序控制和流量控制，丢失数据包只会影响其中一支；由于传输稳定性能保证，也将三次握手合并成一次握手，就提高了传输时间

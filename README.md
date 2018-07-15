SSRR 3.2.2


#### 1.安装
```
    git clone https://github.com/ssrpanel/shadowsocksr.git

或者通过wget下载

    wget https://github.com/ssrpanel/shadowsocksr/archive/master.zip && unzip master && mv shadowsocksr-master shadowsocksr

```

#### 2.安装cymysql
```
    sh setup_cymysql2.sh
```

#### 3.编辑节点配置（混淆、协议、限速、IPV6）
```
    vi user-mysql.json

    ** protocol ** 协议，带 _compatible 结尾兼容 原版，直接用原版可以改为 origin
    ** protocol_param ** 协议参数，配置了的话，客户端也要一致
    ** obfs ** 混淆 tls1.2_ticket_auth 可以限制客户端数量 tls1.2_ticket_auth_compatible 兼容原版，直接用原版可以改为 plain
    ** obfs_param ** 混淆参数，当obfs为 tls1.2_ticket_auth 的时候，这个值为 1 到 256 之间，表示限制客户端数量
    additional_ports 单端口配置，请看wiki
    additional_ports_only 强制单端口，改为true则所有非设置的单端口都无法连接，只能用additional_ports设置的那些端口连接
    dns_ipv6 为true时，强制服务器优先走ipv6，需要节点服务器至少有一个2开头的ipv6地址（有时候会导致IPV4失效）
    connect_verbose_info 为1时记录用户访问网址，推荐打开，可以清楚知道连接成功与否
    redirect 请求失败时返回信息伪造成访问配置里网址

```

#### 4.运行、关闭、看日志
```
    sh logrun.sh
    sh stop.sh
    sh tail.sh
```

#### 5.注意

    - 数据库机的 iptables、firewall 得对本节点IP开放
    - 数据库机的 mysql 的对本节点进行授权（不推荐使用root账号）
    - 再不懂可以进小群咨询 [我要进小群](https://github.com/ssrpanel/SSRPanel/wiki/%E6%88%91%E8%A6%81%E8%BF%9B%E5%B0%8F%E7%BE%A4)

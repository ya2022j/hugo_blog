+++
title = "Centos7安装Docker"
tags = [
"docker",
"Chinese",
]
date = "2022-08-05 11:20:50"
categories = [
"Chinese",
]
+++



# Centos7安装Docker(2022最新亲测可用)

这里参考官方文档进行操作： <https://docs.docker.com/engine/install/centos/>

1.卸载docker旧版本（我的centos7是新的，所以运行后不删除任何软件包）

```commandline    
    
    yum remove docker \
         docker-client \
         docker-client-latest \
         docker-common \
         docker-latest \
         docker-latest-logrotate \
         docker-logrotate \
         docker-engine
    
```

2.安装yum-utils软件包

    
```commandline
    yum install -y yum-utils
```

3.设置Docker仓库（这里使用阿里云地址）

    
```commandline    
    yum-config-manager \
     --add-repo \
     http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
    
```

4.更新yum软件包索引

    
```commandline    
    yum makecache fast
    
```

5.安装最新版本的Docker

```commandline
    
    yum install docker-ce docker-ce-cli containerd.io
    
```

然后会出现下面这种情况：（官网已经给了我们提示）指纹匹配选择 y 6.启动docker systemctl start docker
7.查看docker版本

 ```commandline   
    
    docker version
    
```


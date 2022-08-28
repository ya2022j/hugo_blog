+++
title = "Nginx伪流媒体服务器搭建"
tags = [
"nginx",
"Chinese",
]
date = "2022-08-01 21:28:36"
categories = [
"Chinese",
]
+++




#  Nginx伪流媒体服务器搭建

Nginx 支持伪流媒体播放功能，其可以和客户端的 Flash 播放器结合，对以 .flv、.f4f、.mp4、.m4v、.m4a 为扩展名的文件实现流媒体的播放功能。若启用伪流媒体的支持功能，需要按媒体文件格式在配置编译时增加 --with-http_f4f_module、--with-http_flv_module 和 --with-http_mp4_module 这 3 个参数。



    

##  1、模块配置指令

伪流媒体模块配置指令如下表所示。  
  

指令名称 |  指令值格式 |  默认值 |  指令说明  
---|---|---|---  
f4f |  \-- |  \-- |  启用 F4F 文件支持  
f4f_buffer_size |  size |  512k |  设置读取 .f4x 索引文件的缓冲区大小  
flv |  \-- |  \-- |  启用 FLV 文件支持  
mp4 |  \-- |  \-- |  启用 MP4 文件支持  
mp4_buffer_size |  size |  512k |  设置处理 MP4 文件的缓冲区大小  
mp4_max_buffer_size |  size |  512k |  Metadata 数据处理过程中的最大缓冲区大小  
mp4_limit_rate |  on 或 off 或 facto |  off |  限制客户单媒体流请求的最大速率。仅在 Nginx 商业版本中提供  
mp4_limit_rate_after |  time |  60s |  客户单媒体流请求的速率达到指定值时开始限速。仅在 Nginx 商业版本中提供  
  
F4F 格式仅在 Nginx 商业版本中提供。  

##  2、伪流媒体配置样例

伪流媒体配置样例是利用 Nginx 的自动索引功能生成 XML 格式的目录列表，通过 XSLT 生成前端页面，使用 jQuery 插件 video.js 的
Flash 播放器播放 FLV 及 MP4 格式的流媒体文件。页面效果如下图所示。  
  
Nginx 配置样例如下：  



```commandline
    
    server {
        listen 8081;
        server_name localhost;
        charset utf-8;
        root /opt/nginx-web/files;
        default_type text/xml;
    
    
    location / {
       autoindex on;                                    # 启用自动页面功能
       autoindex_localtime on;                          # 使用Nginx服务器时间
       autoindex_format xml;                            # 自动页面输出格式为XML
       xslt_stylesheet conf/conf.d/example/test.xslt;   # 引入XSLT模板文件
    }
    
    location ~ \.flv$ {
        flv;                                            # FLV文件启用伪流媒体支持
    }
    location ~ \.mp4$ {
        mp4;                                            # MP4文件启用伪流媒体支持
        mp4_buffer_size       1m;                       # MP4文件的缓冲区大小为1MB
        mp4_max_buffer_size   5m;                       # MP4文件最大缓冲区大小为5MB
    }
    

}

```



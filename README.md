#运行说明
环境：python3.6
主要依赖包：pdfminer、pandas、matplotlib
安装依赖包的时候直接```pip3 install xxx ```会比较慢，建议使用其它的镜像源。其中，比较常用的国内镜像包括：
（1）阿里云 http://mirrors.aliyun.com/pypi/simple/
（2）豆瓣 http://pypi.douban.com/simple/
（3）清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
（4）中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
（5）华中科技大学 http://pypi.hustunique.com/
使用指令为：```pip3 install XXX -i http://mirrors.aliyun.com/pypi/simple/```
有时候会不信任国内镜像源，加上--trusted-host mirrors.aliyun.com 就可以了：
``` pip3 install pandas -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com```
ps：XXX代表某个依赖包的名字如pandas，pip3对应python3.X

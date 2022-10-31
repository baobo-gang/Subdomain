## Subdomain

Subdomain: 多种渠道的子域名收集器

#### 程序只供交流，请勿用于非法用途，否则产生的一切后果自行承担 ! ! !



## 依赖

```python
pip install threading
pip install queue
pip install sys
pip install bs4
```



## 运行方式

python  sub_domain.py



## 结构

- cache  收集的子域名保存的地方
- brute.py  字典收集子域名模块
- crt.py  在线收集子域名模块
- common.py  所有模块使用的公共方法
- config.py  配置文件
- sub_domain.py  启动程序



## 验证方式

- 返回状态码
- 返回内容正则判断



## 配置相关

##### config.py里面的timeout为请求的超时时间，建议设置2或3

```python
timeout= 2
```

##### config.py里面的cache_base_path为获取子域名后的文件保存文件夹

```python
cache_base_path = "./cache/"
```

##### config.py里面的cache_base_path为爆破域名字典的字典路径

```python
domain_dict_path = "./dict/domain2.txt"
```

##### config.py里面的module_list为目前拥有的模块列表, 如果新增需要加入下面的列表

```python
module_list = ['crt', "brute"]
```

##### config.py里面的domain为想要收集的子域名的域名，建议去掉www

```python
domain = "xxx.com/net"
```

##### config.py里面的thread为字典获取子域名的线程数量，不要设置太高

```python
thread = 50
```



## 效果

运行时改sub_domain.py 中的domain域名即可

![image-20221031133638886](C:%5CUsers%5Clenovo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20221031133638886.png)

##### 最后再说一次：程序只供交流，请勿用于非法用途，否则产生的一切后果自行承担  ！！ ！
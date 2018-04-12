
class DFS(object):
    '''
    numlen: 为有几位数字，如3,则为1,2,3
    result: 用来保存个序列的结果
    book: 用来判断那个数字已经排列了
    '''
    def __init__(self, n):
        self.numlen = n
        self.result = [0 for i in range(n)]
        self.book = [0 for i in range(n)]

    def dfs(self, s):
        step = s-1
        if step == self.numlen:
            r = ''
            for i in range(self.numlen):
                r += str(self.result[i])

            print (r)
            return

        # 用来尝试每种可能，即第step位的数为i
        for i in range(self.numlen):
            if self.book[i] == 0:
                self.result[step] = i+1
                self.book[i] = 1
                self.dfs(s+1)
                self.book[i] = 0
        return

if __name__ == '__main__':
    d = DFS(5)
    d.dfs()
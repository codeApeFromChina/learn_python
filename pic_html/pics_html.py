#codding:utf-8
import os

pic_root = "G:\Downloads\堀江耽閨@1024李香蘭@比思論壇米兰死忠"
html_root = "G:"

def pics2html():
    # root_dir = open(pic_root)
    count = 0
    for root, dirs, files in os.walk(pic_root):
        count += 1
        print(root,"---",dirs, "----", files)
        with open(html_root + "/" + str(count) + ".html", 'w') as hf:
            for file in files:
                hf.write("<img src = '{0}'/>".format(root + "\\" + file))

if __name__ == '__main__':
    pics2html()
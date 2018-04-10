#coding:utf-8
import os

base_dir = "H:/aaa/fuliyidian20180121"
# base_dir = "H:/aaa/fff/写真/NO.0001-1000/[RS] NO.301-400/[ROSI写真] NO.301-400\\NO.388"
html_dir = "H:/aaa/fuliyidian20180121/html/"
html_mov_dir = "H:/aaa/ff_mov_html/"
html_pic_count = 50

jpg_exts = ['jpg','png','jpeg']
mov_exts = ['mp4','avi','mov']
ext_set = set()
# img_label =
def gen_html():

    for root, dirs, files in os.walk(base_dir):
        try:
            pic_count = 0
            for f in files :
                if get_file_extension(f).lower() in jpg_exts:
                    pic_count +=1

            if pic_count > 5:
                f_count = 0
                file_name = root.split("\\")[-1]
                file_name = file_name.replace('[','_').replace("-",'_').replace(' ','')
                f_html = open(html_dir + file_name + ".html",'w+', encoding='utf-8')
                all_f_count = len(files)
                for f in files:
                    ext_set.add(get_file_extension(f))
                    if get_file_extension(f) in jpg_exts :
                        c = "<img src='" + str(root) + "/" + str(f) +"' width='99%'/>"
                        f_html.write(c)
                        f_count += 1
                        if f_count%html_pic_count == 0 :
                            f_html.close()
                            f_html = open(html_dir + file_name + '_' + str(f_count/html_pic_count) + ".html", 'w+', encoding='utf-8')
                    if get_file_extension(f) in mov_exts :
                        c = "<video src='" + str(root) + "/" + str(f) + "' controls='controls' width='95%' height = '95%'></video>"

                            # "<img src='" + str(root) + "/" + str(f) + "' width='99%'/>"
                        with open(html_mov_dir + "1" + file_name + ".html", 'w+', encoding='utf-8') as f_mov_html:
                            f_mov_html.write(c)

                f_html.close()
        except : pass
def get_file_extension(path):
    return (os.path.splitext(path)[1])[1:].lower()


def get_file_name(path):
    return (os.path.splitext(path)[0])

if __name__ == '__main__':
    # print (get_file_extension('H:/aaa/fff/写真/[UX]2017.06.28 VOL.058w/aaaa.jpg'))
    gen_html()
    print("%s"%"AAA".lower())
    print (ext_set)

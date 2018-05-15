# codding:utf-8
import os
import requests
from bs4 import BeautifulSoup
import re


def get_header():
    headers = {
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Host': 'mtl.ttsqgs.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.meitulu.com/item/12831_2.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
    return headers


def get_index():
    proxies = {
        'http': 'socks5://127.0.0.1:1080',
        'https': 'socks5://127.0.0.1:1080'
    }
    root_file = 'G:/pictures/bl'
    root_url = 'https://www.meitulu.com/t/beautyleg/'
    # resp = requests.get(root_url, proxies=proxies)
    resp = requests.get(root_url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    pattern = re.compile(r'^https://www.meitulu.com/item/\d+.html$')

    count = 0
    for item in soup.find_all("p", class_='p_title'):
        # print(type(item))
        try:
            page_url = item.contents[0]['href']  # 图片列表url

            if pattern.match(page_url):
                # print(page_url)
                page_resp = requests.get(page_url)
                pics_name = str(page_url).split('/')[-1].split('.')[0]  # the pictures name
                pics_path = root_file + '/' + pics_name  # pictures dir path
                if not os.path.exists(pics_path):
                    os.mkdir(pics_path)
                print(str(page_url).split('/')[-1].split('.')[0])
                page_resp.encoding = 'utf-8'
                page_soup = BeautifulSoup(page_resp.text, 'html.parser')  # pictures url
                for child in page_soup.center.children:  # current page's pics ,4 pics
                    pic_url = str(child['src'])
                    pic_name = pics_name + '-' + pic_url.split("/")[-1]
                    print(requests.get(pic_url, headers=get_header()).content)
                    with open(pics_path + '/' + pic_name, 'wb') as pics_f:
                        pics_f.write(requests.get(pic_url, headers=get_header()).content)
                    print(pics_name + '-' + pic_url.split("/")[-1])

                pics_count = int(page_soup.find(id='pages').contents[-3].string)  # pictures pages
                print(pics_count)

                for i in range(2, pics_count + 1):
                    # print(page_url + '_' + str(i))
                    page_i_url = str(page_url).replace(".html", "") + '_' + str(i) + ".html"
                    page_i_resp = requests.get(page_i_url)
                    page_i_resp.encoding = 'utf-8'
                    page_i_soup = BeautifulSoup(page_i_resp.text, 'html.parser')  # pictures url
                    for child in page_i_soup.center.children:  # current page's pics ,4 pics
                        pic_i_url = str(child['src'])
                        print(pics_name + '-' + pic_i_url.split("/")[-1])

                # print(page_soup.find(id='pages').contents[-3].string)



        except Exception as e:
            print(e)

    print(count)


if __name__ == '__main__':
    get_index()

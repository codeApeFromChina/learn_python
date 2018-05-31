# codding:utf-8
import os
import multiprocessing
import requests
from bs4 import BeautifulSoup


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
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/65.0.3325.181 Safari/537.36',
    }
    return headers


def download_pic(pics_path, pic_name, pic_url):  # download picture
    with open(pics_path + '/' + pic_name, 'wb') as pics_f:
        pics_f.write(requests.get(pic_url, headers=get_header()).content)


def get_all_pages_url():
    page_urls = []
    root_url = 'https://www.meitulu.com/t/legku/'
    resp = requests.get(root_url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    # page_count = int(soup.find(id='pages').contents[-3].string)  # pictures pages
    for item in soup.find_all("p", class_='p_title'):
        page_url = item.contents[0]['href']  # 图片列表url
        page_urls.append(page_url)

    # for i in range(2, page_count + 1):
    #     list_url = str(root_url).replace(".html", "") + str(i) + ".html"
    #     list_resp = requests.get(list_url)
    #     list_soup = BeautifulSoup(list_resp.text, 'html.parser')
    #     for item in list_soup.find_all("p", class_='p_title'):
    #         page_url = item.contents[0]['href']  # 图片列表url
    #         page_urls.append(page_url)

    return page_urls


def get_index():
    # proxies = {
    #     'http': 'socks5://127.0.0.1:1080',
    #     'https': 'socks5://127.0.0.1:1080'
    # }
    root_file = 'G:/pictures/legku'
    # root_url = 'https://www.meitulu.com/t/beautyleg/'
    # resp = requests.get(root_url, proxies=proxies)
    # resp = requests.get(root_url)
    # soup = BeautifulSoup(resp.text, 'html.parser')
    #
    # pattern = re.compile(r'^https://www.meitulu.com/item/\d+.html$')
    page_urls = get_all_pages_url()
    count = 0
    for page_url in page_urls:
        try:
            # page_url = item.contents[0]['href']  # 图片列表url
            # if pattern.match(page_url):
            download_pic_task = []
            # print(page_url)
            page_resp = requests.get(page_url)
            pics_name = str(page_url).split('/')[-1].split('.')[0]  # the pictures name
            pics_path = root_file + '/' + pics_name  # pictures dir path
            print(pics_path)
            if not os.path.exists(pics_path):
                os.mkdir(pics_path)
            else:
                continue
            print(str(page_url).split('/')[-1].split('.')[0])
            page_resp.encoding = 'utf-8'
            page_soup = BeautifulSoup(page_resp.text, 'html.parser')  # pictures url
            for child in page_soup.center.children:  # current page's pics ,4 pics
                pic_url = str(child['src'])
                pic_name = pics_name + '-' + pic_url.split("/")[-1]
                download_pic_task.append((pics_path, pic_name, pic_url))
                # with open(pics_path + '/' + pic_name, 'wb') as pics_f:
                #     pics_f.write(requests.get(pic_url, headers=get_header()).content)

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
                    pic_i_name = pics_name + '-' + pic_i_url.split("/")[-1]
                    download_pic_task.append((pics_path, pic_i_name, pic_i_url))

                    # with open(pics_path + '/' + pic_i_name, 'wb') as pics_f:
                    #     pics_f.write(requests.get(pic_i_url, headers=get_header()).content)

            with multiprocessing.Pool(30) as pool:
                pool.starmap(download_pic, download_pic_task)

        except Exception as e:
            print(e)

    print(count)


def f(i, j):
    print(i + j)


if __name__ == '__main__':
    # print(get_all_pages_url())
    get_index()
    # with multiprocessing.Pool(10) as pool:
    #     pool.starmap(f, [(i, i + 1000) for i in range(1, 100000)])

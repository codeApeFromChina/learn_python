import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


proxies = {
        'http': 'http://127.0.0.1:1080',
        'https': 'http://127.0.0.1:1080'
    }
# index_url = "http://91.91p17.space/search_result.php?search_id=%E4%B8%9D%E8%A2%9C&search_type=search_videos&x=50&y=10&page=1"
headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
'Connection': 'keep-alive',
'Cookie': '__cfduid=d744583b446448904f5870494a4412d201527255224; __utmz=50351329.1527255112.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); language=cn_CN; evercookie_cache=undefined; evercookie_etag=undefined; 91username=xinghen1991; __utma=50351329.1630715392.1527255112.1527774484.1529380971.3; __utmb=50351329.0.10.1529380971; __utmc=50351329; CLIPSHARE=robo7vovoaoibob46smu156c50; __51cke__=; __dtsu=1EE7044502EF2F5A62150C1302F99839; DUID=c109uRyEcjEAAKrnCYyZ3lFxfe7fZBeJDhuknQp%2B9hnknYmn; USERNAME=6620rPLKvPliG7BggXUxjLB3OR3ZBcN2CkjttFqTrjcWwgTDBiq2SA; user_level=1; EMAILVERIFIED=no; level=1; __tins__3878067=%7B%22sid%22%3A%201529380976077%2C%20%22vd%22%3A%207%2C%20%22expires%22%3A%201529382863469%7D; __51laig__=7',
'DNT': '1',
'Host': '91.91p17.space',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}


def query_url_list(index_url):
    url_list = []
    resp = requests.get(index_url, headers = headers, proxies = proxies)
    resp.encoding = 'utf-8'
    # print(resp.text)
    from bs4 import BeautifulSoup
    page_soup = BeautifulSoup(resp.text, 'html.parser')  # pictures url
    link_list = page_soup.find_all("div", class_ = "listchannel")


    for item in link_list:
        try:
            url = item.contents[1].contents[1]['href']
            print(url)
            url_list.append(url)
        except Exception as e:
            pass
    return url_list

def Main ():
    index_url = 'http://91porn.com/search_result.php?search_id=%E4%B8%9D%E8%A2%9C&search_type=search_videos&viewtype=basic&page='
    url_list_file = 'g:/url_lists'
    with open("list_file", 'w') as f:
        for i in range(1, int(2100/20)+1):
            page_url = index_url + str(i)
            url_lists = query_url_list(page_url)
            for url in url_lists:
                f.write(url)
                f.write('\n')



def trans_url(ori_url):
    base_url = 'https://www.parsevideo.com/'
    trans_urls = []
    # cap = DesiredCapabilities().FIREFOX.copy()
    # cap["marionette"] = False
    # browser = webdriver.Firefox(log_path = 'firefox.log', capabilities=cap, firefox_binary=r'D:\software\firefox\firefox.exe', executable_path="D:/develop\WinPython-64bit-3.6.3.0Qt5/python-3.6.3.amd64/Scripts/geckodriver.exe")

    browser = webdriver.PhantomJS()
    browser.get(base_url)
    browser.find_element_by_id('url_input').clear()
    browser.find_element_by_id('url_input').send_keys(ori_url)
    browser.find_element_by_id('url_submit_button').click()
    browser.save_screenshot("before_request.png")
    print(browser.find_element_by_id('url_submit_button').get_attribute('disabled'))
    try:
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "url_submit_button")))
        browser.save_screenshot("after_request.png")
        elements = browser.find_elements_by_name("search")
        for item in elements:
            print(item.get_attribute("value"))
            trans_urls.append(item.get_attribute("value"))
        # browser.save_screenshot("request.png")
    finally:
        browser.quit()

    sort_item = []
    sort_item.append(trans_urls[1])
    sort_item.append(trans_urls[3])
    sort_item.append(trans_urls[5])
    sort_item.append(trans_urls[0])
    sort_item.append(trans_urls[4])

    return sort_item


def download_file(file_url, file_name):
    f_video = 'g:/91video/{0}.mp4'.format(file_name)
    # print(requests.get(file_url).content)
    try:
        with open(f_video, 'wb') as f:
            f.write(requests.get(file_url).content)

            return True
    except Exception as e:
        print("{0}, download error. error {1}".format(file_url, e))
        error_log("download error, ", e)
        return False


def read_file_download():
    try:
        with open('list_file', 'r') as url_f:
            file_count = 10
            for item in url_f:
                print(item.strip())
                trans_urls = trans_url(item.strip())
                count = 0
                for trans_item in trans_urls:
                    print('trans url {0} is : {1}'.format(count, trans_item))
                    if download_file(trans_item, file_count):
                        count += 1
                        break;
                if count < 1:
                    error_log("download ori url {0} error".format(item), None)
                file_count += 1

    except Exception as e:
        print("download error. error {0}".format(e))
        error_log("read url list error", e)



def error_log(msg, e):
    with open("g:/91video/logg", 'w') as lf:
        lf.write("error message is : {0}, error is : {1}".format(msg, e))

if __name__ == '__main__':
    # trans_url("http://91porn.com/view_video.php?viewkey=eddeaeed1bffb77efdcb&page=1&viewtype=basic&category=mr")
    # Main()
    # download_file("http://g.t4k.spac//mp43/269494.mp4?st=iQpvd2xxfqQldEiVAm_pvA&e=1529454469")
    read_file_download()





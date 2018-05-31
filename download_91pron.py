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
'Cookie': '__cfduid=d55e72dd417cd605cc8363789b52ba4d21527309897; CLIPSHARE=9nb15qhbvr6gjkj7qq0btgic17; __utma=140380155.93594660.1527309789.1527309789.1527309789.1; __utmb=140380155.0.10.1527309789; __utmc=140380155; __utmz=140380155.1527309789.1.1.utmcsr=thetend.com|utmccn=(referral)|utmcmd=referral|utmcct=/retire.php; __51cke__=; __dtsu=1EE7044502EF2F5A62150C1302F99839; language=cn_CN; 91username=xinghen1991; DUID=834bJcfiB60LX0Y7IWYlTWi5E9pIBiSHKLmmN%2Fx2jHTjC5ke; USERNAME=e21epuhDZHxiPYw3YEeb7Jce2IDrcxOnopp2Y%2BuZIjf%2FJsy1fxD0YQ; user_level=1; EMAILVERIFIED=no; level=1; __tins__3878067=%7B%22sid%22%3A%201527309788561%2C%20%22vd%22%3A%2017%2C%20%22expires%22%3A%201527311914565%7D; __51laig__=17',
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
    index_url = 'http://91.91p17.space/search_result.php?search_id=%E4%B8%9D%E8%A2%9C&search_type=search_videos&x=50&y=10&page='
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
    cap = DesiredCapabilities().FIREFOX.copy()
    cap["marionette"] = False
    # browser = webdriver.Firefox(log_path = 'firefox.log', capabilities=cap, firefox_binary=r'D:\software\firefox\firefox.exe', executable_path="D:/develop\WinPython-64bit-3.6.3.0Qt5/python-3.6.3.amd64/Scripts/geckodriver.exe")

    browser = webdriver.PhantomJS()
    browser.get(base_url)
    browser.find_element_by_id('url_input').clear()
    browser.find_element_by_id('url_input').send_keys(ori_url)
    browser.find_element_by_id('url_submit_button').click()
    # browser.save_screenshot("before_request.png")
    print(browser.find_element_by_id('url_submit_button').get_attribute('disabled'))
    try:
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "url_submit_button")))
        elements = browser.find_elements_by_name("search")
        for item in elements:
            print(item.get_attribute("value"))
            trans_urls.append(item.get_attribute("value"))
        # browser.save_screenshot("request.png")
    finally:
        browser.quit()


def download_file(file_url):
    f_video = 'g:/91video/4.mp4'
    # print(requests.get(file_url).content)
    with open(f_video, 'wb') as f:
        f.write(requests.get(file_url).content)


if __name__ == '__main__':
    trans_url("http://91porn.com/view_video.php?viewkey=816d97f0a3504ac3ed0c")
    # Main()
    # download_file("http://192.240.120.34//mp43/266462.mp4?st=Gz1Ej76JkDyKZYCeR1ooKQ&e=1527412384")





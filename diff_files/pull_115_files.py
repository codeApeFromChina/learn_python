import requests
import json

if __name__ == '__main__':
    headers = {
        'host':'web.api.115.com',
        'x-requested-with':'XMLHttpRequest',
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36 115Browser/8.4.0',
        'referer':'http://web.api.115.com/bridge_2.0.html?namespace=Core.DataAccess&api=UDataAPI&_t=v5',
    }
    cookies = dict(ssov_594669293='1_594669293_94ed6ea6d839a2666fb040a00cef09f0', PHPSESSID='49ovegu89j7753o6piql0k03m4', OOFL='594669293', UID='594669293_A1_1517454635', CID='9572c26f8c8548c326cd67a2608fe0e4', SEID='de9e66bb11f4c3128139c303f35a880bb6a0fdbbcc67884a47e05fe78b3cb08c883924305de87816a570b8436ed72a163948871e289f70737e10f77c', Hm_lvt_44a958b429c66ae50f8bf3a9d959ccf5='1516250473,1516600880,1516951213,1517295618', Hm_lpvt_44a958b429c66ae50f8bf3a9d959ccf5='1517454639',)
    url = "http://web.api.115.com/files?aid=1&cid=1136051790018644625&o=user_ptime&asc=0&offset={0}&show_dir=1&limit={1}&code=&scid=&snap=0&natsort=1&source=&format=json&type=&star=&is_share=&suffix=&custom_order=2&fc_mix="

    r = requests.get(url.format(0, 100), headers=headers, cookies=cookies)
    d = r.json()
    for key, value in r.json().items():
        if type(value) is type([]):
            for i in value:
                print(i)
        print(key + ' , ' + str(value))
        # for i in d:
        #     print("files count is :" + str(len(d)))
        #     print(i['n'])

    # 获取所有文件列表
    # f = open('115_files', 'w', encoding='utf-8')
    # all_flie_names = ''
    # for i in range(7):
    #     print(i)
    #     r = requests.get(url.format((i)*100, 100), headers=headers, cookies=cookies)
    #     # print(r.content.decode('unicode_escape'))
    #     d = r.json()['data']
    #     print("files count is :" + str(len(d)))
    #     for i in d:
    #         all_flie_names += (i['n'] + '\r\n')
    # f.write(all_flie_names)
    # f.close()
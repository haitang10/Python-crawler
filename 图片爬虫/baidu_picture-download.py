'''自动下载百度图片，可以设置关键词和页数，数据同步加载，采用正则表达式确定图片链接'''

import requests
import re
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print('shibai')
def download_photo(url):
    html = getHTMLText(url)
    photo_url_list = re.findall(r'\"objURL\":\"(.*?)\"',html,re.S )
    print(photo_url_list )
    a = 0
    for i in photo_url_list :
        photo = requests.get(i)
        path = 'C://Users/王贺/Desktop/photo/baidu/'+ str(a)+'.jpg'
        a+=1
        with open(path, 'wb') as f:
            f.write(photo.content)
            f.close()
    print('successful')

def main():
    keyword = '翘臀'
    pages = 10
    #start_url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=大学&pn=20'
    start_url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + keyword
    for i in range(pages):
        try:
            url = start_url+'&pn='+str(i)
            download_photo(url)
        except:
            continue
main()
'''自动下载百度图片，可以设置关键词和页数，数据同步加载，采用正则表达式确定图片链接'''

import requests
from bs4 import BeautifulSoup
import os

def getHTMLText(url):
    try:
        k = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

        r = requests.get(url,timeout=300,headers = k)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print('shibai')
def download_photo(url,img_list):
    html = getHTMLText(url)
    soup = BeautifulSoup(html,'html.parser')
    #div = soup.find_all('div',attrs={'class':'comment-meta commentmetadata'})
    p = soup.find_all('p')

    for i in p:
        photo = i.find('img').get('src')
        img_list.append(photo)
    print(img_list)
    a = 0
    path = 'C://Users/王贺/Desktop/photo/zipai'
    for i in img_list :
        filename = path+'/'+str(a) + '.jpg'
        photo = requests.get(i,headers=header(i))
        print(i)
        with open(filename, 'ab') as f:
            f.write(photo.content)
            f.close()
            print('ok')
        a += 1
    print('successful')

def header(referer):
    headers = {
        'Referer':'{}'.format(referer),
        'host' : 'i.meizitu.net',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }
    return headers

def main():
    pages = 1
    start_url = 'http://www.mzitu.com/zipai/comment-page-'
    for i in range(pages):
        img_list = []
        try:
            url = start_url+str(i)
            print(url)
            download_photo(url,img_list)
        except:
            continue
main()
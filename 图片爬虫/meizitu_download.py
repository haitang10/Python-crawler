import requests
from bs4 import BeautifulSoup
import re
import os
def getHTMLText(url):
    try:
        k = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
        r = requests.get(url,timeout=30,headers = k)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print('shibai')
def get_page_urls(url , page_urls):
    html = getHTMLText(url)
    soup = BeautifulSoup(html ,'html.parser')
    a = soup.find_all('a',attrs={'target':"_blank"},string =re.compile(r'.*?'))
    for i in a:
        b = i.get('href')
        page_urls.append(b)
    return page_urls

def get_photo_link(page_urls):
    m =1
    for link in page_urls:
        photo_urls = []
        html = getHTMLText(link)
        soup = BeautifulSoup(html,'html.parser')
        title = soup.find('h2',attrs={'class':'main-title'}).string.replace('?','')
        total = soup.find('div',attrs= {'class':'pagenavi'}).find_all('a')[-2].find('span').string
        for i in range(int(total)):
            photo_url =link +'/' +str(i)
            html = getHTMLText(photo_url)
            soup = BeautifulSoup(html,'html.parser')
            img = soup.find('div',attrs= {'class':'main-image'}).find('img').get('src')
            photo_urls.append(img)
        k =1
        path = 'D://photo/fengjing/{}'.format(title)

        if not os.path.exists(path):
            os.makedirs(path)
        for i in photo_urls:
            print('正在下载第{}套第{}张图'.format(m,k),title)
            filename = path + '/' + str(k)+'.jpg'
            k += 1
            try:
                with open(filename , 'ab') as f:
                    a = requests.get(i,headers = header(i))
                    f.write(a.content)
                    f.close()
            except :
                continue
        m+=1
def header(referer):
    headers = {
        'Referer':'{}'.format(referer),
        'host' : 'i.meizitu.net',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }
    return headers
def main():
    start_url = 'http://www.mzitu.com/page/'
    pages = 20
    for i in range(10,int(pages)):
        page_urls = []
        url = start_url + str(i)+'/'
        get_page_urls(url, page_urls)
        get_photo_link(page_urls)
main()

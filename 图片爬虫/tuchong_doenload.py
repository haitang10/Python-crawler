'''
搜狗图片自动下载，网页为异步加载 ，response为json格式，解析出url链接到列表
'''
import requests
import json
import os
from bs4 import BeautifulSoup
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print('shibai')
    #keyword = '性感'
def main():
    pages = 15
    start_url = 'https://tuchong.com/rest/tags/私房/posts?page='
    a=0
    for i in range(pages):
        try:
            photo_url_list = []
            url = start_url +str(i)+'&count=20'
            html = getHTMLText(url)
            json_text = json.loads(html)  # json格式
            json_text = json_text['postList']
            # 列表
            for j in json_text:
                photo_url_list.append(j['url'])
            print(photo_url_list)

            path = 'D://photo/sifang/'
            if not os.path.exists(path):
                os.mkdir(path)

            for url in photo_url_list:
                html = getHTMLText(url)
                soup = BeautifulSoup(html, 'html.parser')
                artile = soup.find('article', attrs={'class': 'post-content'})
                img_list = artile.find_all('img')
                photo_list = []
                for i in img_list:
                    photo_list.append(i.get('src'))
                print(photo_list )
                for img in photo_list:
                    photo = requests.get(img)
                    filename = path + str(a) + '.jpg'
                    with open(filename, 'wb') as f:
                        f.write(photo.content)
                        f.close()
                    print('正在下载第{}张图片'.format(a))
                    a+=1

        except:
            continue


main()

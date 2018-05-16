'''
搜狗图片自动下载，网页为异步加载 ，response为json格式，解析出url链接到列表
'''
import requests
import json
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print('shibai')
def download_photo(url,photo_url_list):
    html = getHTMLText(url)
    json_text = json.loads(html) # json格式
    json_text =json_text['all_items'] #列表
    for j in json_text :
        photo_url_list.append(j['thumbUrl'])
    print(photo_url_list )
    a = 0
    for i in photo_url_list :
        photo = requests.get(i)
        path = 'C://Users/王贺/Desktop/photo/sougou/'+ str(a)
        a+=1
        with open(path, 'ab') as f:
            f.write(photo.content)
            f.close()
def main():
    #keyword = '大学'
    pages = 20
    photo_url_list = []
    start_url = 'http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category=%E7%BE%8E%E5%A5%B3&tag=%E5%85%A8%E9%83%A8&start=15&len='
    for i in range(pages):
        try:
            url = start_url+str(i)
            download_photo(url,photo_url_list)
        except:
            continue

main()
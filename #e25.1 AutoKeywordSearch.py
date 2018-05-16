# e25.1 AutoKeywordSearch.py
import requests
from bs4 import BeautifulSoup
import re
import json
def getKeywordResult(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ''
def parserLinks(html):
    soup = BeautifulSoup(html,"html.parser")
    links = []
    data = soup.find_all('div',{'data-tools':\
                                re.compile ('title')})
    
    for div in data:
        data1 = div.attrs['data-tools']
        d = json.loads(data1)
        links.append(d['title'])
    return links

    
def main():
    keyword =input('请输入您要查询的信息')
    url = 'http://www.baidu.com/s?wd=' + keyword
    html = getKeywordResult(url)
    links = parserLinks(html)
    count = 1
    for i in links:
        print("[{:^3}]{}".format(count,i))
        count +=1
main()
    
    

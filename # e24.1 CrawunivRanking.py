# e24.1 CrawunivRanking.py
import requests
from bs4 import BeautifulSoup
allUniv = []
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status ()
        r.encoding = "utf-8"
        return r.text
    except:
        return ""
def fillUnivList(soup):
    data = soup.find_all('tr')
    for tr in data:
        data1 = tr.find_all('td')
        if len(data1) == 0:
            continue
        singleUniv =[]
        for td in data1:
            singleUniv.append(td.string)
        allUniv.append(singleUniv)
def printUnivList(num):
    tplt = "{0:^5}\t{1:{5}^10}\t{2:^10}\t{3:^10}\t{4:^10}"
    print(tplt.format("排名","学校名称","省市","总分","规模",chr(12288)))
    for i in range(num):
        u = allUniv[i]
        print(tplt.format(u[0],u[1],u[2],u[3],u[4],chr(12288)))
def main():
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html =getHTMLText(url)
    soup = BeautifulSoup(html,"html.parser")
    fillUnivList(soup)
    n = eval(input('请输入想要的大学排名总数'))
    printUnivList(n)
main()
    
    
        

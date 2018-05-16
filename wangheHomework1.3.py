import requests
from bs4 import BeautifulSoup
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print('shibai')

def getHotelInfoList(url,InfoList):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, 'html.parser')

    a = soup.find_all('a',attrs={'target':"_blank" , 'class':"resule_img_a"})
    #print(a)
    for i in a:
        b = i.get('href')
        InfoList.append(b)
    return InfoList

def getHotelDetailS(InfoList):
    for i in InfoList:
        html = getHTMLText(i)
        soup = BeautifulSoup(html,'html.parser')
        title = soup.find('div',attrs={'class':'pho_info'}).find('em').string
        address = soup.find('span', attrs = {'class':'pr5'})
        dayprice = soup.find('span',attrs = {'class':'detail_avgprice'})
        hotel_img = soup.find('img',id='curBigImage')
        landlord_img = soup.find_all('img',alt='')[-1]
        landlord_name = soup.find('a',attrs={'class':'lorder_name'})
        div = soup.find('div',attrs={'class':'js_box clearfix'})
        div  = div.find_all('div')[1]
        div = div.get('class')[0]# 属性class可能有多个值，所以get 'class' 结果是一个列表 一定要加[0]
        #print(div)
        '''if div == 'member_ico':
            a = 'man'
        elif div == 'member_ico1':
            a = 'woman'
        else :
            a = ''
            print('') '''

        InfoDict = { 'title':title.string,
                     'address':address.string[0:15],
                     'dayprice':dayprice.string,
                     'hotel_img':hotel_img.get('src'),
                     'landlord_img':landlord_img.get('src'),
                     'landlord_name':landlord_name.string,
                     'sex': landlord_sex(div)}
        with open('C://Users/王贺/Desktop/HotelInfo.txt','a') as f:
            try:
                f.write(str(InfoDict))
                f.write('\n\n\n')
                f.close()
                print(InfoDict)
            except:
                print()

def landlord_sex(div):
    #print(div)
    if div == 'member_ico':
        return '男'
    elif div == 'member_ico1':
        return '女'
    else:
        return '不详'

def main():
    # start_url = 'http://xa.xiaozhu.com'
    urls = ['http://xa.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(1,2,1)]
    print(urls)

    for url in urls:
        HotelInfoList = []
        getHotelInfoList(url,HotelInfoList)
        getHotelDetailS(HotelInfoList )


main()

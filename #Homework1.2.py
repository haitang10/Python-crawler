from bs4 import BeautifulSoup
# allInfo = []
def getInfo(soup):
    data = soup.find_all('div', attrs={'class': 'thumbnail'})# data 列表的每一个元素含有每个商品的全部信息
    for goods in data: #对每个元素进行遍历，提取元素的各种信息
        infoDict = {} # 设置空字典存放每个商品的键值对
        images = goods.find('img')
        prices = goods.find('h4', attrs={'class': 'pull-right'})
        titles = goods.find('a')
        reviews = goods.find('p', attrs={'class': 'pull-right'})
        grades = goods.find_all('span') #星级评价在不在一个标签里，所以要建立列表存放含有星级的标签
        # print(grades)
        gradeList = [] # 用★和☆替换span标签中的文本，并将其存放于列表中
        for i in grades:
            a = i.attrs['class'][1] # 获取字符串
            if a == 'glyphicon-star':    # 判断是★还是☆
                b = a.replace('glyphicon-star', '★')   #替换
            elif a == 'glyphicon-star-empty':
                b = a.replace('glyphicon-star-empty', '☆')
            gradeList.append(b)
            # print(b,end= '')
        # print(gradeList )
        infoDict['title'] = titles.string   #向字典中增加各种信息
        infoDict['img'] = images.attrs['src']
        infoDict['price'] = prices.string
        infoDict['reviews'] = reviews.string

        c = ''              #将gradeList中的每个y元素组成字符串
        for i in gradeList:
            c = c + i
        # print(c)
        infoDict['grade'] = c
        print(infoDict, '\n')
        #allInfo.append(str(infoDict ))
        with open('C://Users/王贺/Desktop/goodsInfo.txt','a') as g:  # 将信息写入文件
            g.write(str(infoDict) )
            g.write('\n\n')
            g.close()
def main():
    with open("C://Users/王贺/Desktop/index.html",'r') as f :
        soup = BeautifulSoup(f, 'html.parser')
        getInfo(soup)
main()













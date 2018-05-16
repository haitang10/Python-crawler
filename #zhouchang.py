import math

def square(x):
    y = x * x
    return y
def distance(x1,x2,y1,y2):
    distance = math.sqrt(square(x1-x2) + square(y1-y2))
    return distance
def isTriangle(x1,x2,x3,y1,y2,y3):
    flag = ((x1-x2)*(y3-y2)-(x3-x2)*(y1-y2)) != 0
    return flag
    
def main():
    print("请输入三个点半的坐标")
    # 获取三个坐标点
    x1,y1 = eval(input("point1:(x,y) ="))
    x2,y2 = eval(input('point2:(x,y) ='))
    x3,y3 = eval(input('point2:(x,y) ='))
    # 判断是否为三角形
    if (isTriangle(x1,x2,x3,y1,y2,y3)):
        #计算三角形周长
        s = distance(x1,x2,y1,y2) + distance(x1,x3,y1,y3) + distance(x2,y2,x3,y3)
        print("周长为",s)
    else:
        print("Are you kidding me?")
        
main() 

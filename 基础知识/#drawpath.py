import turtle 

def main():

    # 设置窗口信息
    turtle.title("数据驱动的动态路径绘制")
    turtle.setup(800,600,0,0)
    # 设置画笔
    p= turtle.Turtle()
    p.color("red")
    p.width(5)
    p.shape("turtle")
    p.speed(5)
    # 读取文件
    result = []
    file = open("D:\data.txt","r")
    for line in file:
        result.append(list(map(float,line.split(','))))
    print(result)
    # 动态绘制
    for i in range (len(result)):
        p.color((result[i][3],result[i][4],result[i][5]))
        p.forward(result[i][0])
        if result[i][1]:
            p.rt(result[i][2])
        else:
            p.lt(result[i][2])
    p.goto(0,0)
    
if __name__ =='__main__':
    main()


    

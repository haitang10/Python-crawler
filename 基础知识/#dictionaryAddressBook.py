file1 = open('D:\Python\EmailAddressBook.txt','rb')
file2 = open("D:\Python\TeleAddressBook.txt","rb")

print(file1.readline()) #跳过第一行
file2.readline()
lines1 = file1.readlines()#lines为列表，line为字符串，data为列表
lines2 = file2.readlines()
print(lines2)
print(lines1)
# 建立空字典
dic1 = {}
dic2 = {}
for line in lines1:
    data = line.split()
    print(data)
    dic1[str(data[0].decode('gbk'))] = str(data[1].decode('gbk'))
for line in lines2:
    data = line.split()
    dic2[str(data[0].decode('gbk'))] = str(data[1].decode('gbk'))

lines3=[]
lines3.append('姓名\t 邮箱\t 电话 \n')
# 开始处理
for key in dic1:
    s = ''
    if key in dic2:
        s = '\t'.join([key,dic1[key],dic2[key]])
        s += '\n'
    else:
        s = '\t'.join([key,dic1[key],str('------')])
        s += '\n'
    lines3.append(s)
for key in dic2:
    s = ''
    if key not in dic1:
        s = '\t'.join([key,"-----",dic2[key]])
        s += '\n'
    lines3.append(s)

file3 = open('D:\Python\AddressBook.txt','w')
file3.writelines(lines3)

file1.close()
file2.close()
file3.close()
print('搞定了！')

'''第一步 打开文件 读取文件
   第二步 分别获取两个文件中的信息到列表1和列表2
   第三步 建立合并信息的空列表3
   第四步 生成信息表头，遍历列表1的人，加入到list3,list2剩余信息加入list3
   第五步 将list3写入文件3 ，关闭所有文件'''

file1 = open("D:\Python\EmailAddressBook.txt","rb")
file2 = open("D:\Python\TeleAddressBook.txt","rb")

file1.readline() #跳过第一行
file2.readline()
lines1 = file1.readlines()#lines为列表，line为字符串，data为列表
lines2 = file2.readlines()
# 建立空列表
list1_name = []
list1_email = []
list2_name = []
list2_tele = []
# 获取EmailAddressBook 中的人名，邮箱到两个列表
for line in lines1:
    data = line.split()
    list1_name.append(str(data[0].decode('gbk')))
    list1_email.append(str(data[1].decode('gbk')))
#获取TeleAddressBook中人名，电话到两个列表
for line in lines2:
    data = line.split()
    list2_name.append(str(data[0].decode('gbk')))
    list2_tele.append(str(data[1].decode('gbk')))
lines3 = []
lines3.append("姓名\t   邮箱\t \t电话\n")#建立空列表3并生成表头
#按索引方式遍历list1_name
for i in range(len(list1_name)):
    s = ''
    if list1_name[i] in list2_name:
        j = list2_name.index(list1_name[i])#找到list2中与list1中名字相同的位置
        s = '\t'.join([list1_name[i],list1_email[i],list2_tele[j]])
        s += '\n'
    else:
        s = '\t'.join([list1_name[i],list1_email[i],('------')])
        s += '\n'
    lines3.append(s)
#处理list2中的姓名
for i in range(len(list2_name)):
    s = ''
    if list2_name[i] not in list1_name:
        s = '\t'.join([list2_name[i],'------',list2_tele[i]])
        s += '\n'
    lines3.append(s)
file3 = open('D:\Python\AddressBook.txt','w')
file3.writelines(lines3)

file1.close()
file2.close()
file3.close()
print('搞定了！')

        

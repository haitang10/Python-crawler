file1 = open("D:\Python\EmailAddressBook.txt","r")
file2 = open("D:\Python\TeleAddressBook.txt","r")

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
    print(line)
    data = line.split()
    print(data)

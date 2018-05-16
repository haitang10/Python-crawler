file1 = open("D:\Python\EmailAddressBook.txt","rb")
file2 = open("D:\Python\TeleAddressBook.txt","rb")

file1.readline() #跳过第一行
file2.readline()
lines1 = file1.readlines()#lines为列表，line为字符串，data为列表
lines2 = file2.readlines()
print(lines1)
for line in lines1:
  print(line)
  data = line.split()
  print(data)
  print(data[0])

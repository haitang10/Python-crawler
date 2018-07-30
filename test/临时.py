fo = open("D:\Python\AddressBook.txt","r")
list1= []
for line in fo:
    line = line.replace("\n",",")
    
    list1 = line.split(",")
    
    ls = ""
    for s in list1:
        ls += s + "\t"
    print(ls)
fo.colose()

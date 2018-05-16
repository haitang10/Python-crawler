def gettext():
    file = open('D:\Python\hamlet.txt','r')
    text = file.read()
    text = text.lower()
    for ch in '~!@#$%^&*()<>,./?=-+_':
        text = text.replace(ch,'')
    return text
hamletTxt = gettext()
words = hamletTxt.split()
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
items = list(counts.items())

items.sort(key1 = lambda x: x[1],reverse = True)
for i in range (10):
    word,count = items[i]
    print('{0:<10}{1:>10}\n'.format(word,count))

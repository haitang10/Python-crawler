import requests
try:
    r = requests.get("http://python123.io/ws/demo.html")
    r.raise_for_status()
    r.encoding = 'utf-8'
    demo = r.text
    print(demo)
except:
    print("shibai ")

from urllib.parse import urlencode
import requests
import time
import re
import json
def qr():
    h={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'}
    r=requests.get('https://passport.bilibili.com/x/passport-login/web/qrcode/generate',headers=h)
    print(r.text)
    f=r.text
    f=re.search(r'({.*})',f).group(0)
    j=json.loads(f)
    curli = str(j['data']["url"])
    ll=str(j['data']['qrcode_key'])
    vep={'qrcode_key':ll}
    l ={'url':curli}
    curll= urlencode(l)
    jpgg=requests.get('https://api.pwmqr.com/qrcode/create/',params=curll)
    f=open('ddd.jpg','wb+')
    f.write(jpgg.content)
    f.close()
    print(j['data']["url"])

    while True:
        sq=requests.get('https://passport.bilibili.com/x/passport-login/web/qrcode/poll',params=vep,headers=h)
        sqq=re.search(r'({.*})',sq.text).group(0)
        sqqj=json.loads(sqq)
        if sqqj['data']['code']==0:
            print('完成')
            return sq.cookies
        else :
            print(sqqj['data']['code'])
            time.sleep(2.5)


from bs4 import BeautifulSoup
import requests
import shutil,os
url=r""
dest=r""
data=requests.get(url).text
if data:
    soup=BeautifulSoup(data,"html.parser")
    for img in soup.find_all('img'):
        src=(img['src'])
        if src: 
            print(src[:2])
            path=src.split(r"/")[-1]
            path=(os.path.join(dest,path))
            if "/" == src[:1]:
                src=url+src
            r= requests.get(src, stream=True)
            if r.status_code == 200:
                with open(path, 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)    
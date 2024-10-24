from bs4 import BeautifulSoup
import requests
url="https://www.delfi.ee/viimased"
page=requests.get(url)
soup=BeautifulSoup(page.content,"html.parser")
pealkirjad=soup.find_all("h5")
count=0
for pealkiri in pealkirjad:
    if count==3:
        break
    link=pealkiri.find("a",href=True)
    if link:
        title=link.text
        href=link["href"]
        print(f'Title: {title}\nLink: {href}\n')
    count+=1

    

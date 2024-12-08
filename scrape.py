################################################
# Programmeerimine I
# 2024/2025 sügissemester
#
# Projekt
# Teema: Uudistekanalite web scrape
#
#
# Autorid: Gregor Uustalu, Kaspar Veere
#
#
# Lisakommentaar (nt käivitusjuhend):
#     pip install beautifulsoup4
##################################################
import os
from bs4 import BeautifulSoup
import requests
templates_kaust = "templates"
def delfi():  #delfi scrape
    url="https://www.delfi.ee"
    page=requests.get(url)
    soup=BeautifulSoup(page.content,"html.parser") 
    pealkirjad=soup.find_all("h5") # Leiab kõik uudiste pealkirjad
    count=0
    uudis=[]
    for pealkiri in pealkirjad: # lisab sõnastikku kõik pealkirjad ja nende lingid
        if count==10: # võtab ainult 10 esimest uudist
            break
        link=pealkiri.find("a",href=True)
        if link:
            title=link.text.strip()
            href=link["href"]
            uudis.append({"title": title, "href": href, "source": "Delfi"})
        count+=1
    return uudis
def ohtuleht():  #Õhtuleht scrape
    url="https://www.ohtuleht.ee/"
    page=requests.get(url)
    soup=BeautifulSoup(page.content,"html.parser")
    pealkirjad=soup.find_all("h6") # Leiab kõik uudiste pealkirjad
    count=0
    uudis=[]
    for pealkiri in pealkirjad: # lisab sõnastikku kõik pealkirjad ja nende lingid
        if count==10: # võtab ainult 10 esimest uudist
            break
        link=pealkiri.find("a",href=True)
        if link:
            title=link.text.strip()
            href=link["href"]
            if not href.startswith("http"): # Õhtuleht ei andnud täielikke linke, seega pidi "https://www.ohtuleht.ee/" selle ette lisama
                href=url+href
            uudis.append({"title": title, "href": href, "source": "Õhtuleht"})
        count+=1
    return uudis

def generate_html(filename, title, uudised): # kirjutab uudiseallika jaoks vahelehe
    content = f"""<!DOCTYPE html>
<html lang="et">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css" />

    <title>{title}</title>
</head>
<body>
    <h1>{title}</h1>
    <ul>
"""
    for item in uudised:  # lisab uudised lehele
        content += "<li>\n"
        content += f'    <a href="{item["href"]}" target="_blank">{item["title"]}</a>\n'
        content += "</li>\n"
    
    content += """    </ul>
</body>
</html>"""

    f=open(filename,"w", encoding="utf-8") # loob faili ja kirjutab htmli koos uudistega
    f.write(content)
    f.close()

def generate_main(): # loob pealehe
    content = """<!DOCTYPE html>
<html lang="et">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ajalehed</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            text-align: center;
            border: 2px solid #333;
            padding: 20px;
            width: 300px;
            background-color: #fff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        h1 {
            font-size: 24px;
            margin-bottom: 20px;
        }
        .links a {
            display: block;
            font-size: 18px;
            margin: 10px 0;
            color: #007bff;
            text-decoration: none;
            transition: color 0.3s;
        }
        .links a:hover {
            color: #0056b3;
        }
        hr {
            border: none;
            height: 2px;
            background-color: #333;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Ajalehed</h1>
    <hr>
    <div class="links">
        <a href="ohtuleht.html" target="_blank">Õhtuleht</a>
        <a href="delfi.html" target="_blank">Delfi</a>
    </div>
</div>

</body>
</html>
"""
    f=open("main.html","w", encoding="utf-8") #loob faili ja kirjutab htmli
    f.write(content)
    f.close()


if __name__ == "__main__":
    delfi_uudised = delfi()
    ohtuleht_uudised = ohtuleht()

    generate_html("delfi.html", "Delfi Uudised", delfi_uudised)
    generate_html("ohtuleht.html", "Õhtuleht Uudised", ohtuleht_uudised)
    generate_main()

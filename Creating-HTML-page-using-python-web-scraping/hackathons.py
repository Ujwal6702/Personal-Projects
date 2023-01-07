from re import L
from bs4 import BeautifulSoup as bs
from urllib.request import Request as rs, urlopen
import pandas as pd
import requests 

def startbody():
    return "<body>"

def endbody():
    return "</body>"

def startrow():
    return "<div class=\"row\">"
def endrow():
    return "</div>"
def htmlcode(a,b,c,d):
    return "<div class=\"column\"><div class=\"card\"><img src=\""+b+"\" alt=\""+a+"\" style=\"width:100%\"><div class=\"container\"><h2>"+a+"</h2><p class=\"title\">"+c+"</p><p><button class=\"button\" onclick=\"location.href=\'"+d+"\'\">"+a+"</button></p></div></div></div>"

site = "https://www.hackerearth.com/challenges/?filters=competitive%2Chackathon%2Chiring"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = rs(site, headers=hdr)
page = urlopen(req)
hackerearth = bs(page, "html.parser")

list_of_names=[]
list_of_links=[]
list_of_types=[]
list_of_src_of_images=[]

for links in hackerearth.find_all("div", class_="challenge-card-modern"):
    try:
        name=links.find("div", class_="challenge-name ellipsis dark").span.text
        page=links.find("a").get("href")
        img=str(links.find("div", class_="event-image").get("style"))
        img=img.replace("background-image: url('","")
        img=img.replace("');","")
        type=links.find("div", class_="challenge-type light smaller caps weight-600").text
        list_of_names.append(name)
        list_of_links.append(page)
        list_of_types.append(type)
        list_of_src_of_images.append(img)
    except:
        continue

with open('J:\My Drive\The Geek Squad\C UJWAL\copy.html','r') as firstfile, open('J:\My Drive\The Geek Squad\siri\KODIKON\hackathon.html','w') as secondfile:  
    for line in firstfile:      
        secondfile.write(line)
firstfile.close()
secondfile.close()

file=open("J:\My Drive\The Geek Squad\siri\KODIKON\hackathon.html", "a")
file.write(startbody())
for i in range(len(list_of_names)):
    if i%3==0:
        file.write(htmlcode(list_of_names[i], list_of_src_of_images[i],list_of_types[i], list_of_links[i]))
        file.write(endrow())
    elif i%3==1:
        file.write(startrow())
        file.write(htmlcode(list_of_names[i], list_of_src_of_images[i],list_of_types[i], list_of_links[i]))
    else:
        file.write(htmlcode(list_of_names[i], list_of_src_of_images[i],list_of_types[i], list_of_links[i]))
file.write(endrow())
file.write(endbody())
file.write("</html>")
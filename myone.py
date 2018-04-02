from bs4 import BeautifulSoup
from urllib import request
import re




def GetAll():
    word = "self"
    url = "http://www.iciba.com/"+word
    header = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
    }
    req = request.Request(url=url, headers=header)
    html = request.urlopen(req)
    bs = BeautifulSoup(html, "html.parser")
    liju = bs.find("div",{"class":"container-left"}).find("div",{"class":"js-main-content"}).find("div",{"class":"info-article.article-tab"})
    for tmp in liju:
        print(tmp.text)
    print("end")

GetAll()
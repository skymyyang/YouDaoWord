#-*- coding:utf-8 -*-
from mysqlciyuan import insert
from lxml import etree
import requests
import urllib
import chardet

class cysf():
    def __init__(self):
        self.word = ""
        self.ciyuan = ""
        self.jiyifangfa = ""


    def work_spider(self):
        url = "http://www.youdict.com/w/"+self.word
        header = {'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0'}
        r = requests.get(url,header)
        req = r.content
        print(type(req))
        sel = etree.HTML(str(req, "utf-8"))
        jiyifangfa = []
        for i in sel.xpath('//*[@id="yd-content"]/div[3]/text()'):
            print(i.encode("utf-8"))
            jiyifangfa.append(count.decode("utf-8"))
            self.jiyifangfa = "".join(jiyifangfa)



        for i in sel.xpath('//*[@id="yd-ciyuan"]/p'):
            count = i.text
            ciyuan = count.encode("utf-8")
            self.ciyuan = str(ciyuan,"utf-8")
        print(self.jiyifangfa)
        print(self.ciyuan)



        # req = request.Request(url=url, headers=header)
        # # try:
        # #     req.selector.encode('ascii')
        # # except UnicodeEncodeError:
        # #     req.selector = quote(req.selector)
        # html = request.urlopen(req)
        # bs = BeautifulSoup(html, "html.parser")
        # try:
        #     # ciyuantitle = bs.findAll("span",{"class":"ciyuan-title"})
        #     ciyuansiyi = bs.find("div", {"id" : "yd-ciyuan"}).findAll("p")
        #     # for i in ciyuantitle:
        #     #     cytitle = i.text
        #     #     # print(cytitle)
        #     # print(ciyuansiyi)
        #     for i in ciyuansiyi:
        #         cysiyi = i.text
        #         # print(cysiyi)
        #         # self.ciyuan = cytitle + "\n" + cysiyi
        #         # print(cysiyi)
        #         self.ciyuan = cysiyi.encode("utf8")
        #         # print(self.ciyuan)
        #
        #
        #
        # except:
        #     print("no have ciyuan")  overuse  obese   impressionable





        # try:
        #     jyfangfa = bs.findAll("div",{"style":"font-family:SimSun,serif;"})
        #     for i in jyfangfa:
        #         self.jiyifangfa = i.text
        #         print(self.jiyifangfa)[1]
        #         self.jiyifangfa = self.jiyifangfa.encode("utf8")
        # except:
        #     print("no have jiyifangfa")


a = cysf()
a.word = "accompany"
a.work_spider()
# print(type(a.word),type(a.ciyuan),type(a.jiyifangfa))

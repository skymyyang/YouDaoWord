#encoding=utf-8
from urllib import error,request
from bs4 import BeautifulSoup
from urllib.parse import quote
from http.client import BadStatusLine


class YouDaoSpider(object):
    """有道爬虫"""
    word=""
    yingshiyinbiao=""
    meishiyinbiao=""
    yingshifayin=""
    meishifayin=""
    cixingshiyi=[]
    cizu={}
    liju={}
    xiangguancihui={}
    def __init__(self, **kwargs):
        self.word=""
        self.meishifayin=""
        self.yingshifayin=""
        self.meishiyinbiao=""
        self.yingshiyinbiao=""
        self.cixingshiyi=[]
        self.cizu={}
        self.liju={}
        self.xiangguancihui={}

    def workSpider(self):
        url="http://dict.youdao.com/w/"+self.word+"/#keyfrom=dict2.top"
        yingurl="http://dict.youdao.com/dictvoice?audio="+self.word+"&type=1"
        meiurl="http://dict.youdao.com/dictvoice?audio="+self.word+"&type=2"
        header = {
        'Host': r'dict.youdao.com',
        'Connection': 'keep-alive',
        # 'Accept-Encoding': r'gzip, deflate, sdch',
        # "Referer":"http://dict.youdao.com/",
        # "Content-length":19158,
        'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',}
        # req = request.Request(url, headers=header)
        req = request.Request(url, headers=header)
        try:
            req.selector.encode('ascii')
        except UnicodeEncodeError:
            req.selector = quote(req.selector)

        # try:
        #     htmltest=request.urlopen(req)
        # except BadStatusLine as e:
        #     print(e)
        htmltest = request.urlopen(req)
        bs=BeautifulSoup(htmltest, "html.parser")
        #获取音标
        try:
            yinbiao=bs.findAll("span",{"class":"pronounce"})
            for tmp in yinbiao:
                    if("英" in tmp.text):
                        self.yingshiyinbiao=tmp.find("span",{"class":"phonetic"}).text
                    else:
                        self.meishiyinbiao=tmp.find("span",{"class":"phonetic"}).text
        except:
            print("no have yinbiao")
        #获取词性解释
        try:
            jieshi=bs.find("div",{"class":"trans-container"}).find("ul").findAll("li")
            for tmp in jieshi:
                self.cixingshiyi.append("{"+tmp.text.split('.')[0]+":"+tmp.text.replace(tmp.text.split('.')[0]+".",'')+"}")
        except:
            print("no have cixingjieshi")
        #获取词组
        try:
            cizuhtml=bs.find("div",{"id":"wordGroup"}).findAll("p",{"class":"wordGroup"})
            for tmp in cizuhtml:
                self.cizu.setdefault(tmp.text.strip().splitlines()[0].strip(),tmp.text.strip().splitlines()[1].strip())
        except:
            print("no have cizu")
        #获取同义词
        try:
            tongyici=bs.find("div",{"id":"synonyms"}).ul.findAll("li")
            for tmp in tongyici:
                engwords=""
                citmp=tmp.next_sibling.next_sibling.findAll("span",{"class":"contentTitle"})
                for citmptmp in citmp:
                    engwords=engwords+citmptmp.find("a",{"class":"search-js"}).text+","
                self.xiangguancihui.setdefault(tmp.text.split('.')[0],engwords)
        except:
            print("no have tongyici")
        #获取例句
        try:
            lijutmp=bs.find("div",{"id":"bilingual"}).ul.findAll("li")
            for tmp in lijutmp:
                self.liju.setdefault(tmp.p.text,tmp.p.next_sibling.next_sibling.text)
        except:
            print("no have liju")
        #获取发音音频
        try:
            data=request.urlopen(yingurl).read()
            with open("voice\\"+self.word+"ying.mp3","wb") as file:
                 file.write(data)
            self.yingshifayin="/voice/"+self.word+"ying.mp3"
            data=request.urlopen(meiurl).read()
            with open("voice\\"+self.word+"mei.mp3","wb") as file:
                 file.write(data)
            self.meishifayin="/voice/"+self.word+"mei.mp3"
        except:
            print("no have fayinyinpin")
        return self
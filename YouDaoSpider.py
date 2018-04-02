#coding:utf8
from urllib import error,request
from bs4 import BeautifulSoup
from urllib.parse import quote
from http.client import BadStatusLine
import time
import requests
#"http://youdao.com/w/eng/ch%C3%A2teau/#keyfrom=dict2.index"
#"http://youdao.com/w/f%C3%AAte/#keyfrom=dict2.top"
# http://youdao.com/w/eng/vis-%C3%A0-vis/#keyfrom=dict2.index
# http://youdao.com/w/eng/El%20Ni%C3%B1o/#keyfrom=dict2.index

import re


class YouDaoSpider(object):
    """有道爬虫"""
    word = ""
    yingshiyinbiao = ""
    meishiyinbiao = ""
    yingshifayin = ""
    meishifayin = ""
    cixingshiyi = []
    cizu = {}
    liju = {}
    xiangguancihui = {}
    def __init__(self, **kwargs):
        self.word = ""
        self.meishifayin = ""
        self.yingshifayin = ""
        self.meishiyinbiao = ""
        self.yingshiyinbiao = ""
        self.cixingshiyi = []
        self.cizu = {}
        self.liju = {}
        self.xiangguancihui = {}

    def workSpider(self):
        url = "http://dict.youdao.com/w/"+self.word.replace('é','%C3%A9').replace('ï','%C3%AF').replace('â', '%C3%A2').replace('ê', '%C3%AA').replace('à', '%C3%A0').replace('ñ', '%C3%B1').replace(" ", "%20")+"/#keyfrom=dict2.top"
        urllower = "http://dict.youdao.com/w/"+self.word.replace('é','%C3%A9').replace('ï','%C3%AF').replace('â', '%C3%A2').replace('ê', '%C3%AA').replace('à', '%C3%A0').replace('ñ', '%C3%B1').replace(" ", "%20").lower()+"/#keyfrom=dict2.top"
        yingurl = "http://dict.youdao.com/dictvoice?audio="+self.word.replace('é','%C3%A9').replace('ï','%C3%AF').replace('â', '%C3%A2').replace('ê', '%C3%AA').replace('à', '%C3%A0').replace('ñ', '%C3%B1').replace(" ", "%20")+"&type=1"
        yingurllower = "http://dict.youdao.com/dictvoice?audio="+self.word.replace('é','%C3%A9').replace('ï','%C3%AF').replace('â', '%C3%A2').replace('ê', '%C3%AA').replace('à', '%C3%A0').replace('ñ', '%C3%B1').replace(' ', '+').replace(" ", "%20").lower()+"&type=1"
        meiurl = "http://dict.youdao.com/dictvoice?audio="+self.word.replace('é','%C3%A9').replace('ï','%C3%AF').replace('â', '%C3%A2').replace('ê', '%C3%AA').replace('à', '%C3%A0').replace('ñ', '%C3%B1').replace(" ", "%20")+"&type=2"
        meiurllower = "http://dict.youdao.com/dictvoice?audio="+self.word.replace('é','%C3%A9').replace('ï','%C3%AF').replace('â', '%C3%A2').replace('ê', '%C3%AA').replace('à', '%C3%A0').replace('ñ', '%C3%B1').replace(' ', '+').replace(" ", "%20").lower()+"&type=2"
        #处理单词和短语之中出现空格和特殊字符，从而导致爬取的mp3文件无法保存
        wordyp = re.findall('[a-zA-Z0-9" "éïâàñê]+', self.word)
        wordyp2 = ''.join(wordyp)
        wordyp2 = wordyp2.replace('é','-').replace('ï','-').replace('â', '-').replace('à', '-').replace('ñ', '-').replace('ê', '-')
        print(url)
        header = {
            'Host': r'dict.youdao.com',
            'Connection': 'keep-alive',
            'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            }
        req = request.Request(url, headers=header)
        #解决短语因ascii的问题无法正常爬取
        try:
            req.selector.encode('ascii')
        except UnicodeEncodeError:
            req.selector = quote(req.selector)
        #解决部分短语因为首字母大写而无法获取网页内容，将其改为小写
        try:
            htmltest = request.urlopen(req)
        except error.HTTPError as e:
            print(self.word + "-" + str(e))
            print(type(e.code))
            if e.code == 400:
                res = request.Request(url, headers=header)
                print(res)
                htmltest = request.urlopen(res)
            else:
                time.sleep(1)
                htmltest = request.urlopen(req)
        except BadStatusLine as e:
            print(self.word + "-" + str(e))
            req2 = request.Request(urllower, headers=header)
            htmltest = request.urlopen(req2)
        # except error.HTTPError as e:
        #     print(self.word + "-" + str(e))
        #     time.sleep(1)
        #     htmltest = request.urlopen(req)
        bs = BeautifulSoup(htmltest, "html.parser")
        #获取音标
        try:
            yinbiao = bs.findAll("span",{"class":"pronounce"})
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
                self.cixingshiyi.append("{"+tmp.text.split('.')[0].strip()+":"+tmp.text.replace(tmp.text.split('.')[0]+".",'').strip()+"}")
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
                if tmp.p.text.strip() != "":
                    self.liju.setdefault(tmp.p.text.strip(),tmp.p.next_sibling.next_sibling.text.strip())




        except:
            print("no have liju")
        #获取发音音频
        try:
            data=request.urlopen(yingurl).read()
            with open("voice\\"+wordyp2+"ying.mp3","wb") as file:
                 file.write(data)
            self.yingshifayin="/voice/"+wordyp2+"ying.mp3"
            data=request.urlopen(meiurl).read()
            with open("voice\\"+wordyp2+"mei.mp3","wb") as file:
                 file.write(data)
            self.meishifayin="/voice/"+wordyp2+"mei.mp3"
        except BadStatusLine as e:
            print(self.word + "-" + str(e))
            data=request.urlopen(yingurllower).read()
            with open("voice\\"+wordyp2+"ying.mp3","wb") as file:
                file.write(data)
            self.yingshifayin="/voice/"+wordyp2+"ying.mp3"
            data=request.urlopen(meiurllower).read()
            with open("voice\\"+wordyp2+"mei.mp3","wb") as file:
                file.write(data)
            self.meishifayin="/voice/"+wordyp2+"mei.mp3"


            # try:
            #     data=request.urlopen(yingurllower).read()
            #     with open("voice\\"+wordyp2+"ying.mp3","wb") as file:
            #          file.write(data)
            #     self.yingshifayin="/voice/"+wordyp2+"ying.mp3"
            #     data=request.urlopen(meiurllower).read()
            #     with open("voice\\"+wordyp2+"mei.mp3","wb") as file:
            #          file.write(data)
            #     self.meishifayin="/voice/"+wordyp2+"mei.mp3"
            # except UnboundLocalError as e:
            #     data=request.urlopen(yingurllower).read()
            #     with open("voice\\"+self.word+"ying.mp3","wb") as file:
            #          file.write(data)
            #     self.yingshifayin="/voice/"+self.word+"ying.mp3"
            #     data=request.urlopen(meiurllower).read()
            #     with open("voice\\"+self.word+"mei.mp3","wb") as file:
            #          file.write(data)
            #     self.meishifayin="/voice/"+self.word+"mei.mp3"


        print("no have fayinyinpin")
        return self

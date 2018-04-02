# from YouDaoSpider import YouDaoSpider
# from MysqlHelper import MysqlHelper
#
#
# foo = YouDaoSpider()
# foo.word = "the Hanging Gardens"
# tmpExample=foo.workSpider()
# MysqlHelper.insert(tmpExample.word,tmpExample.meishiyinbiao,tmpExample.yingshiyinbiao,tmpExample.cixingshiyi,tmpExample.cizu,tmpExample.liju,tmpExample.xiangguancihui,tmpExample.meishifayin,tmpExample.yingshifayin)

from urllib import request,error
word = "the Hanging Gardens"
word = word.replace(" ", "%20")
url = "http://dict.youdao.com/w/"+word+"#keyfrom=dict2.top"
req = request.Request(url)
print(req)
htmltest = request.urlopen(req)
print(htmltest)

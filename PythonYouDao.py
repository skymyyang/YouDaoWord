﻿
from YouDaoSpider import YouDaoSpider
import json
from MysqlHelper import MysqlHelper
from ReadExcel import ReadExcel





readExcel=ReadExcel()
words=readExcel.readsheet("dytest.xlsx")
print(len(words))
for tmp in words:
    example=YouDaoSpider()
    tmp = str(tmp)
    example.word=tmp.replace("",'').replace("",'').replace("）",'').replace("（",'').replace("…"," ").replace('’','\'').rstrip()
    print(example.word.encode("utf8"))
    print("------------------------start")
    tmpExample=example.workSpider()
    MysqlHelper.insert(tmpExample.word,tmpExample.meishiyinbiao,tmpExample.yingshiyinbiao,tmpExample.cixingshiyi,tmpExample.cizu,tmpExample.liju,tmpExample.xiangguancihui,tmpExample.meishifayin,tmpExample.yingshifayin)
    print(tmpExample.word.encode("utf8"))
    print("------------------------end")
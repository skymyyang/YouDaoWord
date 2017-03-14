#encoding=utf-8
import pymysql
import json

class MysqlHelper:
    """mysql 帮助类"""


    @staticmethod
    def insert(word,asymbol,esymbol,explain,cizu,liju,xiangguancihui,aspoken,espoken):
        db=pymysql.connect(host="mfgskymyyang.chinacloudapp.cn",user="skymyyang",password="666666",db="metest",charset="utf8")
        cursor=db.cursor()
        print(word.encode("utf8"))
        print("--------------------------------insert into mysql db")
        cursor.execute("insert into mfg_t_wordtest (f_word,f_asymbol,f_esymbol,f_explain,f_cizu,f_liju,f_xiangguancihui,f_aspoken,f_espoken,f_biaoji,f_type) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,0,0)",(word,asymbol,esymbol,"{"+json.dumps(explain,ensure_ascii=False,indent=2)+"}",json.dumps(cizu,ensure_ascii=False,indent=2),json.dumps(liju,ensure_ascii=False,indent=2),json.dumps(xiangguancihui,ensure_ascii=False,indent=2),aspoken,espoken))
        db.commit()
        db.close()

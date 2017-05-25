#encoding=utf-8
import pymysql
import json

def insert(word, ciyuan, jiyifangfa):
    db = pymysql.connect(host="192.168.180.187",user="root",password="123456",db="lytest",charset="utf8")
    cursor=db.cursor()
    # print(word.encode("utf8"))
    # print("--------------------------------insert into mysql db")
    cursor.execute("insert into mfg_ciyuan(f_word,f_ciyuan,f_jiyifangfa) values(%s, %s, %s)", (word, ciyuan, jiyifangfa))
    # json.dumps(ciyuan,ensure_ascii=False,indent=2),json.dumps(jiyifangfa,ensure_ascii=False,indent=2)
    db.commit()
    db.close()

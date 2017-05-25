from ciyuansuanfa import cysf
from ReadExcel import ReadExcel
from mysqlciyuan import insert



# a = cysf()
# a.word = "sm"
# a.work_spider()


readExcel=ReadExcel()
words=readExcel.readsheet("wordExcel\dy04.xlsx")
print(len(words))
for tmp in words:
    a = cysf()
    tmp = str(tmp)
    a.word = tmp.replace("",'').replace("",'').replace("）",'').replace("（",'').replace("…"," ").replace('’','\'').rstrip()
    print(a.word.encode("utf8"))
    print("------------------------start")
    a.work_spider()
    insert(a.word, a.ciyuan, a.jiyifangfa)
    print(a.word.encode("utf8"))
    print("------------------------end")

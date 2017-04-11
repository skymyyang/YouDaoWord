#coding:utf8
from xlrd import open_workbook
import re
import os


class ReadExcel:
    """读取Excel表"""
    def __init__(self):
        self.wordsurl=[]


    def readsheet(self,path):
        messageInfo=open_workbook(path) #打开Excel读取文件数据
        sheetInfo=messageInfo.sheets()[0] #通过索引顺序获取工作表
        row_index = 0
        while row_index < sheetInfo.nrows: #获取行数
            value=sheetInfo.cell(row_index,0).value
            self.wordsurl.append(sheetInfo.cell(row_index,0).value)
            row_index += 1
        return self.wordsurl

def findFile(wordsurl):
    for fileurl in wordsurl:
        filename = "/app"+fileurl
        #print(filename)
        if os.path.exists(filename):
            message = 'OK, the %s is exists'%(filename)
            with open("sucess.log", 'a') as f:
                f.write(message+'\n')
            #print(message)
        else:
            message = 'OK, the %s is not exists'%(filename)
            print(message)
            # message = message.encode('utf-8')
            with open('nofile.txt', 'a') as f:
                f.write(message+'\n')
a = ReadExcel()
wordsurl = a.readsheet("dcurl2.xlsx")
findFile(wordsurl)

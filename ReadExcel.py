from xlrd import open_workbook



class ReadExcel:
    """读取Excel表"""
    words=[]
    def readsheet(self,path):
        messageInfo=open_workbook(path)
        sheetInfo=messageInfo.sheets()[0]
        row_index = 0
        while row_index < sheetInfo.nrows:
            value=sheetInfo.cell(row_index,0).value
            self.words.append(sheetInfo.cell(row_index,0).value)
            row_index += 1
        return self.words



# class Readmp3url:
#     """读取MP3url"""
#     MP3url = []
#     def readsheet1(self, eclpath):

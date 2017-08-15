from urllib import error,request
from bs4 import BeautifulSoup
from urllib.parse import quote
from http.client import BadStatusLine
import re
#risqu%C3%A9
word = "risqué"
wordr = word.replace('é','%C3%A9')
print(wordr)
url = "http://dict.youdao.com/dictvoice?audio="+wordr+"&type=1"
print(url)
# word2 = "risqu%C3%A9"
# word3 = "naïve"
# url2 = "http://dict.youdao.com/dictvoice?audio=na%C3%AFve&type=1"
# url = "http://dict.youdao.com/dictvoice?audio="+word+"&type=1"
# url3 = "http://dict.youdao.com/dictvoice?audio=clich%C3%A9&type=1"
# print(url)
# data = request.urlopen(url)
# print(data)

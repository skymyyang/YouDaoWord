from urllib import error,request
from bs4 import BeautifulSoup
from urllib.parse import quote
from http.client import BadStatusLine
import re
#risqu%C3%A9
word = "risqué"
word2 = "risqu%C3%A9"
url = "http://dict.youdao.com/dictvoice?audio="+word2+"&type=1"
print(url)
data = request.urlopen(url)
print(data)

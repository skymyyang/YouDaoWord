from urllib import error,request
from bs4 import BeautifulSoup
from urllib.parse import quote
from http.client import BadStatusLine,HTTPConnection

def http_get(url, path, headers):
    conn = HTTPConnection(url, 80)
    print ('Connecting to ' + url)
    conn.request(url, path, headers)
    resp = conn.getresponse()
    if resp.status<=400:
        body = resp.read()
        print ('Reading Source...')

    if resp.status >= 400:
        print (url)
        raise ValueError('Response Error: %s, %s, URL: %s' % (resp.status, resp.reason,url))
    return body
def workSpider():
    url="http://dict.youdao.com/w/"+"the Opera House"+"/#keyfrom=dict2.top"
    yingurl="http://dict.youdao.com/dictvoice?audio="+"the Opera House"+"&type=1"
    meiurl="http://dict.youdao.com/dictvoice?audio="+"the Opera House"+"&type=2"
    path = '/'
    header = {"Host":"dict.youdao.com",
    # "Referer":"http://dict.youdao.com/",
    "Content-length":19158,
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
    a = http_get(url, path, headers=header)
    print(a)
    req = request.Request(url, headers=header)
    try:
        req.selector.encode('ascii')
    except UnicodeEncodeError:
        req.selector = quote(req.selector)

    try:
        htmltest=request.urlopen(req)
        print(htmltest.read())
    except BadStatusLine as e:
        #pass
        print(e)
        # htmltest = request.urlopen(req)
    # bs=BeautifulSoup(htmltest, "html.parser")

workSpider()

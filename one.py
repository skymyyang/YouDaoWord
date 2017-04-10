'''
cgi默认解析自己根目录下的index.html文件
cgi.FiledStorage()可以接受到client端请求上来的数据
get  http请求方式  属于明文请求，将请求的数据以键值对的形式附加到url后面
post http请求方式，但属于密文请求，不会在url上有所显示
get  用于我们向服务器提交数据以后获取响应数据
post 用户我们向服务器提交数据进行保存或校验
'''
import cgi
html = """


<html>
<head><title>
hello world

</title>
<body>
hello word this is cgi<br/>
%s is %s

</body>
</head>
</html>
"""
content = cgi.FieldStorage()
print("content-type: text/html")
print("\n")
print(html%content.getvalue("name"))

#!D:/Anaconda3/python.exe

# CGI处理模块
import os
import cgi
import cgitb

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage()

# 获取数据
site_name = form.getvalue('name')
site_url = form.getvalue('url')

# open('./data', 'a+').write(site_name)
# open('./data', 'a+').write(site_url)

# 打开文件
fo = open("./data", "a+")
fo.writelines(site_name)
fo.writelines("\n")
fo.writelines(site_url)
fo.writelines("\n")

# 关闭文件
fo.close()


print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<title>菜鸟教程 CGI 测试实例</title>")
print("</head>")
print("<body>")
print("<h2>%s官网：%s</h2>" % (site_name, site_url))
print("</body>")
print("</html>")

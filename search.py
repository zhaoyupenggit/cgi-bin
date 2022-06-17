#!D:/Anaconda3/python.exe
# coding:utf-8

# CGI处理模块
import os
import cgi
import cgitb
import string
import codecs
from sqlalchemy import null

form = cgi.FieldStorage()
site_name = form.getvalue('name')
# site_sex = form.getvalue('sex')
# site_age = form.getvalue('age')
# site_tel = form.getvalue('tel')


# 读取姓名文件，并将其转换为列表
fo = codecs.open("./data/name", "r", encoding="utf-8")
# print("文件名为: ", fo.name)
list_name = []
for line in fo.readlines():  # 依次读取每行
    line = line.strip()  # 去掉每行头尾空白
    list_name.append(line)
# print(list_name)
fo.close()

# 读取性别文件，并将其转换为列表
fo = codecs.open("./data/sex", "r", encoding="utf-8")
# print("文件名为: ", fo.name)
list_sex = []
for line in fo.readlines():  # 依次读取每行
    line = line.strip()  # 去掉每行头尾空白
    list_sex.append(line)
# print(list_sex)
fo.close()

# 读取年龄文件，并将其转换为列表
fo = codecs.open("./data/age", "r", encoding="utf-8")
# print("文件名为: ", fo.name)
list_age = []
for line in fo.readlines():  # 依次读取每行
    line = line.strip()  # 去掉每行头尾空白
    list_age.append(line)
# print(list_age)
fo.close()

# 读取电话文件，并将其转换为列表
fo = codecs.open("./data/tel", "r", encoding="utf-8")
# print("文件名为: ", fo.name)
list_tel = []
for line in fo.readlines():  # 依次读取每行
    line = line.strip()  # 去掉每行头尾空白
    list_tel.append(line)
# print(list_tel)
fo.close()


def search(site_name):
    if site_name in list_name:
        return list_name.index(site_name)
    else:
        return -1   # 没有找到


if search(site_name) != -1:
    Num = search(site_name)
    # 搜索结果
    search_name = list_name[Num]
    search_sex = list_sex[Num]
    search_age = list_age[Num]
    search_tel = list_tel[Num]
else:
    # 搜索结果
    search_name = 'null'
    search_sex = 'null'
    search_age = 'null'
    search_tel = 'null'

# print(Num)
# print(list_name[Num])
# print(list_sex[Num])
# print(list_age[Num])
# print(list_tel[Num])

# def create_list(value,List,fo):
#     for line in fo.readlines():  # 依次读取每行
#     line = line.strip()  # 去掉每行头尾空白
#     List.append(line)

print("Content-type:text/html\n\n")
print()
print("<html>")
print("<head>")
print("<title>Search</title>")
print("</head>")
print("<body>")
print("<h2>Search Result</h2>")
print("<p>Name: %s</p>" % (search_name))
print("<p>Sex: %s</p>" % (search_sex))
print("<p>Age: %s</p>" % (search_age))
print("<p>Tel: %s</p>" % (search_tel))
print('<p><a href="/index.html">back</a></p>')
print("</body>")
print("</html>")

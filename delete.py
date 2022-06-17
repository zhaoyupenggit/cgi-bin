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
# site_name = 'delete'

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
        return -1   # 没有找到 返回-1 但是不能使用False，因为False=0


if search(site_name) != -1:
    Num = search(site_name)
    # 被删除数据
    delete_name = list_name[Num]
    delete_sex = list_sex[Num]
    delete_age = list_age[Num]
    delete_tel = list_tel[Num]
    # 删除数据
    list_name.pop(Num)
    list_sex.pop(Num)
    list_age.pop(Num)
    list_tel.pop(Num)

    # 将修改后的数据写入姓名文件
    fo = codecs.open("./data/name", "w+", encoding="utf-8")
    # print("文件名为: ", fo.name)
    for line in list_name:
        fo.write(line+'\n')
    fo.close()

    # 将修改后的数据写入性别文件
    fo = codecs.open("./data/sex", "w+", encoding="utf-8")
    # print("文件名为: ", fo.name)
    for line in list_sex:
        fo.write(line+'\n')
    fo.close()

    # 将修改后的数据写入年龄文件
    fo = codecs.open("./data/age", "w+", encoding="utf-8")
    # print("文件名为: ", fo.name)
    for line in list_age:
        fo.write(line+'\n')
    fo.close()

    # 将修改后的数据写入电话文件
    fo = codecs.open("./data/tel", "w+", encoding="utf-8")
    # print("文件名为: ", fo.name)
    for line in list_tel:
        fo.write(line+'\n')
    fo.close()

else:
    # 被删除数据
    delete_name = 'null'
    delete_sex = 'null'
    delete_age = 'null'
    delete_tel = 'null'

print("Content-type:text/html\n\n")
print()
print("<html>")
print("<head>")
print("<title>Delete</title>")
print("</head>")
print("<body>")
print("<h2>Have Deleted</h2>")
print("<p>DeleteName: %s</p>" % (delete_name))
print("<p>DeleteSex: %s</p>" % (delete_sex))
print("<p>DeleteAge: %s</p>" % (delete_age))
print("<p>DeleteTel: %s</p>" % (delete_tel))
print('<p><a href="/index.html">back</a></p>')
print("</body>")
print("</html>")

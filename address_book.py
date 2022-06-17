#!D:/Anaconda3/python.exe
# coding:utf-8

import cgi
import cgitb
import codecs
# CGI处理模块
import os
import string

from sqlalchemy import null

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

print("Content-type: text/html\n\n")
print
print("<b>通讯录</b><br>")
print("<ul>")
for i in range(len(list_name)):
    print("<li><table><tr><td>姓名: %s ;</td><td>性别: %s ;</td><td>年龄: %s ;</td><td>电话: %s ;</td></tr></table></li>" %
          (list_name[i], list_sex[i], list_age[i], list_tel[i]))
print("</ul>")
print('<p><a href="/index.html">back</a></p>')

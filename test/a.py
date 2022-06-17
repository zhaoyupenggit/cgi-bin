# CGI处理模块
import os
import cgi
import cgitb
import string
import codecs
from sqlalchemy import null

# 读取姓名文件，并将其转换为列表
fo = codecs.open("../data/name", "r", encoding="utf-8")
# print("文件名为: ", fo.name)
list_name = []
for line in fo.readlines():  # 依次读取每行
    line = line.strip()  # 去掉每行头尾空白
    list_name.append(line)
# print(list_name)
fo.close()

# 读取性别文件，并将其转换为列表
fo = codecs.open("../data/sex", "r", encoding="utf-8")
# print("文件名为: ", fo.name)
list_sex = []
for line in fo.readlines():  # 依次读取每行
    line = line.strip()  # 去掉每行头尾空白
    list_sex.append(line)
# print(list_sex)
fo.close()

# 读取年龄文件，并将其转换为列表
fo = codecs.open("../data/age", "r", encoding="utf-8")
# print("文件名为: ", fo.name)
list_age = []
for line in fo.readlines():  # 依次读取每行
    line = line.strip()  # 去掉每行头尾空白
    list_age.append(line)
# print(list_age)
fo.close()

# 读取电话文件，并将其转换为列表
fo = codecs.open("../data/tel", "r", encoding="utf-8")
# print("文件名为: ", fo.name)
list_tel = []
for line in fo.readlines():  # 依次读取每行
    line = line.strip()  # 去掉每行头尾空白
    list_tel.append(line)
# print(list_tel)
fo.close()

for i in range(len(list_name)):
    print(list_name[i]),
    print(list_sex[i]),
    print(list_age[i]),
    print(list_tel[i]),

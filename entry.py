#!D:/Anaconda3/python.exe
# coding:utf-8

# CGI处理模块
import cgi
import cgitb
import string
import codecs

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage()

# 获取数据
if form.getvalue('name'):
    site_name = form.getvalue('name')
else:
    site_name = 'nullname'
if form.getvalue('sex'):
    site_sex = form.getvalue('sex')
else:
    site_sex = 'male'
if form.getvalue('age'):
    site_age = form.getvalue('age')
else:
    site_age = '0'
if form.getvalue('tel'):
    site_tel = form.getvalue('tel')
else:
    site_tel = '000'

# 读取姓名文件，并将其转换为列表
fo = codecs.open("./data/name", "r", encoding="utf-8")
# print("文件名为: ", fo.name)
list_name = []
for line in fo.readlines():  # 依次读取每行
    line = line.strip()  # 去掉每行头尾空白
    list_name.append(line)
# print(list_name)
fo.close()


def search(site_name):
    if site_name in list_name:
        return list_name.index(site_name)
    else:
        return -1   # 返回-1表示没有找到


if search(site_name) == -1:  # 如果没有找到，则添加
    Num = search(site_name)
    # 录入数据
    entry_name = site_name
    entry_sex = site_sex
    entry_age = site_age
    entry_tel = site_tel

    # 写入姓名
    fo = open("./data/name", "a+")
    fo.writelines(site_name)
    fo.writelines("\n")
    fo.close()

    # 写入性别
    fo = open("./data/sex", "a+")
    fo.writelines(site_sex)
    fo.writelines("\n")
    fo.close()

    # 写入年龄
    fo = open("./data/age", "a+")
    fo.writelines(site_age)
    fo.writelines("\n")
    fo.close()

    # 写入电话
    fo = open("./data/tel", "a+")
    fo.writelines(site_tel)
    fo.writelines("\n")
    fo.close()

else:   # 如果找到，则打印已录入
    # 录入数据
    entry_name = 'Already entered\t' + site_name
    entry_sex = 'Already entered\t'
    entry_age = 'Already entered\t'
    entry_tel = 'Already entered\t'

print("Content-type:text/html\n\n")
print()
print("<html>")
print("<head>")
print("<title>Entry</title>")
print("</head>")
print("<body>")
print("<h2>Recorded</h2>")
print("<p>Name: %s</p>" % entry_name)
print("<p>Sex: %s</p>" % entry_sex)
print("<p>Age: %s</p>" % entry_age)
print("<p>Tel: %s</p>" % entry_tel)
print('<p><a href="/index.html">back</a></p>')
print("</body>")
print("</html>")

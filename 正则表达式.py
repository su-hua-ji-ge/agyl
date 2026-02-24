#1.正则表达式
#字符串处理工具
#要导入re模块
#特点：语法比较复杂，可读性较差。但是通用性强，适用于多种编程语言
import re
# re.match()  #进行匹配re.match可以匹配出xxx开头的字符串
# #pattern:匹配的正则表达式
# #string:要匹配的字符串
# ww = re.match("俗话",'俗话19')#必须要都有相同的字符串，才可以匹配 关键字为match 关键字查找。
# print(ww)
# # ftoup()  #上一步匹配成功就使用，froup()提取数据
# print(ww.group())
#
# #匹配单个字符
#1. . 匹配任意一个字符，除\n以外   ---常用
# dd=re.match("...","hellop")#要匹配多个字符加几个. 一个.对应一个字符
# print(dd)
# print(dd.group())
#2.[]匹配中列举的字符     ----常用
# aa = re.match("[he]",'hello') #匹配是在第二个，从第一个字符开始如果有则后面的不匹配，只会匹配一个
#匹配0-9  1
# aa = re.match("[0123456789]",'3421')
#匹配0-9  2
# aa = re.match("[0-9]",'3421')  #变式：0-35-9可以让其没有4
# print(aa)
# print(aa.group())
# 3.\d的匹配数字0-9
# res = re.match(r"...\d","2ff345")   #\d不可以匹配非数字
# print(res.group())
#4.\D匹配非数字
# res=re.match(r"..\D\D","fdas")  #只要不是数字都可以匹配
#print(res.group())
#5.\s匹配空白，即空格和tab键
# res=re.match(r"\s.."," hello") #一个tap键代表两个\s
# print(res.group())
#6.\S匹配非空白
# res=re.match(r"\S","babs   ") #不是空白都可以匹配
# print(res.group())
#7.\w匹配单词字符
# res=re.match(r"\w\w","bfuis")
# print(res.group())
# \W 匹配非单字符
# res=re.match(r"\W\W","。/")
# print(res.group())
#匹配多个字符      #前面都要有一个修饰的东西（符号）
#1.* 匹配前一个字符出现0次或者无限次，及可有可无   -----常用
# res = re.match(r"\w*","bibgebibgbig")  #由*号前面的符号表示其匹配什么值
# print(res.group())                                      #前面都要有一个修饰的东西（符号）
#2.+ 匹配前一个字符出现1次或者无限次，及至少一次   -----常用
# res = re.match(r".+","1地址在这里")
# print(res.group())
#3.? 匹配前一个字符出现1次或者0次       -----常用
# res = re.match(r"\d?","998hesld")
# print(res.group())
#4.{m}匹配前一个字符出现m次
# res = re.match(r"\d{10}","9999999765")
# print(res.group())
#{m,n}匹配前一个字符出现从m次到n次
#注意必须符合m小于n
# res = re.match(r"\d{4,8}","9999999765")  #这时表示最少匹配4位，最多匹配8位
# print(res.group())
#匹配开头结尾
#1.^匹配字符串开头：表示对：……取反
# res = re.match("oe","oefff")
# print(res.group())  #结果：oe
# #取反 注意^中[]表示不匹配
# res = re.match("[^oe]","fff")   #[^py]表示匹配除了py的字符剩下的开头
# print(res.group())  #结果：f
# #2.$ 匹配字符串结尾
res = re.match(".{8}$","bingbing")  #只有在满足条件的时候才可以进行筛选
print(res.group())
#find : 检测莫个子字符串是否包含在字符串中，如果在据返回字符串开始位置的下标，否则返回-1
#find格式：（'子字符串'，开始位置下标）(仍然包前不包后）
#开始位置和结束位置的下标都可以省略，表示在整个字符串中查找
# name ="发文发文发文发文"#汉字与字母都可以
# print(name.find("发")) #1 第一个下标为1
# print(name.find('发',1))# 检索的第一个bs的b下标为0
# print(name.find("文",3,5))

#index():检测莫个子字符串是否包含在字符串中，如果在据返回字符串开始位置的下标，否则报错
#index语法：（子字符串，开始位置下标，结束位置下标）
a="命运，在此显现！"
print(a.index("命",0,6))
print(a.index("！"))
print("********************")
#count(计数)():书整个字符串的数量，没有则显示0
a="asdfafds"
print(a.count("a"))
print(a.count("t"))
print(a.count("as"))

#1.startswith():是否以某个字符开头，是（True），不是（False）。设置开头和结束位置下标，则在指定范围内检查
#startswith（子字符串，开始位置下标，结束位置下标）
#示例：
sa='sixsixaa'
print(sa.startswith('six'))
print(sa.startswith('sax'))
print(sa.startswith('s,1,3'))#包前不包后
#2.endswith():是否以某个字符结尾，是（True），不是（False）。设置开头和结束位置下标，则在指定范围内检查
#endswith（子字符串，开始位置下标，结束位置下标）
#和startswith一样

#3.isupper():检测字符串中是否为大写，是（True）,否（False）
#格式：字符串名.isupper()

#修改元素
#1.replace():替换
#语法：replace("旧内容",'新内容',替换次数）(默认从左到右替换)
a="美好的一天，开始！"
print(a.replace("开始",'结束',1))

#2.split ( ):zh==指定分隔符切割字符串
#格式：字符串名称.split('分割的符号（汉字）',替换次数)(也默认从左到右替换)
a="美好的一天,开始！"
print(a.split(',')) #它以列表的形式返回 ['美好的一天', '开始！']
#如果字符串中不包含分割内容（它是把要分割的符号（汉字）替换，不是添加），则不分割。和作为一个整体输出。
print(a.split('！'))#输出结果分割的地方为( ',' )
print(a.split('dw'))

#3.capitalize():第一个字符大写，其他小写
sa='sixsixaa'
print(sa.capitalize())
#4.lower():大写转小写
sa='sixsixaa'
print(sa.lower())
#5.upper():小写转大写
sa='sixsixaa'
print(sa.upper())
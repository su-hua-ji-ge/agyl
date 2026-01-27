#1.类型转换
#1.1int():转换为一个整数，只能转换有纯数字组成的字符串
a = 1.2
print(type(a))#要转换时b =int(这个要为被赋予的浮点数的值)
b = int(a)
c = int(a)
print(b,type(b),c,type(c))
#浮点型强行整型后去掉小数点，并只保留整数
#例：print(int(13.45))
#str（字符串） --> int（整型）#只可转换纯数字字符串
a=int('1456')
#输出被转换的int整型print(type(a))可以确定已经转换成int整型
#print(int("agyl"))#报错
#print(int("俗话几个"))#报错
#所以字符串中有数字和正负好之外的字符就会报错,正负号要写在前面
# age = int(input("请输入你的年龄:"))
# if age >= 18:
#     print(age)

#1.2 flout()：转换成一个小数

print(float(11))#整型转换为浮点数会自动添加一位小数
#字符串中有正负号、数子和小数点以外的字符，不支持转换

#1.3str():任何类型转换为字符串
# a=100
# print(type(a))  <class 'int'>
# a1 = str(a)
# print(type(a1))   <class 'str'>
#float 转换为str会取出来末尾为0的小数部分（至少保留一位，去除其他的为0的部分）
li = [1,2,3]
st = str(li)
print(st,type(st))

#eval(str)
#让字符串也可以进行行运算
print(eval('1+5*5'))#整形和字符串不可以相加，使用时要在一个引号内

#eval() 可以实现list(列表),dict(字典),tuple(元组),str(字符串)
# #只要用正确的方式写出要转换的元素，然后定义一个值
# a = "[[1,2],[3,4],[5,6]]"
# li = eval(a)
# print(li,type(li))#按照此模板照做

#list():可将可迭代对象转换成列表
#注意必须是可迭代对象：str(字符串)，tuple(元组)，dict(字典)，set(集合)
#print(list(对应的数值格式))
#字典转换成列表，会取键名为列表的值
# print(list({'name':'agyl','age':18}))\
# 结果：['name', 'age']
#集合转换成列表，会先去重在转换
#print(list({'a','a','g'}))
#结果：['a', 'g']
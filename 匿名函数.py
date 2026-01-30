# #2.3lambda结合if判断
# a=6
# b=4
# # print("a比b小") if a<b else print("a大于b")
# #套用lambda
#先创建函数,输入形参，倒装句
com = lambda a,b : "a比b小" if a<b else "a大于b"
#结尾要输入实参
print(com(5,8))
#lambda适用于简单的代码（代码量少，逻辑简单），否则会徒增困难

# #内置函数
# #1.查看所有的内置函数

# import builtins
# print(dir(builtins))

#大写字母开头一般为内置常量名，小写字母开头一般为内置函数名
#内置函数1
# set():创建一个不重复元素集
#list():将可迭代对象转换成列表
#tuple():将可迭代对象转换成元组
#abs():返回绝对值（不管符号返回数字本体如：-10返回10）
#sum():求和
# print(sum(1,2,3))#整型不可迭代,字符串不可相加
print(sum({1.5,2,3.5}))#相加时有浮点数时结果必定为浮点数（小数）

#2.min() 求最小值
# max（）求最大值
#变式(在有负数时以绝对值求最大值)
print(max(1,5,3,6,8,key=abs))

#zip():将可迭代对象作为参数，将对象对应的元素打包成一个个元组
li = [1,2,3,4,5,9]
li2 = ['a','b','c','d','e','s']
print(zip(li,li2))
#取出zip
#1.for循环
for i in zip(li,li2):
    print(i)
#如果元素个数不一样，就按照长度最短的返回。多的会不显示
#2.列表
print(list(zip(li,li2)))#要是可迭代对象

#映射函数：map()
#map(func,iterl)：func：自己定义的函数，iterl要放进去的可迭代对象
li = [1,2,3,43]
def func(x):
    return x * 6
a= map(func,li)
print(a)
#for循环取出来
for i in a:
    print(i)
#列表输出
print(list(a))

#reduce():把对象的两个元素取出，计算出一个值然后保存着，接下来给第三个元素计算
#要先导包
from functools import reduce
# reduce(function,sequenae) function是必须有两个参数的函数，另一个序列：迭代对象
li2 = [1,2,3,4]
def add(a,b):
    return a+b#计算过程：1=a,2=b,a+b=1+2=3结果给a，而剩下的第3个参数给b如此循环
    #如果要a+2b时要写成2*b，这样1+2*3这样了
a=reduce(add,li2)
print(a)

#拆包
#直接取出数据（类似绝对值）
ass=(1,2,3,4,5,6)
#1.
# a,b,c,d,e,f=ass
# print(a,b,c,d,e,f)#直接用元组内的相同变量接受收
#一般在获取元组值时使用
#2.
#利用*可以取出多个的属性
a, *b= ass
print(a,b)
a=ass
print(a)
def asd(a,b,*c):
    print(a,b,*c)
asd(1,2,3,4,5,6)
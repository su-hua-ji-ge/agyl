#异常
# print(a)#异常
#当Python的解释器发现有错误时，会无法执行并给出错误提示
#格式1：
#try:
#可能引发异常现象的代码
#         不确定能否正常执行的代码
try:
    print(a)
except:   #默认基类异常
    print("出现错误！")
print("2号")
#变式
# except #NameError(异常类型) as a（取别名为）: #指定捕获异常为NameError,自定义名字为a
try:
    print(a)
except NameError as sd:
    print("NameError类型错误")
print("A")

#格式2
try:
    print(a)
except Exception as err: #万能捕获异常Exception
    print(err)
print("A")\
#格式3：多分支异常
try:
    pritn(s)
except IndexError as sa:
    print(sa)
except KeyError as sa:
    print("key错误")
except NameError as sa:
    print("命名错误")
print("S")

#else try代码块结束后运行的代码（没有异常时才会运行）
try:
    print("a")
except NameError as sa:
    print(sa)
else:
    print("没有捕获到异常")

#3.finally（无论是否有无异常都会执行）
# ---------

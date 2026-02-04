# #1.4被装饰的函数有参数
# def chiei(fn):
#     def iner(name):  #内函数，name是内函数的参数 #在这里写了什么，就要在被装饰的函数上 传什么。
#         print(f"{name}是iner函数的参数")
#         print("这是1号")
#         fn(name)
#     return iner
# @chiei
# def func(name):
#     print("这是被装饰的函数")
# func("bibi")
# print("-----------------")
# #标准版的装饰器
# st = chiei(cr1) #这时ot = iner
# st ("bivy") #此时才是调用内函数并要按照是否有参数，有就传参
# # print("-----------------")
# # #1.5被装饰的函数有可变参数*args,**kwargs
# # #被
# # def cr2(*args,**kwargs):#**kwargs接受 “键 = 值”，以字典形势输出。*args接受为空，输出空元组
# #     print(args)
# #     print(kwargs)
# # cr2(name="bibi",ss="fs")#以元组输出
# # def a():
# #     print("s")
# # def cote(name):#参数
# #     return 123 #如果return输出的结果为name则输出的结果为cote("实参")
# # print("sad",cote("bibi"))#这里cote("bibi")=123,sad（实参）=name(行参)
# print("-----------------")
# #可变参数*args, **kwargs
# def func(*args, **kwargs):
#     print(args)#以元组输出
#     print(kwargs)#以键等于值的形式
# def innt(fn):
#     def innr(*arge,**kwargs):
#         print("登录...")
#         fn(*arge,**kwargs)
#     return innr#innt("传参")()第二个小括号表示调用内函数
# ot = innt(func)
# ot("d,f",name="bibi") #name ="bibi"以键等于值的形式传递给kwargs

#多个装饰器
def decol(fn):
    def iner():
        return "hhh|"+fn()+"|hehehe"
    return iner
#2.个
def decol2(fn):
    def iner():
        return "ns"+fn()+"fcyx"
    return iner
#被装饰的函数1
@decol
@decol2
#遵守离被装饰函数最近的先执行（被@的从上往下的远近决定）
def test1():
    return "完事"
print(test1())
#这时decol的fn()=test1
# 应用场景：定义一个装饰器，然后在所有需要增强的函数上使用这个装饰器，那么所有被装饰的函数都有了装饰器里的增强方法了
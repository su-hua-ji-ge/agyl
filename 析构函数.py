# #析构函数
# #格式：__del__,删除对象时，解释器默认调用__del__
# class Per:
#     def __init__ (self):
#         print("我是__init__()")
#     def __del__ (self):
#         print("被销毁了")
# aa=Per()
# del aa#删除aa这个对象
# print("倒数第二行代码")
# print("aaaa")
#正常运行时，不会调用__del__(),对象执行结束之后系统会自动调用__del__(),同时也代表函数已经全部结束了
# # 封装
# #面向对象的三大特性：封装、继承、多态
# class per:
#     name="bibi"
# pe = per()
# # print(pe.name)
# # per.name = "zz"
# # print(pe.name)
#
# #隐藏属性（私有权限）
# #方法1：在属性名
# class per:
#     name="jnam"
#     __age =21
#     def int(self):
#         print(f"为了爱芮！永远{self.__age}岁！")
# e=per()
# print(e.name)
# # print(e.__name)
# #1.隐藏属性实际上是将名字修改为：_类名__属性名__ _per__age
# print(e._per__age)
# e._per__age= 18
# print(e._per__age)
# #方法2：在类的内部访问 #这个更加正规（推荐使用）
# e.int()
# per.__age=19
# e.int()

#_xxx:单下划线开头，声名私有属性/方法，定义在类中，外部可以使用，子类也可以继承（但是在另外的py文件
# # 中使用from xxx import * 导入时无法导入）
# class per:
#     name = "俗话几个"
# #     __age = 21  #隐藏属性
# #     _sex = "战列舰" #私有属性（单下划线）
# # a = per()
# # print(a._sex) #私有属性要在外部调用要用 对象名._属性名
# 隐藏属性方法
# #使用对象._类名__属性名访问隐藏属性（不正规方法）
# # print(a._per__age)
# class MAN:
#     def __play(self):
#         print("一个坚韧的男人")
#     def dina(self):
#         print("一个普通的智慧灵长类动物")
#         MAN.__play(self)
#         self.__play()#推荐使用这个
# ma = MAN()
# ma.dina()#使用后只要调用dina

#私有方法
class gi:
    def _buy(self):
        print("买")
g=gi()
g._buy()#可以子外部使用私有属性
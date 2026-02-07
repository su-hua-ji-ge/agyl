# #1.回顾
# #定义类
# class Ps:#(类)
#     name = "bibi"#类属性
#     def run(self):
#         print("人类会跑步",self)
# pa=Ps()
# print(pa)
# pa.run()
#
# #实列属性
# #格式：
# #self.属性名
# class Person:
#     name = "bibi"
#     def intt(self):
#         print(f"{self.name}的年龄：{self.age}")#这里的self.age是实例属性
#         #这里Person.name可以调用bibi，self.name也可以
# pe = Person()
# pe.age=20#这里要给实例属性附上值
# pe.sex="女"#这个是实例属性
# print(pe.sex)#根据对象名访问实例属性
# # print(Person.sex)#实例对象只能由对象名访问，不能由类名访问
# pe.intt()
# #访问类属性，类可以访问到，实例对象也可以访问到
# print(Person.name)
# print(pe.name)
# print("--------------")
# #实例属性和类属性的区别
# #类属性：是公共的
# #实列属性：是属于对象的，是私有的只能由对象名访问
# pe2 = Person()
# print(pe2.name)
# print(pe2.sex)#实例对象pe.sex="女"，是给pe对象新增的实例属性，其他对象没有

# 构造函数（要频繁实例化所要的属性时用其传值）
#格式：__init__()
#通常用来做属性初始化或者赋值操作，在类实例化对象时，会被自动调用
# class Test:
#     def __init__(self):
#         print("这是__init__()函数")
# te=Test()#自动调用
class sdf:
    name = "bibi"#类属性
    def __init__(self,name,age,hh,xb):#可以在这里将参数变为形参，并在实例化时写入实参
        self.name = name#前面有self的是实例属性
        self.age=age
        self.hh=hh
        self.xb=xb#还要把这里的参数改为自己
    def play(self):
        print(f"{self.name}打游戏")
    def intt(self):
        print(f"{self.name}的年龄{self.age},身高{self.hh},性别当然为：{self.xb}")
tt=sdf("bilinili",19,165,"女")
tt.play()
tt.intt()
#同理也可以二次实例化
aa=sdf("ailixiya",22,171,"女")#这里要再次传参实例化之间不会共享传参
aa.play()
aa.intt()
# __init__():初始化对象
from tkinter.font import names


class Test(object):
    def __init__(self):
        print("这是__init__()")
    def __new__(cls,*args,**kwargs):       #需要参数，必须让 __new__ 返回实例对象，否则 __init__ 不会执行（所以才重写）
        print("这是__new__()")
        print(cls)      #new的功能就一个就是创建对象（创建对象的过程是那两个，
                # 划分地址，返回对象引用），这段讲的是new重写，保留原功能的基础上在代码体里增加了一个print函数，对象创建完成init会自动调用
        res = super().__new__(cls)       #方法重写，res里保存的是实例对象的应用的引用__new__()是静态方法，形参里有cls,实参就必须传cls
        return res     #res相当于实例对象，没有返回这个实例对象的话，__init__是不会被调用的
    # 重写new方法的时候一定要return super().__new__(cls).否则解释器得不到分配空间的对象引用，不会调用__init__()
# te=Test()
# #__new__():object基类提供的内置的静态方法
# #作用：1.内存中为对象分配空间 2。返回对象的引用
# print(te)       #这里被new覆盖了，要想使用init就要用super(重写)

#执行步骤
#一个对象的实例化过程：首先执行__new__(),如果没有写__new__(),默认调用的是object里内置的__new__(),返回一个实例对象，
#然后再调用__init__()初始化

#1.new是本来默认就运行了的方法，它起到了做好准备工作的作
class Person(object):
    def __new__(cls, *args, **kwargs):
        print("这是new方法")
        opj= super().__new__(cls)
        print("返回值:",opj)
        return opj       #不要重复new
    def __init__(self,name):
        self.name = name  #实例属性
        print("名字是：",self.name)
#2.但如果这个new被你自己手动打进去，写了别的功能，它原本的“准备”功能就会被覆盖，导致其他的方法都不能运行(才要重写)

# pe=Person("bibi")
# print(pe)
# pe2=Person("susu")
# print(pe2)

#·__new__创建对象，__init__初始化对象
#·__new__返回对象引用，__init__定义实例属性
#·一个类，一个实例

class Person(object):
    name = "比比"      #类属性：类所拥有的属性
    def __init__(self):
        self.age=18          #实例属性：对象私有的
    # def play(self):
    #     print(f"{Person.name}在玩游戏")  #最好类名.属性名
    #     print(self.age)
    @staticmethod
    def introduce():
        print(f"我是{Person}f")     #静态方法能够访问类属性，但是毫无意义，静态方法不支持访问类属性
    @classmethod
    def show(cls):   #cls代表对象本身
        print(cls.name)    #所以cls可以替换掉类本身
#代表类对象本身
pe=Person()
pe.introduce()

#单例模式
#一个类里只有一个实例
#例：pc打开回收站时不管点多少次都只会且只有一个回收站窗口
#创建方式
#1.通过@classmethod
#2.通过装饰器
#3.通过重写__new__实现
#4.通过导入模块实现

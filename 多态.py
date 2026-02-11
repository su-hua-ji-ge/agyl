# 多继承的弊端：容易导致冲突
# 多态指同一种行为具有不同的表现形式
# 前提：继承，重写
# 特点：1.不关注对象的类型，关注对象具有的行为（不关注实例方法是否同名）
# 2.兼容性比较强
# 3.不同的子类对象，调用相同的父类对象会有不同的结果
# print(10+100+89)
class Ain:
    """父类：动物类"""
    def dho(self):
        print("叫声")
class Cat(Ain):
    def dho(self):
     """子类：猫类"""
    def dho(self):
        print("喵~（无感情）")
class Dog(Ain):
    """子类2：狗类"""
    def dho(self):
        print("汪！")
# cat=Cat()
# cat.dho()
# dog=Dog()
# dog.dho()
#大抵是同一种方法不同的表达方式
class Ain:
    def eat(self):
        print("吃饭")
class Pig:
    def eat(self):
        print("吃糠和杂粮")
class Dog(Ain):
    def eat(self):
        print("吃肉和骨头")
#统一接口
def test(obj): #形参
    obj.eat()
# ain=Ain()
# pig=Pig()
# dog=Dog()
# test(ain)
# test(pig)
# test(dog)
# #test函数传入不同的对象，执行不同的对象的eat的方法  （obj）
# #静态方法
#使用@staticmethod(static：静态)（method：方法），静态方法无self,cls参数的限制
#静态方法与类无关，可以被转换成函数使用d
class Person(object):
    @staticmethod
    def eat(name):
        print(f"{name}人类会学习")
Person.eat("dd")
pe=Person()
pe.eat("dd")  #调用方法时去传参，不用实例化简化

#类方法
#使用装饰器@classmethod(class：类 method：方法)来标识为类方法，对与类方法，第一个参数必须是类对象，一般是cls为第一个参数
#格式：
#class 类名:
    # @classmethod
    # def 方法名（cls,形参）
    #     方法体
#类方法内部可以方法类属性，或者调用其他的类方法
class Person(object):
    name = "bingbing"       #类属性
    @classmethod
    def sleep(cls):
        print("cls:",cls)    #cls代表类对象本身，类本质上就是一个对象
        print("睡觉")
        print(cls.name)
print(Person.sleep())
Person.sleep()
#当方法中需要使用类对象（如访问私有类属性等），定义类方法
#类方法一般是配合类属性使用
#类当然可以调用实例方法了，只不过要传一个对象实例的self参数进去，
# 静态方法就是优化掉实例化这一步，类方法不仅可以优化掉实例化，也可以当实例调用类方法时使用类属性
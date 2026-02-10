#经典类
#class A:     #经典类：不在任意内置类型派生的类
class A:
    def walk(self):
        print("走路")
class dog(A):
    name = "雷诺"#也是派生类
    def bite(self): #Dog是派生类
        print("恐喝")
    # pas  #不是派生类，没有不同于父类的东西
#class A()
#class A(object)  新式类：继承了object（对象）类或该类的子类都是新式类 ——————推荐
#opjcet:对象，python为所以对象提供的基类（顶级父类），提供了一些内置的属性和方法，可以使用dir()查看
# print(dir(object))
# python3中如果一个类没有继承任何类，默认object(python3)类，因此都是新式类

#多继承
#子类可以继承多个父类，并且具有所有父类的属性和方法
class F(object):
    def monee(self):
        print("成功继承稳定被动月收入100万美金~130万美金的产业")
class Mo(object):
    def money(self):
        print("经商能力+55+天赋+27，遗传影响+56+保养+29")
class Son(F,Mo):#父类哪个写在前面先调用那个
    def ww(self):
        print("经商82,颜值85")
s=Son()
s.money()#重名时，谁在子类中调用就近原则
s.monee()

#方法的调用顺序
print(Son.__mro__)#查看对应对象的顺序

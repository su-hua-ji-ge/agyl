# #继承（多继承和单继承)
# # 就是让类和类之间转变为父子关系，子类默认继承父类属性和方法
# #语法：class 类名（父类名）
#     # 代码块...
# # 单继承
# class fulei:
#     def rl(self):
#         print("吃饭")
#     def sd(self):
#         print("玩耍")
# class Girl(fulei):
#     pass  #占位符，类下面不写任何东西，会自动跳过
#     def gi(self):
#         print("化妆")
# class Boy(fulei):
#     pass
#     def bo(self):
#         print("锻炼")
# girl = Girl()
# girl.gi()
# girl.rl()#可以用父类的参数、方法
# boy=Boy()
# boy.bo()
# boy.sd()
# #继承的传递（多重传递）
#a,b,c c继承b,b继承a,c(子类)具有a,b类的方法和属性
class Father():
    def _eat(self):
        print("吃饭")
    def __al(self):
        print("睡觉")
class Cas(Father):
    def b(self):
        print("锻炼")
class ddd(Cas):
    def f(self):
        print("学习")
# d=ddd()
# d._eat()#私有属性也可以
# d._Father__al()#隐藏属性也可以
# d.b()
# d.f()

# #方法的重写
#在子类中定义与父类相同名称的方法
class P:
    def money(self):
        print("成功继承稳定被动月收入100万美金~130万美金的产业")
class Man(P):
    def money(self):
        print("自己净赚一千万美金和12个百万美金级的以及2个千万美金级的各绝对30%股权")
# man=Man()
# man.money()#如果子类重写了父类的方法会优先调用自己的方法
#对父类的方法子类可以增加自己的方法
#1.父类名，方法名
#2.super().方法名()   _------推荐使用
#3.super(子类名,self).方法名()
class P:
    def money(self):
        print("成功继承稳定被动月收入100万美金~130万美金的产业")
class Man(P):
    def money(self):
        # P.money(self)#第一种方法******
        # super().money()#第二种方法（推荐）本质上super类创建的对象，可以调用父类的方法
        super(Man,self).money()
        print("自己净赚一千万美金和12个百万美金级的以及2个千万美金级的各绝对30%股权")
man=Man()
man.money()
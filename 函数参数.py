#函数参数
#1.必备参数（位置参数）
# 含义：传递和定义参数的顺序及个数必须一致
#格式：def func(a,b)
def funa(name,name2,name3):
    print('名字：',name)
    print(name2)
    print(name3)
funa('a','b','c')#没有传参会报错,传参时前后数量一致
#默认参数
#为参数提供默认值，调用函数时可不传该默认参数的值
#格式：def 函数名(为参数提供默认值，例：a=2222)
def faio(a=23,):#所有位置参数必须出现在默认函数前，包括函数定义和调用
    print(a)
faio()#没有传值会根据默认值来执行代码
faio(3455)
#可变参数
#传入的值可以改变，可多也可少或不传
#格式：def 函数名(*arge*位置参数*)#*号可以让传多个函数
def func(*arge):
    print(arge)
    print(type(arge))
func(1,2,3)#传多个值时以元组形式接受
#可以接受数字，汉族，英文
#关键字参数
#格式：def 函数名(**kwargs)
def func2(**kwarge):
    print(kwarge)
func2(name='huan',age='19')#以字典的形式接受的,以字典的形式输出的键值对:采用键=值的形式
#作用：可以扩展函数的功能

#函数嵌套
#大致为：
def study(a,b):
    return a + b
print(study(a=1,b=2))
def ass():
    resul=study(a=5,b=6)#要有一个变量接受返回值（不可用Pythen关键字如if,return,for,while等）
    print(resul)
ass()
#函数定义
def dtue():#外函数
    print("俗话.")
    def aaa():#定义# 内函数
        print('几个！')
    aaa()#调用
dtue()
#内层不可调用外层（死循环）
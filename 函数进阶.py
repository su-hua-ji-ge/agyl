#作用域
#1.1指变量生效的范围，分为全局变量和局部变量
#全局变量和局部变量命名相同，全局变量不会被局部变量覆盖
#全局变量
#函数外部定义的变量，在整个文件中都是有效的
a=120#全局变量(值会被局部变量短暂影响但超出局部变量的影响之后，会继续变为全局变量的值)
def ea1():
    print("这是ea1的值：",a)
def ea2():
    a=140#局部变量
    print("这是ea2的值：",a)
print("这是函数前的a值：",a)
ea1()
ea2()
print("调用函数后的a值：",a)
#局部变量
#内部定义的变量，骢定义位置开始到函数定义结束有效
def eas():
    sim=43
    print("sim",sim)#只在函数体内
    return sim#就是这个=====
eas()
#sim()#在函数体外面不可调用局部变量
def wwa():
    aas=eas()
    print("eas的值:",aas)#不可以吧别的局部变量调用到别的函数体内，会显示那个局部变量的位置
wwa()
#如果想要用return函数返回值这样别的函数体会接受的局部变量得的值也算是用了

#函数：global可以将局部变量声名为全局变量

#1.5：nonlocal
#把嵌套函数中的第二层函数声明为第一层函数（上一层）
a=20
def eas():
    s=2
    def eas2():
        a=3
        # nonlocal s#只能声名上一层
        def eas3():
            nonlocal s
            def eas4():
                s=4
                print("第四层s的值：",s)
            eas4()
            s=6
            print("第三层s的值：",s)
        eas3()

        print("第二层s的值：",s)
    eas2()
    print("第一层s的值：",s)
eas()
#==========由此得出nonlocal函数只会将上层的函数声名，不会声名下层的

#匿名函数(lambda)
#语法：函数名 = lambda 形参：返回值（表达式）
#调用：结果 = 函数名（实参）
#普通函数与匿名函数的转换
def add(a,b):
    return a+b
print(add(1,3))
#==
add = lambda a,b: a+b#a,b是匿名函数的形参，a+b为表达式，函数名要等与lambda
print(add(1,3))
#lambda的参数格式
#无参数====
funas = lambda : "一桶水"
print(funas())
#1-2参数
ass = lambda name:name
print(ass("asdf"))
#默认函数
sdd = lambda name,age=23:(name,age)
print(sdd('d',18))
print(sdd('sd',43))
#多个函数
fina = lambda a,b=3,c=3:a+b*c
print(fina(3))
#默认参数必须写在非默认参数后面
#可变参数
#关键词函数
fidd = lambda **indd:indd#以字典（键值对）输出（写）
print(fidd(asdd='f',agr="sdf"))
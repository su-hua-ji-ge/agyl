# with open(r'D:\复习.txt','r',encoding='utf-8') as f:  #open()→打开文件，获取文件对象 f | as f 保存到
#     #data.a:文件路径 r:只读模式(如果文件不存在会报错)
#     content = f.read() #将f.read全部内容读取到content
#     print(content) #输出到content到屏幕（它的内容）----
# with open('D:\测试1.txt','w') as f: #用utf-8的编码格式解码
#     f.write("覆盖内容")

# try:
#     ff = input("请输入文件名或路径：")   #如果要让用户输入直接在里面嵌入输入程序
#     with open(ff,'r',encoding='utf-8') as f: #被赋值的值可以直接放到原来路径位置
#         ss=f.read()
#         print(ss)
# except FileNotFoundError: #收纳错误让其避免崩溃，且不会暴露文件路径
#     print("文件不存在")

# import os #os模块，Python标准库，提供操作系统相关功能，（一般用于处理文件路径、目录、环境变量等）
# def is_safe_path(path):
#     return '..' not in path and not os.path.isabs(path)
#函数逻辑分解 两个条件对必须满足，1 '..' not in path 不能包含 ..
#2 not os.path.isabs
#不能是绝对路径
# print(is_safe_path("date.txt")) #True 正确通过
# print(is_safe_path("../../etc"))  #False 错误不通过

# i = 0
# while i <10:
#     print(f"当前i等于{i}")
#     i += i + 1 #这是每次循环在原有值上加一，i += 1 意思为每次循环加一

def modify_list(lst): #定义一个名为modify_list的函数并接受了一个参数lst
    #通常为一个列表
    lst.append(0) #建一个可变对象，调用列表的append()方法
    return lst #显示返回修改后的列表
my_list = [1,2,3] #创建一个新列表并给my_list
re = modify_list(my_list) #调用modify_list(my_list)将结果放到re里
print(re)
#将修改函数封装成便于复用的函数，满足如多个地方要“给列表追加0”
modify_list([1,2,3])

def jisuan(a,b):
    return a+b,a*b,int(a/b)
jas = jisuan(8,4)
print(jas)

def my_func(x):
    y = x + 1
    return y
print(my_func(3))

try:
    with open("nof.txt","r",encoding="utf-8") as f:
        pass
except FileNotFoundError:
    print("警告：文件不存在")

a = 1
for i in range(3): #生成包含0,1,2的序列，包前不包后（不包含3）
    a += i
    print(a)

    
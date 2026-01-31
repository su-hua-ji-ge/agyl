# #2.4
# #抛出异常---raise
# #1.创建一个异常
# # raise Exception("错误")
# #实战
# #编写一个用户输入密码长度要大于大于等于6防止密码薄弱
# def ass():
#     a=input("请输入您的密码：")
#     if len(a)>=6:
#         return "密码保存成功"
#     raise Exception("密码要大于6位数，以保证您的账号安全")
# # print(ass())
#
# try:
#     print(ass())
# except Exception as a:#把异常处理成不会因为报错而停止的方法
#     print(a)
# print("as")

#模块
# py文件本质上是一个模块，导入就是执行另一个文件
# random、time、os、logging直接导入并使用
#第三方模块（第三方库）
#下载：cmd窗口pip install 模块名（要下载Python，而不是PyCharm）
#自定义模块
#及自己在项目中定义的模块

#导入模块import
#语法
#1.import 模块名
#调用：：模块名，功能名
import asss#自动运行asss.py
#调用某个函数
print(asss.name)
#print(模块名.函数名)
#导入模块方式2
#语法
#from ... import ... 功能1功能2
from asss import sa,sd,name#导入函数只需要函数名，不需要加上()
sa()
sd()
print(name)

#方式三
#from 模块名 import *  #直接将模块中的所有导入
from asss import *
sd()
#不建议使用过多from .... import ....声名，有时命名冲突会造成错误
#同名时会永远调用后面的

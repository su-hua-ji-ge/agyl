# os模块
import os
# 用于和操作系统进行交互
# 1.os.name
print(os.name)
#对于Windows,返回nt,对于Linux,返回posix
#2.os.getenv(环境变量名称) #读取环境变量
print(os.getenv("path"))
#3.os.path.split()  #作用：把目录和文件名分离，以元组的形式接受，第一个为目录路径，第二个元素是文件名
print(type(os.path.split(r"D:\py\.venv1")))
#os.path.dirname   #显示split分割的第一个元素，及目录
#os.path.basename  #显示split分割的第二个元素，即文件名
#print(os.path.basename(r"D:\py\.venv1\")  #报错，如果以/结尾返回空值，以\结尾为报错

con= input("请输入内容：")
mubiao = input("目标文件夹（路径)")
try:#尝试执行的代码块，如果出错，会跳转到except处理模块避免程序崩溃
    with open(mubiao, "w" , encoding="utf-8")as f:
#with open(…)上下文管理器自动处理文件的打开-操作-关闭
#w写入模式
        f.write(con)#这里是，需要在括号里写
    #入要传入的内容，或者说是被内容复制的函数&
        print("写入成功")
except FileNotFoundError:
 #当文件路径不存在时收录
 print(f"错误：路径{mubiao}不存在，检查路径是否输入正确")
except Exception as e:
#捕获所有会被前面处理的错误
    print(f"写入失败：{e}")
#as，将错误信息储存到,e:被存储的变量
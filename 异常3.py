# 1.3import 模块名 as 别名
# import asss as ass
# ass.sa()
#2.as给功能起别名
#语法：from 模块名 import 功能 as 别名
from asss import sd as a,name,sa as d
#要功能和功能隔开
a()
print(name)
d()
#2.模块（内置全局变量__name__）
#3.4.2 语法：

if  name  == "  main  ":
    print("main")
    #用来控制py文件在不同的应用场景执行不同的逻辑
#1:文件在当前程序执行时：__name__ == "__main__ " #被当模块导入时，下面的代码不会显示
#2:文件被当作模块时： __name-- == 模块名#完全相反，自己执行时不会显示，当模块时都会显示
import asss2
asss2.test()
print("--------------------")
#包：项目结构中的文件夹/目录
#区别普通文件夹的地方为：包含__intit__py的文件夹         #init是为了让编辑器识别这个文件夹是一个包
#创建方法，右键项目名，新建Python软件包（Python Package）
#防冲突
#import导入包时，会首先执行__init__.py的文件的代码
#方法一
# import pack
#方法二
# from 包名 import 文件名
# from pack import ssss
# ssss.main()
#__all__:；本质上是一个列表，列表里面的元素就代表要导入的模块
#可以控制导入
from pack import * #导入了all的[]里的
#某种意义上限制了导入模块，*只允许导入all[]里的

#套包
#一个包里可以套别的包
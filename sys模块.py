# sys模块
# sys作用:负责程序跟python解释器的交互
import  sys #导入sys模块
# 1.sys.getdefaultencoding():获取系统默认编码值
print(sys.getdefaultencoding())
#2.sys.path:获取环境变量的路径,跟解释器相关
print(sys.path[0])  #以列表(list)的形式返回,第一项为当前所在的工作变量
#sys.platform    #获取操作系统平台名称
print(sys.platform)
#sys.version         #获取python解释器的版本信息
print(sys.version)
print(sys.executable)#大致是获取开始程序的文件位置

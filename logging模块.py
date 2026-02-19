#导入logging模块
import logging
#作用：用于作用日志信息
#1.程序调试
#2，了解软件程序运行情况是否正常
#3，软件程序运行故障分析与问题定位
#基本排序
# CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTEST
# logging.debug("握手debug")
# logging.info("我是info")
# logging.warning("我是warning")
# logging.error("我是error")
# logging.critical("我是critical")
#logging默认的lecel为warning,只会显示级别大于warning的日志信息
#4.logging.basicConfig()  #配置root logging的参数
#1，filename:指定日志的文件名。 所有会显示的日志都会存放到这个文件夹
#2.filemoge:文件的打开方式默认a,追加模式
#3.level: 指定日志显示级别，默认是警告信息warning
#4.format: 指定日志的输出格式
logging.basicConfig(filename="log.log",filemode="w",level=logging.NOTSET,format="%(levelname)s:%(asctime)s\t%(message)s")
#format的格式：
#格式	描述
# (levelno)s	打印日志级别的数值
# %(levelname)s	打印日志级别名称
# %(pathname)s	打印当前执行程序的路径
# %(filename)s	打印当前执行程序名称
# (funcName)s	打印日志的当前函数
# %(lineno)d	打印日志的当前行号
# %(asctime)s	打印日志的时间
# %(thread)d	打印线程id
# %(threadName)s	打印线程名称
# %(process)d	打印进程ID
# (message)s	打印日志信息
# %(name)s	打印logger的名字
# (module)s	调用日志输出函数的模块名
# %(created)f LogRecord的创建时间，也就是当前时间， time.time0
# (msecs)d	LogRecord的创建时间的毫秒部分
# (relativeCreated)d	输出日志信息的，自logger创建以来的毫秒数
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

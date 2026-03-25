# a = input("请输入文件名或路径：")
# filename = f"输入{a}"
# if filename.endswith('.log'): #endswith()方法判断字符串是否以指定后缀结尾
#     print("这是一个日志文件")
# else:
#     print("这不是一个日志文件")

log_line = input("请输入复制的日志行：")
ip = log_line.split()[0].strip()#在这里split()将字符串根据空格拆分成列表，[0]表示取列表的第一个元素
 #strip()方法用于移除字符串首尾指定的字符（默认为空格或换行符）
#split()方法用于将字符串拆分成列表，默认以空格为分隔符
print(ip)

import sys
白名单1 = {22,80,443}
系统端口 = set(range(1,1024))
用户端口 = set(range(256,65536))
DANGEROUS_PORTS = {135,139,445,3389,22}
try:
    port = input("请输入端口号：")#这里将输入的端口号转换为整数类型
    if not port.isdigit():
        raise ValueError(f"{port}请输入纯数字内容")
    port = int(port)
    if port < 1 or port > 65535: #这里进行判断端口号是否在1 ~ 65535之间
        raise ValueError(f"错误{port}，请输入1 ~ 65535之间的整数")
except ValueError as e:
    print(f"输入错误：{e}")
    sys.exit(1)
if port in DANGEROUS_PORTS :  # 表示单条件触发：高危端口，这里先判断高危的端口然后嵌套一个if判断句，判断是否在白名单1中
    # 如果在白名单1中，建议使用
    if port in 白名单1:
        print(f"白名单端口{port}为高危端口，谨慎使用（请确认必要性）！")
        sys.exit(1)
        print(f"端口{port}为高危端口，不建议使用") 
        sys.exit(1)
elif port in 系统端口:
    print(f"端口{port}为系统端口，不建议使用")
    sys.exit(1)
elif  port in 用户端口:
    print(f"端口{port}为用户端口，建议使用")
    sys.exit(0)
else:
    print("端口号错误")
    sys.exit(1)

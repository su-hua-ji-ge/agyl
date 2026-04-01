import sys

# 定义扫描结果为列表的列表
scan_results = [
    [22, 80, 443, 8080],    # Web服务器
    [22, 3306, 80, 6379],   # DB+缓存服务器
    [21, 22, 23, 3389],     # 文件服务器（含高危端口！）
    [80, 443, 27017]        # 应用服务器
]

# scan_results = [4, 5345, 456]  # 这是错误的格式，应该是列表的列表
#以下将添加白名单端口的函数
def add_whitelist_port(whitelist): #whitelist为白名单列表的输入形参
    confirm = input("请输入y/n进行确认")
    if confirm == "y":
        print("继续")
        port_input = input("请输入要添加的端口：")
        if port_input.isdigit():
            port = int(port_input)
            print(f"已添加端口: {port}")
            whitelist.append(port)
            return True
        else:
             raise ValueError("请输入数字")
    elif confirm == "n":
        print("不继续")
        return False
    else:
        print("输入错误,请输入y或n")
        return False
#
try:
    high_risk_ports = [22, 3389] #高危名单
    whitelist_ports = [80, 22, 443] #白名单
    
    add_port = input("是否额外添加白名单端口？（y/n）")
    if add_port == "y":
        add_whitelist_port(whitelist_ports) #调用添加白名单端口的函数
        print(f"当前白名单端口：{whitelist_ports}")
    elif add_port == "n":
        print("不继续")
    else:
        print("输入错误,请输入y或n")
    
    # 遍历每个服务器的端口列表
    for server_ports in scan_results:
        # 检查是否存在高危端口
        if any(port in server_ports for port in high_risk_ports):
            print(f"该服务器存在高危端口{high_risk_ports},立刻退出")
            sys.exit(1)
        # 检查是否存在白名单端口
        elif any(port in server_ports for port in whitelist_ports):
            print("请注意，该服务器使用了白名单端口")
            confirm = input("是否继续？（y/n）")
            if confirm == "y":
                print("扫描完成,无异常")
            elif confirm == "n":
                print("不继续")
                sys.exit(0)
            else:
                print("输入错误,请输入y或n")
                sys.exit(1)
        else:
            print("扫描完成，未发现白名单端口")
    
    print("所有服务器扫描完成")
    
except ValueError as e:
    print(f"{e}")
except Exception as e:
    print(f"操作失败：{e}")
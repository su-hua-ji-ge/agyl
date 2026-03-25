ip_prv_ip = input("请输入IP:").split()
if not ip_prv_ip:
    print("IP不能为空")
    exit()
try:
    if  (ip_prv_ip.startswith("198.168.") or
         ip_prv_ip.startswith("10.") or
         ip_prv_ip.startswith("172.16.") or
         ip_prv_ip.startswith("172.16.")) :
        #使用：startswith来判断前后或固定格式的地方
        #是否与条件一样
        print("该网址为内网IP")
    elif ip_prv_ip.startswith("8.8.8.8"):
        print("该网址为外网IP，请注意!")
    else:
        print("未知IP类型")
except Exception as ee:
    print(f"格式错误:{ee}")

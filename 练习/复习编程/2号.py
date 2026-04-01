import sys
try:
    url = input("请输入URL（标准格式）:").strip() #去掉首尾空格
    if len(url) == 0:
        raise ValueError("URL不能为空")
#https://user:pass@www.example.com:8080/path/to/resource?query=param#fragment
#这是url的标准格式
    valid_protocols = ["http","https","ftp","ftps"] #授权通过的协议
    invalid_protocols = ["htto","hh"] #错误的协议
    separator = "://"
    if separator in url: #这里以"://"为分隔符
        protocol = url.lower().split(separator)[0] #全部小写，提取协议部分
        if protocol in valid_protocols:
            print("协议合法")
        elif protocol in invalid_protocols:
            raise ValueError("协议错误,未检测到授权通过的协议，请检查输入")
        else:
            raise ValueError("协议错误,未检测到授权通过的协议，请检查输入")
    else:
        raise ValueError("格式错误")
except ValueError as e:
    print(f"{e}，URL格式错误")
except Exception as e:
    print(f"操作失败：{e}")

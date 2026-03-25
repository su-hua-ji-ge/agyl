#methods = ["GET" , "POST" , "GET" , "PUT" , "GET" , "POST"]
methods = input("请输入Http（空格分割):").split()
jiben ={"GET","POST","PUT"}    
#if methods in jiben:,methods是列表，而jiben是一个集合
#不能使用in来判断，要用
if all(ff in jiben for ff in methods):
    print("格式正确")
else:
    print("格式错误！")
    exit()
fd_count = sum(1 for ff in methods if ff=="GET")
af_count = sum(1 for ff in methods if ff=="POST")
sd_count = sum(1 for ff in methods if ff=="PUT")
#这里endswith是判断字符串结尾是否匹配，改成如：
#ff == "目标"
print(f"GET数量为：{fd_count}， POST数量为：{af_count}，PUT数量为：{sd_count}")
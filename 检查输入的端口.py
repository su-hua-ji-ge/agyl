while True:
        es = input("请输入正确的端口：(1-65535)")
        if not es.isdigit():
            print(f"{es}发现非数字符号")
            continue #跳过本次循环重新输入
        port = int(es)#这里转换成整数
        if 1 <= port <= 65535:
                print(f"端口{es}")
                print("测试通过")
                break
        else:
            print("已超出有效端口范围")      
aa = input("是否继续输入？(y/n):") 
if aa == 'n':
    print("程序已退出")
    exit()
    #if ssj_hs(j,h)之中括号里面的内是在
    #要用该代码块时，输入的形参
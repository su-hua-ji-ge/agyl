import sys   #Import sys等于用户告诉客
#户我用了系统级退出

try:
    syl = input("请输入CPU使用率（如65）:")
    if not syl.isdigit():
        raise ValueError(f"{syl}请输入纯数字内容")
        syl = int(syl)
        if syl < 0 or syl > 100:
            raise ValueError(f"错误{syl}，请输入0 ~ 100之间的整数")
            print(f"CPU使用率为：{syl} %")
        if 100 >= syl >= 80: print("注意！CPU使用率过高，建议检查是否有异常进程运行")
        elif syl <= 79 and syl >= 71:
            print(f"CPU{syl}%为正常负载")
        elif 70 >= syl >= 60:
            print("CPU使用率正常")
        else: print("CPU使用率过低，建议检查是否有异常进程运行")

except ValueError as e:
    print(f"输入错误：{e}")
    sys.exit(1)#从exiy() 变成 sys.exit(1)时表示脚后跟可以被jenkins调用，能配ansible执行且能返回明确状态码给系统（可以勉强作为系统级脚本）
    #sys.exit(1):可以告诉客户的监控系统会据此报警
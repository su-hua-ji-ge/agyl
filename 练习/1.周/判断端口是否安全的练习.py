import  sys

scan_results = [
    [22, 80, 443, 8080],    # Web服务器
    [22, 3306, 80, 6379],   # DB+缓存服务器
    [21, 22, 23, 3389],     # 文件服务器（含高危端口！）
    [80, 443, 27017]        # 应用服务器
]
#此函数内包含，注册端口
zhuce = set(range(1025,49151))
#此函数包含动态端口
dongt = set(range(49152,65535))
#此函数内包含关键端口,谨慎!
guanjian = set(range(1,1024))
#扁平化：先创建一个函数块
#su_aa = []
#再做一个for循环且再嵌套一个判断子目标
#for scan_a in scan_results:#这里先找到每个子列表
    #for pare in scan_a:#然后这里再把每个子
    #列表中的端口找出来，复制到pare
        #然后再输出,然后再用append:没事，可以加三个列表，添
#加到列表末尾，最终得到一维列表
        #su_aa.append(pare)——
#扁平化
su_aa=[pare for scan_a in scan_results for pare in scan_a]
#[]:表示这个函数里面是列表
#pare = 最后输出到su_aa这个列表里面的出口
#然后后面的就能按照正常的表达式来看
#例如：for scan_a in scan_results :就可以按照正常的循环表达式来看待及遍历查看scan_results的各个子内容，并命名为pare
su_aa2 = list(set(su_aa))#利用list去重
#列出高危
gaowei = [21,23,3389]
#列出白名单
bai = [3566,565,1245]
#开始进行高危检测
for pare in su_aa2:
    if pare in gaowei:
        print(f"高危端口{pare}存在！")
#用户输入函数中，内容包含一部分系统端口，让其判断是否继续
while True:
        aa = input("输入内容中包含一部分系统端口，请检查判断是否继续(y/n)")
        if aa == "n":
             print("程序已退出")
             sys.exit(1)
        elif aa == "y":
            break
        else:
             print("请输入y或n")
        try:
              port=input("请输入要加入白名单的端口:")
              ata=map(int,port.split('-'))#
              bai = range(port)
        except ValueError:
              print("需要是整数")
        except Exception as e:
            print(f"发生未知错误:{e}")
for portt in su_aa2:
    if zhuce  in su_aa2:
        print("端口检测正常")
    elif dongt in su_aa2:
        print(f"端口{dongt}属于注册端口，在正常范围")
    
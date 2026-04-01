import sys
try:
    file_path = input("请输入要输入的文件路径：")
    shur = input("其输入：a(覆盖文件内容)，b(追加内容),c(读取文件内容)")
    shur = shur.lower() #将输入转换为小写
    shur = shur.strip() #移除首尾空格
    if len(shur) != 1: #这里!=1是判断输入是否为一个字符，如果不是一个字符，就提示用户输入一个字符
        print("输入错误,请输入一个字符")
        sys.exit()
    #根据用户输入进行操作,使用elif语句判断用户输入的字符是否为a,b,c中的一个
    if shur == "a": 
        # 覆盖文件内容
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("hello world")
            print("写入成功")
    elif shur == "b":
        # 追加内容
        with open(file_path, "a", encoding="utf-8") as f:
            f.write("hello world")
            print("追加成功")
    elif shur == "c":
        # 读取文件内容
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                print(f"文件内容：{content}")
                print("读取成功")
        except FileNotFoundError:
            print("文件不存在")
    else:
        print("输入错误,请检查输入是否为a,b,c的字母字符")
except Exception as e:
    print(f"操作失败：{e}")
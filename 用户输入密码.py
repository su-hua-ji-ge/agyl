password = input("请输入密码:")
while True:
    if len(password)  >= 8:
        print("设置完成")
        break
    else:
        print("不足字数限制，请重新设置")
        if input("是否重新设置或退出（y/n):")=="n":
         break
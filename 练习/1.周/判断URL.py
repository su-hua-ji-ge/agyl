as_sd = input("请输入URL：").strip()#优化之去掉首尾空格
if "://" in as_sd:
   clean_url = as_sd.lower()#这个的意思是全部转转小写
   wsa=clean_url.split("://")[0].strip()
   jiancha = {"http","https","ftp","ftps"} #本质上是将对应的合法，可通过协议赋值给一个函数（用{}）
   if wsa in jiancha: #这里会自动匹配哪种协议
   #本质上是if通过
       print(f"协议合法：{jiancha}")
   else:
       print(f"协议错误：非{jiancha}协议")
   exit()
   print(wsa)
else:
    print("格式错误")

    
    
filename = input("请输入文件：")
if ("password" in filename)  or ("secret" in filename) or ("key" in filename):
#if "password"  or "secret" or "key" in filename:
#or>in所以优先级不同，要用括号来强制改变优先级
      #这样是检查敏感词，是否在文件名中
    print("包含敏感词！")
    exit()
else:
    print("命名成功！")
 
print(any)
 #更高级，更简洁的函数:any()-----
filename = input("请输入文件：")
filename_lower = filename.lower()
#_代表的是调用某个函数(如a_lower,就是调用统一小写的这个函数)#同时赋值给filename_lower
ass = ["password","secret","key"]
#判断条件
if any(word in filename_lower for word in ass):
#if "password"  or "secret" or "key" in filename:
#or>in所以优先级不同，要用括号来强制改变优先级
      #这样是检查敏感词，是否在文件名中
    print("包含敏感词！")
    exit()
else:
    print("命名成功！")
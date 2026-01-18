st = "啊，好"#把st赋值
st1 = st.encode("utf-8")#然后写st用"utf-8“encode（解码）并赋值给st1
print(st1,type(st1))#type时要在再前面写一次要解码的被赋值者
st2=st1.decode("utf-8")
print(st2,type(st2))

print(20+20)
print("10"+"20")#数字分别加上"时中间的+变成了
a=214
b=6456
print(a,b,sep="^")

print("爱自己，爱众生\n"*6)
print("3\n\\3"*7)
# 2.2成员运算符
# 作用：检查字符串是否包含了某个子字符串(某一个或多个)
# in : 如果包含的话，返回Ture，不包含返回False
# not in : 如果不包含的话，返回Ture,包含返回False
a = "123456438759832475"
print('123456' in a) #对（True）
print('a' in a)#错（False）
print('12' not in a)#错（False）
print('asd' not in a)#对（True）
# 它们都要其中


